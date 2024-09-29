import asyncio
import sys
from contextlib import suppress

from bot.utils import logger
from bot.utils.launcher import process


async def main():
    # Встановлюємо тайм-аут на 10 секунд (можна змінити час)
    try:
        await asyncio.wait_for(process(), timeout=410.0)
    except asyncio.TimeoutError:
        logger.warning("<r>Bot stopped due to timeout...</r>")
        sys.exit(1)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("<r>Bot stopped by user...</r>")
        sys.exit(2)
