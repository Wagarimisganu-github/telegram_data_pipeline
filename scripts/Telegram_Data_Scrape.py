import nest_asyncio
import asyncio
from telethon import TelegramClient
import pandas as pd
import os
import re
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("scraping_log.txt"),
        logging.StreamHandler()
    ]
)


api_id = '21313820'
api_hash = 'a7e1d9f7b7624b94dc919894ea2a150e'
phone = '+251911851800'

client = TelegramClient('session_name4', api_id, api_hash)

if not os.path.exists('telegram_images'):
    os.makedirs('telegram_images')

def extract_information(message_text):
    price = None
    phone = None
    price_pattern = r'(\d+[\.,]?\d*\s?(?:birr|\$))'
    prices = re.findall(price_pattern, message_text.lower())
    if prices:
        price = ', '.join(prices)
    phone_pattern = r'(\+251\d{9}|\d{10})'
    phones = re.findall(phone_pattern, message_text)
    if phones:
        phone = ', '.join(phones)
    return price, phone

async def scrape_channel(channel_username):
    messages = []
    try:
        async for message in client.iter_messages(channel_username, limit=50000):
            message_text = message.message
            price, phone = extract_information(message_text) if message_text else (None, None)
            media_file_path = None
            if message.media:
                media_file = await message.download_media(file='telegram_images/')
                media_file_path = media_file
            messages.append({
                'channel': channel_username,
                'sender_id': message.sender_id,
                'message': message_text,
                'date': message.date,
                'price': price,
                'phone': phone,
                'media_file_path': media_file_path
            })
        logging.info(f"Successfully scraped {len(messages)} messages from {channel_username}.")
    except Exception as e:
        logging.error(f"Error scraping channel {channel_username}: {e}")

    return messages

async def scrape_multiple_channels(channel_usernames):
    all_messages = []
    for channel in channel_usernames:
        logging.info(f"Scraping channel: {channel}")
        channel_messages = await scrape_channel(channel)
        all_messages.extend(channel_messages)
    df = pd.DataFrame(all_messages)
    df.to_csv('telegram_multiple_channels_data.csv', index=False)
    logging.info("Data saved to telegram_multiple_channels_data.csv.")

async def main():
    async with client:
        channels = ['CheMed123', 'lobelia4cosmetics']
        await scrape_multiple_channels(channels)

nest_asyncio.apply()

await main()
