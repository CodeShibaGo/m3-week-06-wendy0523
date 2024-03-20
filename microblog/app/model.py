from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import text
from sqlalchemy import create_engine
from app import app,db

engine = create_engine('mysql+pymysql://root:112024112024@localhost:3306/data')
class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    
    phone_number: so.Mapped[Optional[str]] = so.mapped_column(sa.String(10))

    

    def __init__(self, username, email, password_hash,phone_number):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.phone_number = phone_number
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
with engine.connect() as con:

    rs = con.execute(text('select * from user'))

    for row in rs:
        print (row)
with engine.connect() as con:
    con.execute(text('CREATE TABLE IF NOT EXISTS members (MebmbersId INTEGER PRIMARY KEY,Address VARCHAR(255),MebmberPhoto BLOB)'))
