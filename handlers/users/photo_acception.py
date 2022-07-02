from aiogram import types

from loader import dp
from utils import photo_link
from utils import remove_background


@dp.message_handler(content_types="photo")
async def photo_handler(message: types.Message):
    photo = message.photo[-1]
    link = await photo_link(photo=photo)
    await message.answer(link)
    new_photo = await remove_background(link)
    await message.reply_document(document=new_photo, caption="Orqa fon olib tashlandi 😉")
        