from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# This installs the latest stable release
# Note: It's better to run pip commands in your terminal, not within the script.
# You would typically do: pip install python-telegram-bot --upgrade

# python bot.py
# Note: This line would typically be used to execute the bot script from the terminal.

url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soup_list_href = soup.find_all('a', {"class": "short-img img-fit"})
links_list = []
with open('link.txt', "w", encoding='utf-8') as f:
    for href in soup_list_href:
        links_list.append(href['href'])
        f.write(f"{href['href']}\n")

command = """/help - список всіх команд бота
/hello - привітання
/film - список найновіших фільмів
/about - інформація про бота
/source - посилання на код бота
/random_film - отримати випадковий фільм зі списку
/website - посилання на вебсайт з фільмами
/contact - зв'язатися з розробником"""

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привіт, {update.effective_user.first_name}!')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if links_list:
        response_text = "Ось список найновіших фільмів:\n"
        for i, link in enumerate(links_list):
            response_text += f"{i+1}. {link}\n"
        await update.message.reply_text(response_text)
    else:
        await update.message.reply_text("Наразі список фільмів порожній.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Цей бот надає інформацію про найновіші фільми з вебсайту uaserials.pro.")

async def source(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Вихідний код цього бота наразі недоступний.") # Replace with your actual source code link if available

import random
async def random_film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if links_list:
        random_link = random.choice(links_list)
        await update.message.reply_text(f"Випадковий фільм: {random_link}")
    else:
        await update.message.reply_text("Список фільмів порожній, тому неможливо вибрати випадковий фільм.")

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Переглянути всі фільми можна тут: {url}")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Ви можете зв'язатися з розробником через Telegram: @Bohdanddj") # Replace with your actual Telegram username

app = ApplicationBuilder().token("7755559564:AAEO2TdxXvGpBU4M51TVI0g7NXy5mDIMq54").build() # Replace with your actual bot token

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("source", source))
app.add_handler(CommandHandler("random_film", random_film))
app.add_handler(CommandHandler("website", website))
app.add_handler(CommandHandler("contact", contact))

app.run_polling()