# Thanks For: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/ramadhani892/RamPyro-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/ramsupportt


from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "😖")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/eda4816a97d4e74445fc0.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Yo pler aing userbot.")
API_HASH = getenv("API_HASH", "6e06fb8f7b42fb33821f272597321bc1")
API_ID = getenv("API_ID", "8529843")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001692751821]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1001667983274") or 0)
BOT_TOKEN = getenv("BOT_TOKEN", "5955445604:AAHfetV9cxbp9s9YCCJU3GxKgYLwuZ2lvb8")
BOT_VER = "1.0.3@master"
BRANCH = getenv("BRANCH", "main")
CH_SFS = getenv("CH_SFS", "chnlwiki")
IG_ALIVE = getenv("IG_ALIVE", "saya_wiki")
CHANNEL = getenv("CHANNEL", "AboutWiki")
CMD_HANDLER = getenv("CMD_HANDLER", ",", "*", "-", "_")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "AboutWiki")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/geezrampy/Ram-Pyro")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAhIHQAKtaxwLeqhaFNlqWcAFdGOFxhsIZ1eIVXAzL0JwB5gN5V4n-6XYiXpuuXm8PMRSTbKj5_0c4PgA3o33IFtPfls4bz-BUV2tpK0FQcibUUmAEDwHmxLSF09Or0SawVzLoFJjL5dtWhIDPGMjJI3zAiniUzqj_Szos8nJqzYDj76mOJWZk9_VgIcFM4e0JW5u3vjuc43XeJsQYNWlefNujM8sDxWIzW_3sPdMGBZrPJb-bNTk1TahaD1FryHuiBfcVSd5esuzfMkbVnc-9boOWfRkoQL2Q-a8Ipi-Qy2aOGxxdWWBOqNY5aKYVGnZU361plxxaf1zhjdixTWPiStdQTRgAAAAB_KaBGAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQA-CqDsFaocMOy4ZUo_-iv3ga88m0ZQI9zxm8wX1zzVIoQC70g07WcdU7QkJYug8zWkydUJhIb7yqRUuynXEnHeVwdVbdeSsNEJNDg4RYpMQEOjvotyPnLn0KNBJlqNZNJnWENDanXZX8lcUPo3DZuyZHaoyj2dnSLvWkl0i8M0oh6-8Y-UIT_FFj1NpcLUQWA4b1NIVmvDFx2xUKvzluPohhZ72A3jefBPIapVATFWVTIUlYf2H8Jue5ehjGSX5dkbQVxjFBUIigxFSLVYbPy6JvgAgImjMB0ZgYGffhzsMHhtOjXBepx0OCF6lgDBhuZHcacn-FixKB_x26Je-EqRdgzYWwA")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
