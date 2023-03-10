from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5614118535:AAE8N8ayXQhlivTjrFAx3S_3YgzD0bDRll4'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nВот ссылка на оплату.\nВ ответ вышли пожалуйста квитанцию об оплате. \n https://pay.kaspi.kz/pay/yre4xsac")


@dp.message_handler(content_types=['document', 'photo'])
async def handle_files(message: types.Message):
    allowed_content_types = ['pdf', 'jpeg', 'png']
    print(message.content_type)
    if message.content_type not in allowed_content_types:
        await message.reply("Спасибо!")
        return

    # Process the file
    await message.reply("Спасибо за отправку файла.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
