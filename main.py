# -*- coding: utf-8 -*-
import os

try:
    import mariadb
except:
    os.system('cmd /k "python -m pip install mariadb"')

try:
    conn = mariadb.connect(
        user="root",
        password="Synology123.",
        host="192.168.0.100",
        port=3306,
        database="Storage"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()



while 1:
    cmd = input("CMD: ")


    #CMD Search
    if cmd == "search":
        dat = input("type & value: ").split()
        cur.execute("SELECT * FROM Main WHERE type = ? and value = ? ", (dat[0], dat[1],))

        for (id) in cur:
            print("id", id[0])
            print("pos", id[1])
            print("led", id[2])
            print("type", id[3])
            print("value", id[4])
            print("pcs", id[5])



    #CMD ADD
    if cmd == "add":
        dat = input("ADD: Type, Value, PCS to add: ").split()
        PCS = 0
        kusy = 0
        cur.execute("SELECT * FROM Main WHERE type = ? and value = ? ", (dat[0], dat[1],))
        for (id) in cur:
            ID = id[0]
            PCS = int(id[5])
        kusy = PCS + int(dat[2])
        cur.execute("UPDATE Main SET PCS = ? WHERE ID = ?",(kusy, ID))


    #CMD RM
    if cmd == "rm":
        dat = input("ADD: Type, Value, PCS to RM: ").split()
        PCS = 0
        kusy = 0
        cur.execute("SELECT * FROM Main WHERE type = ? and value = ? ", (dat[0], dat[1],))
        for (id) in cur:
            ID = id[0]
            PCS = int(id[5])
        kusy = PCS - int(dat[2])
        cur.execute("UPDATE Main SET PCS = ? WHERE ID = ?", (kusy, ID))
