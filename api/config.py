"""Config — constants and env vars."""
import os

BASE = "https://www.apnacollege.in"
IMPERSONATE = "chrome124"
TIMEOUT = 25
ADMIN_COOKIE = "se_admin"
TOKEN_TTL = 60 * 60 * 24 * 7
ADMIN_TTL = 60 * 60 * 4
BATCH_CACHE_TTL = 300

BRAND = "SeongEra_Study 📚✏"
TG_LINK = "https://t.me/SeongEraStudy"
TG_ADMIN = "https://t.me/Seong_Era"

ADMIN_CODE = os.environ.get("ADMIN_CODE", "12345678")
SUPABASE_URL = (os.environ.get("SUPABASE_URL") or "").rstrip("/")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY") or ""

UPI_ID = "yourupi@upi"
QR_IMAGE = "https://i.ibb.co/1Ghndgcb/IMG-20261015-162405-562.jpg"
