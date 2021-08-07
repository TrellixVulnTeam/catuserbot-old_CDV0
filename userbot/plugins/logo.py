"""
# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
"""
# modified by @jisan7509

import asyncio
import os
import urllib

from PIL import Image, ImageDraw, ImageFont

from .sql_helper.globals import addgvar, gvarstatus

BACKGROUND = ""
FOREGROUND = ""

fg_name = [
    "aliceblue",
    "antiquewhite",
    "aqua",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "black",
    "blanchedalmond",
    "blue",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "coral",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "cyan",
    "darkblue",
    "darkcyan",
    "darkgoldenrod",
    "darkgray",
    "darkgrey",
    "darkgreen",
    "darkkhaki",
    "darkmagenta",
    "darkolivegreen",
    "darkorange",
    "darkorchid",
    "darkred",
    "darksalmon",
    "darkseagreen",
    "darkslateblue",
    "darkslategray",
    "darkslategrey",
    "darkturquoise",
    "darkviolet",
    "deeppink",
    "deepskyblue",
    "dimgray",
    "dimgrey",
    "dodgerblue",
    "firebrick",
    "floralwhite",
    "forestgreen",
    "fuchsia",
    "gainsboro",
    "ghostwhite",
    "gold",
    "goldenrod",
    "gray",
    "grey",
    "green",
    "greenyellow",
    "honeydew",
    "hotpink",
    "indianred",
    "indigo",
    "ivory",
    "khaki",
    "lavender",
    "lavenderblush",
    "lawngreen",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgreen",
    "lightgray",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightslategrey",
    "lightsteelblue",
    "lightyellow",
    "lime",
    "limegreen",
    "linen",
    "magenta",
    "maroon",
    "mediumaquamarine",
    "mediumblue",
    "mediumorchid",
    "mediumpurple",
    "mediumseagreen",
    "mediumslateblue",
    "mediumspringgreen",
    "mediumturquoise",
    "mediumvioletred",
    "midnightblue",
    "mintcream",
    "mistyrose",
    "moccasin",
    "navajowhite",
    "navy",
    "oldlace",
    "olive",
    "olivedrab",
    "orange",
    "orangered",
    "orchid",
    "palegoldenrod",
    "palegreen",
    "paleturquoise",
    "palevioletred",
    "papayawhip",
    "peachpuff",
    "peru",
    "pink",
    "plum",
    "powderblue",
    "purple",
    "rebeccapurple",
    "red",
    "rosybrown",
    "royalblue",
    "saddlebrown",
    "salmon",
    "sandybrown",
    "seagreen",
    "seashell",
    "sienna",
    "silver",
    "skyblue",
    "slateblue",
    "slategray",
    "slategrey",
    "snow",
    "springgreen",
    "steelblue",
    "tan",
    "teal",
    "thistle",
    "tomato",
    "turquoise",
    "violet",
    "wheat",
    "white",
    "whitesmoke",
    "yellow",
    "yellowgreen",
]
fg_list = "`aliceblue` , `antiquewhite` , `aqua` , `aquamarine` , `azure` , `beige` , `bisque` , `black` , `blanchedalmond` , `blue` , `blueviolet` , `brown` , `burlywood` , `cadetblue` , `chartreuse` , `chocolate` , `coral` , `cornflowerblue` , `cornsilk` , `crimson` , `cyan` , `darkblue` , `darkcyan` , `darkgoldenrod` , `darkgray` , `darkgrey` , `darkgreen` , `darkkhaki` , `darkmagenta` , `darkolivegreen` , `darkorange` , `darkorchid` , `darkred` , `darksalmon` , `darkseagreen` , `darkslateblue` , `darkslategray` , `darkslategrey` , `darkturquoise` , `darkviolet` , `deeppink` , `deepskyblue` , `dimgray` , `dimgrey` , `dodgerblue` , `firebrick` , `floralwhite` , `forestgreen` , `fuchsia` , `gainsboro` , `ghostwhite` , `gold` , `goldenrod` , `gray` , `grey` , `green` , `greenyellow` , `honeydew` , `hotpink` , `indianred` , `indigo` , `ivory` , `khaki` , `lavender` , `lavenderblush` , `lawngreen` , `lemonchiffon` , `lightblue` , `lightcoral` , `lightcyan` , `lightgoldenrodyellow` , `lightgreen` , `lightgray` , `lightgrey` , `lightpink` , `lightsalmon` , `lightseagreen` , `lightskyblue` , `lightslategray` , `lightslategrey` , `lightsteelblue` , `lightyellow` , `lime` , `limegreen` , `linen` , `magenta` , `maroon` , `mediumaquamarine` , `mediumblue` , `mediumorchid` , `mediumpurple` , `mediumseagreen` , `mediumslateblue` , `mediumspringgreen` , `mediumturquoise` , `mediumvioletred` , `midnightblue` , `mintcream` , `mistyrose` , `moccasin` , `navajowhite` , `navy` , `oldlace` , `olive` , `olivedrab` , `orange` , `orangered` , `orchid` , `palegoldenrod` , `palegreen` , `paleturquoise` , `palevioletred` , `papayawhip` , `peachpuff` , `peru` , `pink` , `plum` , `powderblue` , `purple` , `rebeccapurple` , `red` , `rosybrown` , `royalblue` , `saddlebrown` , `salmon` , `sandybrown` , `seagreen` , `seashell` , `sienna` , `silver` , `skyblue` , `slateblue` , `slategray` , `slategrey` , `snow` , `springgreen` , `steelblue` , `tan` , `teal` , `thistle` , `tomato` , `turquoise` , `violet` , `wheat` , `white` , `whitesmoke` , `yellow` , `yellowgreen`"

bg_name = ["red", "blue", "white", "black", "purple"]
bg_link = [
    "https://telegra.ph/file/698854d6e231455877413.jpg",
    "https://telegra.ph/file/7264fe9488a0a1484cf6f.jpg",
    "https://telegra.ph/file/210ac4c5ead2d4a3bbabb.jpg",
    "https://telegra.ph/file/47fce894d66ae67e3665f.jpg",
    "https://telegra.ph/file/e05c66b5c101d7e1e10f7.jpg",
]

font_name = "1. `Streamster`\n2. `Streetwear`\n3. `Sabo-Regular`\n4. `RoadRage-Regular`\n5. `Redressed_Regular`\n6. `BERNIER Distressed`\n7. `BERNIER Shade`\n8. `West Side`\n9. `still time`\n10. `Thunderstorm`\n11. `Alt_Retro_Light`\n12. `Pirata_One_Regular`"
logo_font = [
    "Streamster",
    "Streetwear",
    "Sabo-Regular",
    "RoadRage-Regular",
    "Redressed_Regular",
    "BERNIER Distressed",
    "BERNIER Shade",
    "West Side",
    "still time",
    "Thunderstorm",
    "Alt_Retro_Light",
    "Pirata_One_Regular",
]
logo_font_link = [
    "https://github.com/Jisan09/Files/blob/main/fonts/Streamster.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/Streetwear.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/Sabo-Regular.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/RoadRage-Regular.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/Redressed_Regular.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/BERNIER%20Distressed.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/BERNIER%20Shade.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/West%20Side.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/still%20time.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/Thunderstorm.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/Alt_Retro_Light.ttf?raw=true",
    "https://github.com/Jisan09/Files/blob/main/fonts/Pirata_One_Regular.ttf?raw=true",
]


@bot.on(admin_cmd(pattern="lf(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="lf(?: |$)(.*)", allow_sudo=True))
async def lang(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    data = dict(zip(logo_font, logo_font_link))
    if not input_str:
        await edit_delete(
            event, f"**Available font names are here:-**\n\n{font_name}", time=60
        )
        return
    if input_str not in logo_font:
        catevent = await edit_or_reply(event, "`Give me a correct font name...`")
        await asyncio.sleep(1)
        await edit_delete(
            catevent, f"**Available font names are here:-**\n\n{font_name}", time=60
        )
    else:
        string = data[input_str]
        if os.path.exists("temp/logo.ttf"):
            os.remove("temp/logo.ttf")
            urllib.request.urlretrieve(
                string,
                "temp/logo.ttf",
            )
        await edit_delete(
            event, f"**Font for logo changed to :-** `{input_str}`", time=10
        )


@bot.on(admin_cmd(pattern="fg(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="fg(?: |$)(.*)", allow_sudo=True))
async def lang(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str:
        await edit_delete(
            event,
            f"**Available foreground color names are here:-**\n\n{fg_list}",
            time=20,
        )
        return
    if input_str not in fg_name:
        catevent = await edit_or_reply(
            event, "`Give me a correct foreground color name...`"
        )
        await asyncio.sleep(1)
        await edit_delete(
            catevent,
            f"**Available foreground color names are here:-**\n\n{fg_list}",
            time=20,
        )
    else:
        addgvar("FOREGROUND", input_str)
        await edit_delete(
            event, f"**Foreground color for logo changed to :-** `{input_str}`", time=10
        )


@bot.on(admin_cmd(pattern="(bg|cbg)(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="(bg|cbg)(?: |$)(.*)", allow_sudo=True))
async def lang(event):
    if event.fwd_from:
        return
    cmd = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    if cmd == "cbg":
        if input_str.startswith("https://telegra.ph"):
            addgvar("BACKGROUND", input_str)
            await edit_delete(
                event, f"**Background for logo changed to :-** `{input_str}`", time=10
            )
            return
        else:
            await edit_delete(event, "Give a valid Telegraph picture link.", time=10)
            return
    data = dict(zip(bg_name, bg_link))
    if not input_str:
        await edit_delete(
            event, f"**Available background names are here:-**\n\n{bg_name}", time=10
        )
        return
    if input_str not in bg_name:
        catevent = await edit_or_reply(event, "`Give me a correct background name...`")
        await asyncio.sleep(1)
        await edit_delete(
            catevent, f"**Available background names are here:-**\n\n{bg_name}", time=10
        )
    else:
        string = data[input_str]
        addgvar("BACKGROUND", string)
        await edit_delete(
            event, f"**Background for logo changed to :-** `{input_str}`", time=10
        )


@bot.on(admin_cmd(pattern="logo (.*)"))
@bot.on(sudo_cmd(pattern="logo (.*)", allow_sudo=True))
async def adityalogo(message):
    if message.fwd_from:
        return
    reply_to_id = await reply_id(message)
    event = await edit_or_reply(message, "`Processing.....`")
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return
    if gvarstatus("BACKGROUND") is None:
        urllib.request.urlretrieve(
            "https://telegra.ph/file/47fce894d66ae67e3665f.jpg", "temp/bg_img.jpg"
        )
    else:
        BACKGROUND = gvarstatus("BACKGROUND")
        urllib.request.urlretrieve(BACKGROUND, "temp/bg_img.jpg")
    img = Image.open("./temp/bg_img.jpg")
    draw = ImageDraw.Draw(img)
    if not os.path.exists("temp/logo.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/DevsExpo/FridayUserbot/blob/master/bot_utils_files/Fonts/Streamster.ttf?raw=true",
            "temp/logo.ttf",
        )
    font = ImageFont.truetype("temp/logo.ttf", 220)
    if gvarstatus("FOREGROUND") is None:
        FOREGROUND = "yellow"
    else:
        FOREGROUND = gvarstatus("FOREGROUND")
    image_widthz, image_heightz = img.size
    w, h = draw.textsize(text, font=font)
    h += int(h * 0.21)
    draw.text(
        ((image_widthz - w) / 2, (image_heightz - h) / 2),
        text,
        font=font,
        fill=FOREGROUND,
    )
    file_name = "LogoBy@MeisNub.png"
    img.save(file_name, "png")
    await message.client.send_file(
        message.chat_id,
        file_name,
        reply_to=reply_to_id,
    )
    await event.delete()
    if os.path.exists(file_name):
        os.remove(file_name)
        os.remove("temp/bg_img.jpg")


CMD_HELP.update(
    {
        "logo": "__**PLUGIN NAME :** Logo__\
\n\n📌** CMD ➥** `.logo` <Text>\
\n**USAGE   ➥  **Make a logo of ur desire text.\
\n\n📌** CMD ➥** `.cbg` < Telegraph Link of Image> \
\n**USAGE   ➥  **Changes the background for logo with custom image\
\n\n📌** CMD ➥** `.bg` <color name>\
\n**USAGE   ➥  **Changes the background for logo with built-in color\
\n\n📌** CMD ➥** `.fg` <color name>\
\n**USAGE   ➥  **Changes the foreground for logo with built-in color\
\n\n📌** CMD ➥** `.lf` <font name>\
\n**USAGE   ➥  **Changes the font for logo"
    }
)
