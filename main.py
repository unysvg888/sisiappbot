import asyncio
from telethon import TelegramClient

# Получить здесь: https://my.telegram.org
API_ID = 38778596
API_HASH = "8f8d503ec35a33cd5a580b2aa4ec1248"

# Куда отправлять команды
CHAT = -1003716053846  # "me" - Избранное.

COMMANDS = [
    "/sisi@sisiupbot",
    "/dick@themetrbot",
    "фарма"
]

client = TelegramClient("session", API_ID, API_HASH)


async def main():
    await client.start()
    
    print("✅ Бот подключился. Отправляю команды...")
    
    for command in COMMANDS:
        try:
            await client.send_message(CHAT, command)
            print(f"✅ Отправлено: {command}")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"❌ Ошибка при отправке {command}: {e}")
    
    print("✅ Все команды отправлены. Завершаю работу.")
    await client.disconnect()

# Запускаем скрипт
asyncio.run(main())