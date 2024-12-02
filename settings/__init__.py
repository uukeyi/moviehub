from split_settings.tools import include
import os
from dotenv import load_dotenv
load_dotenv()
include(
    'base.py',
    'dev.py' if os.getenv('DJANGO_ENV') == 'development' else 'prod.py',
)
