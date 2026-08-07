import asyncio
from telethon import TelegramClient

# Получить здесь: https://my.telegram.org
API_ID = 38778596          # <-- Вставь свой api_id
API_HASH = "8f8d503ec35a33cd5a580b2aa4ec1248" # <-- Вставь свой api_hash

# Куда отправлять команды
CHAT = -1003716053846  # "me" - Избранное.
# Можно указать username, например "@username",
# либо ID чата.

COMMANDS = [
    "/sisi@sisiupbot",
    "/dick@themetrbot"
]

INTERVAL = 3600  # 1 час

client = TelegramClient("session", API_ID, API_HASH)


async def main():
    await client.start()

    print("Бот запущен.")

    while True:
        try:
            for command in COMMANDS:
                await client.send_message(CHAT, command)
                print(f"Отправлено: {command}")

                # Небольшая пауза между командами
                await asyncio.sleep(2)

            print("Следующая отправка через 1 час.")
            await asyncio.sleep(INTERVAL)

        except Exception as e:
            print("Ошибка:", e)
            await asyncio.sleep(60)


with client:
    client.loop.run_until_complete(main())