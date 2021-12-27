import logging
import os
from aiogram import Bot, Dispatcher, executor, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S %z')

if not os.environ.get('AIOGRAM_BOT_TOKEN'):
    logging.error('Environment variable AIOGRAM_BOT_TOKEN not found!')
    exit(1)

# Объект бота
bot = Bot(token=os.environ.get('AIOGRAM_BOT_TOKEN'))

# Диспетчер для бота
dp = Dispatcher(bot)


# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


if __name__ == '__main__':
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
