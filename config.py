import os
from dotenv import load_dotenv

load_dotenv()

USER_MONGO = os.getenv("USERS") or ""
PASSWORD_MONGO = os.getenv("PASSWORD") or ""
