import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "18743539"))
API_HASH = getenv("API_HASH", "e0c6aefdf03392c545e01bf9c068134f")
BOT_TOKEN = getenv("BOT_TOKEN", "5934867038:AAHPSxjCZwRsLBK1PB58w4RZ7-qNoEHO2fA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
STRING_SESSION = getenv("STRING_SESSION", "BQASluOTioWmlO3umdTfiMgSpIB76t8P0MkV4YXqW-VfGesfY_bA-SdR2VAep96DbR5a3RaIIPqpOOqtK53ALr-xzZlkt42fJUvGsp7umhG_-i7-pQgjN9I1QZ0EhRPKNevsUWqfovxDOEq3b5RCuS35lqfyz6fRtKVAVj9aC22t4AXWRp8XfI3X91_F7riHK2HLrYWQaAr4D-CmcLjAugsYLwpNQTTalK0d5RdrSx609re_HfEH34wcNAmFPzpNBXIdwSCv7b30J2kkNy4YzyXzBbP2R1bUo0jBHZ5YcBXyG157ns0CrAmbeQhbc6cAYXCjzcjne-BYdIwJNFHK_F1QO9xjyQA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1004299209").split()))
