from pyrogram import Client
import random

from bot.config import settings
from bot.utils import logger

android_device = random.choice([
    'SM-G960F', 'SM-G973F', 'SM-G980F', 'SM-G960U', 'SM-G973U', 'SM-G980U',
    'SM-A505F', 'SM-A515F', 'SM-A525F', 'SM-N975F', 'SM-N986B', 'SM-N981B',
    'SM-F711B', 'SM-F916B', 'SM-G781B', 'SM-G998B', 'SM-G991B', 'SM-G996B',
    'SM-G990E', 'SM-G990B2', 'SM-G990U', 'SM-G990B', 'SM-G990', 'SM-G990',
    'Pixel 2', 'Pixel 2 XL', 'Pixel 3', 'Pixel 3 XL', 'Pixel 4', 'Pixel 4 XL',
    'Pixel 4a', 'Pixel 5', 'Pixel 5a', 'Pixel 6', 'Pixel 6 Pro', 'Pixel 6 XL',
    'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro', 'IN2010', 'IN2023',
    'LE2117', 'LE2123', 'OnePlus Nord', 'IV2201', 'NE2215', 'CPH2423',
    'NE2210', 'Mi 9', 'Mi 10', 'Mi 11', 'Mi 12', 'Redmi Note 8',
    'Redmi Note 8 Pro', 'Redmi Note 9', 'Redmi Note 9 Pro', 'Redmi Note 10',
    'Redmi Note 10 Pro', 'Redmi Note 11', 'Redmi Note 11 Pro', 'Redmi Note 12',
    'Redmi Note 12 Pro', 'VOG-AL00', 'ANA-AL00', 'TAS-AL00',
    'OCE-AN10', 'J9150', 'J9210', 'LM-G820', 'L-51A', 'Nokia 8.3',
    'Nokia 9 PureView', 'POCO F5', 'POCO F5 Pro', 'POCO M3', 'POCO M3 Pro'
])

async def register_sessions() -> None:
    API_ID = settings.API_ID
    API_HASH = settings.API_HASH

    if not API_ID or not API_HASH:
        raise ValueError("API_ID and API_HASH not found in the .env file.")

    session_name = input('\nEnter the session name (press Enter to exit): ')

    if not session_name:
        return None

    session = Client(
        name=session_name,
        api_id=API_ID,
        api_hash=API_HASH,
        app_version='1.6.7',
        device_model=android_device,
        workdir="sessions/"
    )

    async with session:
        user_data = await session.get_me()

    logger.success(f'Session added successfully @{user_data.username} | {user_data.first_name} {user_data.last_name}')
