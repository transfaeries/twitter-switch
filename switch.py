import tweepy
import pluralkit
import os
import logging
import asyncio

pk = pluralkit.Client(os.environ['PK_TOKEN'])
logging.basicConfig(level=logging.INFO)

async def main():

    system = await pk.get_system()
    logging.info(system.description)

    members = pk.get_members()
    async for member in members:
        logging.info(f"{member.name} (`{member.id}`)")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

