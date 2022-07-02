from ast import Bytes
from loader import dp, bot
import aiohttp
from aiogram.types import Message
from io import BytesIO
from utils import background_remove
from aiogram import types


async def photo_link(photo: types.photo_size.PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        form = aiohttp.FormData()
        form.add_field(
            name="file",
            value=file
        )
        async with bot.session.post("https://telegra.ph/upload", data=form) as response:
            image_src = await response.json()
        
        link = "http://telegra.ph/" + image_src[0]["src"]
        return link



