import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "29075024"))
API_HASH = getenv("API_HASH", "03e2e866d262d8e6ad69f431c73392c9")
BOT_TOKEN = getenv("BOT_TOKEN", "5766907095:AAFgR4per1ZxAw0C0pGa0PAI0kBFCdnbGyw")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
STRING_SESSION = getenv("STRING_SESSION", "BQAFx9qx-dWdzyQMQe_fJF_HiyEAo-zlnsIXffv6GdIMagVzPwp0z-T2Qs5x7Z1_SesOl73a4jqHbCFJYtO49Ey0mO-v5K1q5d3nQ2ofOQ7GdhbvKU2tn4-f1Yl3KqKQ5Cao01ITY13v3ROvDN6SETJt2AUri6knz4ZYNksiUfA7Gtr0CnY60zcip5ayyQeafpCNLPe0-Gi7EtebS1PLnqKJaa-BBVFn-9Eoewjbs8p7rEYDwl_r_sZ5fdrbZqe65SPD6kbIhUaerDgtFEwHYCBWWomnM9VNErrKGP8164JABNOGpA5uLEWTz21eER4qXWn-qb2uHyttmkYQ1bBIG8j5a5EdwQA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1004299209").split()))
