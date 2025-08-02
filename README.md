# generate-password-telegram-bot

Бот для генерации паролей в телеграмме. Пароли снегерированы с помощью библиотеки secrets, поэтому они полностью безопасны

Технологии:

aiogram 3.21.0 (для взаимодействия с Telegram Bot API). pip install aiogram
asyncio (для асинхронного запуска). pip install asyncio
secrets (для генерации безопасного пароля. Библиотека random небезопасна, так как её можно предугадать).
string (для работы с текстом).
os и dotenv (для загрузки токена бота). pip install python-dotenv
