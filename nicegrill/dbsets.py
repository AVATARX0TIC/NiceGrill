from database.allinone import *

if not get_auth() or not getPM():
    stickerchat = "INSERT INTO auth (id) VALUES (0)"
    auth(stickerchat)
    max = "INSERT INTO antipm (max) VALUES (3)"
    setPM(max)
    notif = "UPDATE antipm SET mute = 1"
    setPM(notif)
    supblock = "UPDATE antipm SET supblock = 0"
    setPM(supblock)
    antipm = "UPDATE antipm SET anti = 1"
    setPM(antipm)

if not getStats():
    setStats("INSERT INTO stats (id, name, msg) VALUES (1, 'NiceGrill Bot', \"Hold on...Whaaa.. I'm alive 🤥🤥\")")

if not getpath():
    setpath("INSERT INTO downloader (path) VALUES ('./')")
