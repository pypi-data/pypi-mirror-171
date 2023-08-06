import asyncio
import math
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from aiohttp import ClientSession
from nonebot import logger
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot_plugin_htmlrender import get_new_page
from playwright.async_api import Page, ViewportSize

from .const import SCHALE_DB_DIFFERENT, SCHALE_URL

PAGE_KWARGS = {
    "is_mobile": True,
    "viewport": ViewportSize(width=767, height=800),
}


async def schale_get_stu_data():
    async with ClientSession() as c:
        async with c.get(f"{SCHALE_URL}data/cn/students.min.json") as r:
            return await r.json()


async def schale_get_stu_dict():
    ret = await schale_get_stu_data()
    data = {x["Name"].replace("(", "（").replace(")", "）"): x for x in ret}

    for schale, gamekee in SCHALE_DB_DIFFERENT.items():
        if schale in data:
            data[gamekee] = data[schale]
            del data[schale]

    return data


async def schale_get_stu_info(stu):
    async with get_new_page(**PAGE_KWARGS) as page:  # type:Page
        await page.goto(
            f"{SCHALE_URL}?chara={stu}", timeout=60 * 1000, wait_until="networkidle"
        )

        # 进度条拉最大
        await page.add_script_tag(content="utilStuSetAllProgressMax();")

        return await page.screenshot(full_page=True)


async def schale_get_calender(server=1):
    async with get_new_page(**PAGE_KWARGS) as page:  # type:Page
        await page.goto(
            SCHALE_URL,
            timeout=60 * 1000,
            wait_until="domcontentloaded"
            # html加载完成需要立马改服 commit事件太早
        )

        await page.add_script_tag(
            content=f"regionID={server};" "loadModule('home');"  # 改服  # 防止进入之前的模块
        )
        await page.wait_for_load_state("networkidle")

        return await (
            # 当时活动标题的上级节点
            await page.query_selector('xpath=//*[@id="ba-home-server-info"]/..')
        ).screenshot()


async def draw_fav_li(lvl):
    try:
        stu_li = [
            x
            for x in await schale_get_stu_data()
            if (x["MemoryLobby"] and x["MemoryLobby"][0] == lvl)
        ]
    except:
        logger.exception("获取schale db学生数据失败")
        return "获取SchaleDB学生数据失败，请检查后台输出"

    if not stu_li:
        return f"没有学生在羁绊等级{lvl}时解锁L2D"

    txt_h = 48
    pic_h = 144
    icon_w = 182
    icon_h = pic_h + txt_h
    line_max_icon = 6
    txt_y_offset = -4

    if (l := len(stu_li)) <= line_max_icon:
        line = 1
        length = l
    else:
        line = math.ceil(l / line_max_icon)
        length = line_max_icon

    img = Image.new("RGBA", (icon_w * length, icon_h * line), (255, 255, 255))
    font = ImageFont.truetype(
        str((Path(__file__).parent / "res" / "SourceHanSansSC-Bold-2.otf")), 25
    )

    async def draw_stu(name_, dev_name_, line_, index_):
        img_card = Image.new("RGBA", (icon_w, icon_h), (255, 255, 255))

        async with ClientSession() as s:
            async with s.get(
                f"{SCHALE_URL}images/student/lobby/Lobbyillust_Icon_{dev_name_}_01.png",
            ) as r:
                ret = await r.read()
        icon_img = Image.open(BytesIO(ret)).convert("RGBA")
        img_card.paste(icon_img, (0, 0), icon_img)

        font_w, font_h = font.getsize(name_)
        draw_x = 0 if font_w >= icon_w else round((icon_w - font_w) / 2)
        draw_y = round((txt_h - font_h) / 2) + pic_h + txt_y_offset
        draw = ImageDraw.Draw(img_card)
        draw.text((draw_x, draw_y), name_, (0, 0, 0), font)

        img.paste(img_card, (index_ * icon_w, line_ * icon_h))

    task_li = []
    l = 0
    i = 0
    for stu in stu_li:
        if i == line_max_icon:
            i = 0
            l += 1
        task_li.append(draw_stu(stu["Name"], stu["DevName"], l, i))
        i += 1
    await asyncio.gather(*task_li)

    ret_io = BytesIO()
    img.save(ret_io, "PNG")
    return MessageSegment.text(f"羁绊等级 {lvl} 时解锁L2D的学生有以下这些：") + MessageSegment.image(
        ret_io
    )
