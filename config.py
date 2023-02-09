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
DB_URL = getenv("DATABASE_URL", "postgres://tlqjytgo:5L7q4eK2t1PDCcfyKsrzz6o_A-e4Pu-w@trumpet.db.elephantsql.com/tlqjytgo")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "AboutWiki")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/Wiki28/RW")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBBj3nq6459SsnbE9yqHiorRd2QbEnU7NDooNFXG1PU1XEGGOAZXRPQNjgJrzx3g11XqVjKlSBYu1XPc5b4gLh7BcepoyvUF7ViZv4pAIriPqjCD9sQWV8wCG4Rn0A95_jX5oqlK_GaZPq_BFwQDU3E13COADub11vziJVQN8UwMnzafPPi0xygpi_tiag_X-dHKxxq9YFFRg4JPohJZlh1e9SCrm9XKne034wuohxHguXLrLw0iaYAOAi9uf0ZwvyvOSQJRznn5jx8SiXOSQPejjA5uoq1P4ZO_j0junZELbYYJZmxvPZvty-paJJpWQCWdAohH7WFMFT2_rGvFDfymgRgA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
