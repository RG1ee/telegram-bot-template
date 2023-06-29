import os
from dotenv import load_dotenv

load_dotenv()


TOKEN: str = os.getenv("BOT_TOKEN", default="a;lskjdf;laieojwfwkljslajls;df")
DB_NAME: str = os.getenv("DB_NAME", default="db")
