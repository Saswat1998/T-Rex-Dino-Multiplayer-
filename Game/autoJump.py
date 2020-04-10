while True:
    global ts
    c, addr = s.accept()
    data=c.recv(16)
    stringdata = data.decode('utf-8')
    if stringdata == "Jump" and (datetime.now()-ts).total_seconds() > 1:
        print("Jumped")
        pgui.press("space")
        ts=datetime.now()

    c.close()