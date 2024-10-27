import asyncio
import sys
from contextlib import suppress
from bot.utils import logger
from bot.utils.launcher import process


async def main():
        await process()  # Тайм-аут 10 секунд


if __name__ == '__main__':
    try:
        with suppress(KeyboardInterrupt):
            asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("<r>Bot stopped by user...</r>")
        sys.exit(2)
