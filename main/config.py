from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

CHANNELS = [
    ("https://t.me/Zangoriekran_kanali", -1002107248547, "Zangori Ekran"),
    ("https://t.me/Yummy_multik", -1001652312277, "Yummy"),
    ("https://t.me/kinoolami_asilmedia_zakazkino", -1001377886442, "Zakaz Kinolar")
]

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_HOST = env.str("DB_HOST")
DB_PORT = env.str("DB_PORT")
DB_NAME = env.str("DB_NAME")

