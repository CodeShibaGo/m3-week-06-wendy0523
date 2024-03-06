# Questions

## Q: 使用 `virtualenv` 建立虛擬環#116

A: python3 -m venv venv
在你的目錄中創建一個名叫 venv 新的虛擬環境。

## Q: python-dotenv 如何使用？ #119

A:
參考資料：https://pypi.org/project/python-dotenv/

1. 安裝 python-dotenv
   pip install python-dotenv

2. 創建 .env 檔案

# Development settings

DOMAIN=example.org #開發應用時所使用的網域名稱
ADMIN_EMAIL=admin@${DOMAIN} #admin@example.org

3. 使用 load_dotenv 取值，可以配合 os 模組的 getenv()

from dotenv import load_dotenv #導入了 dotenv 庫中的 load_dotenv 函數。從.env 檔案中載入環境變數
import os

load_dotenv() # 呼叫 load_dotenv 函數，讀取.env 再執行。
server_ip = os.getenv("DOMAIN")
print(server_ip)

## Q: 如何使用 Flask-SQLAlchemy 連接上 MySQL？ #123

## Q: Flask-Migrate 如何使用？ #124

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

## Q: 如何用土炮的方式建立 Table？ #126

## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129
