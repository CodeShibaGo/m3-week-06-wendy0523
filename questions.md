# Questions

## Q: 使用 `virtualenv` 建立虛擬環#116

安裝 pip install virtualenv
退出虛擬環境 deactivate

A: python3 -m venv venv
在你的目錄中創建一個名叫 venv 新的虛擬環境

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

load_dotenv() # 呼叫 load_dotenv 函數，讀取.env 再執行

server_ip = os.getenv("DOMAIN")#os.getenv()提取 DOMAIN 的值，並將值赋值给變數 server_ip
print(server_ip)#印出

## .env 與 .flaskenv 的差別

.env 中的變數不僅可以被 Flask 使用，還可以被其他程式或命令列工具所引用，需要安裝 python-dotenv 才可以自行載入，用於資料庫連接字串、API 金鑰等

.flaskenv 是 Flask 專用的配置文件，僅對 Flask 命令列工具和 Flask 應用程式有效，不會影響其他程式或命令列工具。它通常用於配置開發環境下的一些特定選項，如調試模式、自動重載等

.env 文件用於存儲應用程式的所有環境變數，
而.flaskenv 文件是 Flask 專用的配置文件

## Q: 如何使用 Flask-SQLAlchemy 連接上 MySQL？ #123

1.  安裝 mysql
    a. 在 MySQL[官網](https://dev.mysql.com/downloads/mysql/)安裝 MySQL  在你的`.bashrc`中加入這行，讓你可以使用 mysql 指令

    export PATH=${PATH}:/usr/local/mysql/bin

    b. 登入 MySQL，打完這個指令會需要輸入密碼，密碼就是你剛剛在安裝 MySQL 時輸入的密碼
    mysql -u root -p

2.  安裝 PyMySQL

    pip install PyMySQL

3.  建立資料庫

CREATE DATABASE data; 創建資料庫
USE data; 切換資料庫
SHOW DATABASES; 查看
exit 離開

4. Flask-SQLAlchemy

   a. 安裝 `pip install flask-migrate`

   b.載入 Flask-SQLAlchemy
   `from flask_sqlalchemy import SQLAlchemy`

   c.config：設定資料庫連線
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'mysql+pymysql://root:root@localhost:5000/data'
   db = SQLAlchemy(app)

   參考:https://medium.com/seaniap/python-web-flask-%E4%BD%BF%E7%94%A8sqlalchemy%E8%B3%87%E6%96%99%E5%BA%AB-8fc49c584ddb

## Q: Flask-Migrate 如何使用？ #124

Flask-Migrate 套件是用來來操作資料庫遷移管理，不需要重新建立資料庫資料庫，更方便新增或刪除,修改欄位。

a. 安裝 `pip install flask-migrate`

b.匯入 Flask-Migrate 套件
`from flask_migrate import Migrate`

c. 使用 Migrate 方法，第一個參數為 Flask app、第二個參數為 db 資料庫

`Migrate(app,db)`

d. 執行 init 指令

//MacOS/Linux，在終端機輸入指令來運行 Flask
`export FLASK_APP=microblog.py`

`flask db init` #執行後會看到專案目錄底下會出現 migrations 資料夾

`flask db migrate -m 'DB init'` #指令來產生 migration scripts

`flask db upgrade `#執行 upgrade 指令將 migration script apply to database

[參考資料]：(https://medium.com/seaniap/python-web-flask-%E5%AF%A6%E4%BD%9C-flask-migrate%E6%9B%B4%E6%96%B0%E8%B3%87%E6%96%99%E5%BA%AB-a5ebc930422a)
(https://flask-migrate.readthedocs.io/en/latest/#installation)

## Q: 如何使用 SQLAlchemy 下 Raw SQL？ #125

# SQLAlchemy

1. 匯入 text
   `from sqlalchemy import text`
   `from app import db`

在 SQLAlchemy 中，create_engine 函數用於連接資料庫和提供資料庫資料接受 URL 作為參數。
`engine = create_engine('mysql+pymysql://username:password@localhost/db_name')`

2. 使用 session.execute()
   `session.execute()` 方法允許你直接執行原始 SQL 語句。

#匯入 create_engine()
`from sqlalchemy import create_engine` #建立資料庫引擎
.`text()` 函數時，您可以將一個 SQL 字串作為參數傳遞
.`engine.connect()`用於建立與資料庫的連接的方法
.`execute()`用於執行 SQL 查詢或命令的方法

````with engine.connect() as con:

    rs = con.execute(text('select * from user'))

    for row in rs:
        print (row)
```
印出結果：
(1, 'John', 'john@example.com', 'password_hash_value', '1234567890')

. 使用engine.execute()執行原始 SQL(這種方法在 SQLAlchemy 2.0 中已被標記為過時)
[參考資料](https://www.atlassian.com/data/notebook/how-to-execute-raw-sql-in-sqlalchemy)

## Q: 如何用土炮的方式建立 Table？ #126

#IF NOT EXISTS 表格已存在不會再執行sql

```with engine.connect() as con:
    con.execute(text('CREATE TABLE IF NOT EXISTS members (MebmbersId INTEGER PRIMARY KEY,Address VARCHAR(255),MebmberPhoto BLOB)'))```

mysql> SHOW TABLES;
+-----------------+
| Tables_in_data  |
+-----------------+
| alembic_version |
| members         |
| user            |
+-----------------+
3 rows in set (0.01 sec)

[參考資料](https://www.atlassian.com/data/notebook/how-to-execute-raw-sql-in-sqlalchemy)


## Q: 什麼是密碼雜湊？如何使用 Python 實現？ #129
````
