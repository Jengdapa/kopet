import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "29075024"))
API_HASH = getenv("API_HASH", "6fcfe9d0effb1068ce5d12b2372953c8")
BOT_TOKEN = getenv("BOT_TOKEN", "5934867038:AAHPSxjCZwRsLBK1PB58w4RZ7-qNoEHO2fA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
STRING_SESSION = getenv("STRING_SESSION", "BQCefUrlkjE7s_UFkdOoFlWGo4K7UsxjLUIubLWq8B8xd1O5J3SF_JzaBI-s5y2qDxTWohQ23Mr2EiXgHAvU_8GQ3NnYCDbu796oIggCDdgdJOQ3OMLvSyJegMfa1bDTIieOnzJxnZro9WzbbwkRHYGfiT3igqIzKHygtlwpNnqyhaMF8DzVmA9hlZpaOdkSe4Z_gCgkl1q2QjPngs343e8y5CFt4r-UmJQXp_spUy2_hiLzQRDPRpRclu6K7zrj8zext1A7eCebOfnjAHqgFbc1j27LfGOfft3HWBYbK9iHNgzb8C4uCVKhJfaUL-kd8FTxCFChF3TSVGs1YKiS3FZKAAAAAGSITs8A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1004299209").split()))
