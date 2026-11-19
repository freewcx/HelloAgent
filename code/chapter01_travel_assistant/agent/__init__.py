from pathlib import Path

from dotenv import load_dotenv

# .env 在仓库根目录：agent/ → chapter01_travel_assistant/ → code/ → HelloAgent/
# 显式指定路径，不依赖自动向上搜索
load_dotenv(Path(__file__).resolve().parents[3] / ".env")
