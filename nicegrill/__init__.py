from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
from nicegrill import dbsets
import functools
import asyncio
from nicegrill.main import main
from nicegrill.modules import _init
from config import API_HASH, API_ID, SESSION
<<<<<<< Updated upstream
=======
from telethon.sessions import StringSession
>>>>>>> Stashed changes
import pandas as pd
import sqlite3
import os


if not API_ID or not API_HASH:
    API_ID = int(input("Enter your API ID:"))
    API_HASH = input("Enter your API HASH:")
    file = open("config.py", "a+")
    file.write(f"API_ID={API_ID}\nAPI_HASH=\"{API_HASH}\"")
    file.close()

if not SESSION:
<<<<<<< Updated upstream
    print("Run generate_session.py to create a string session first")
    break
=======
    print("Run generate_session.py first to get your string session")
    return
>>>>>>> Stashed changes

async def restore(client):
    async for msg in client.iter_messages((await client.get_me()).id, limit=2):
        if msg.document and msg.document.attributes[0].file_name == "database.db":
            await client.download_media(msg)
            await msg.delete()
    qtables = "SELECT * FROM sqlite_master WHERE type='table'"
    if not os.path.isfile("database.db"):
        return
    olddb = sqlite3.connect("database.db")
    tables = pd.read_sql(qtables, olddb)
    newdb = sqlite3.connect("database/database.db")
    newcur = newdb.cursor()
    for table in tables.index:
        newcur.execute(f"DROP TABLE IF EXISTS {tables.name[table]}")
        newcur.execute(tables.sql[table])
        qcols = pd.read_sql(f"SELECT * from {tables.name[table]}", olddb)
        qcols.to_sql(
            tables.name[table],
            newdb,
            index=False,
            if_exists="append")
    os.system("rm *.db*")
    newdb.commit()
    olddb.close()
    newdb.close()


<<<<<<< Updated upstream
with TelegramClient(StringSession(SESSION) , API_ID, API_HASH) as client:
=======
with TelegramClient(StringSession(SESSION), API_ID, API_HASH) as client:
>>>>>>> Stashed changes
    asyncio.get_event_loop().create_task(restore(client))
    client.parse_mode = 'html'
    _init.loads()
    main.read(client)
    client.add_event_handler(
        functools.partial(main.outgoing),
        events.NewMessage(outgoing=True, forwards=False))
    client.add_event_handler(
        functools.partial(main.outgoing),
        events.MessageEdited(outgoing=True, forwards=False))
    print(f"Logged in as {(client.get_me()).first_name}")
    client.run_until_disconnected()
