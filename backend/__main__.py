import asyncio
from backend.connectors.base_connector import BaseConnector
from dotenv import load_dotenv
from backend.types import Chain

load_dotenv()

asyncio.run(BaseConnector(Chain.ETHEREUM, None, None, None, None).monitor_liquidations(aave_version='V2'))
# print(Chain.ETHEREUM.name)