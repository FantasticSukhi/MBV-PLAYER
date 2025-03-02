import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","GARUD_NETWORK_OWNER")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "MAMBA_MUSIC_XBOT")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "RIYA MUSIC")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "itz_m3_riya")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://theriyamusic94:f67KlgTyzr3TTutn@cluster0.lym5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 99999*))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002337113505))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7448520005))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/FantasticSukhi/RIYA_MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/GARUD_NETWORK")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+ppwQp_YKizBiMGU1")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "99999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "99999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 50))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQAoNHoACRGZcqbrJyltmPGBL5rjwfH9jHQesmn3TGO_zdEY8QDBAmqGUJ624UI06r3dEebvIW_ZRn02hVAB-gJrOtwca6TR-TbJFsjoG2pL4-y2pdI8awy7xB_puZGKxRRELIPq_UfwVh_mIOwOR0EA-RJuXgwQrz15fLbyQbu0TCs4oMfMiAfu2oGVPtEkB4SqaUpnyxV78A-PkueD3o3Uoi0xmOrHngo1fRZT4AJH8h8KgXYR1Dcem7H3p_U96asjTTQBSkvbEYPhmVkiGDtqyZu2rpzIOyrIDwYcJJzQuCTtWQ3_Y3E8uX-a2N3vLxsehUkeA-WJTw0oet6-fnN6kTXSBgAAAAHG9g2BAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
)
PLAYLIST_IMG_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
STATS_IMG_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
TELEGRAM_AUDIO_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
TELEGRAM_VIDEO_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
STREAM_IMG_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
SOUNCLOUD_IMG_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
YOUTUBE_IMG_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
SPOTIFY_ARTIST_IMG_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
SPOTIFY_ALBUM_IMG_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"
SPOTIFY_PLAYLIST_IMG_URL = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
