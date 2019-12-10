import pymysql,log,linecache,sys,getpass
import myfunction as fc

def open(db_id,db_pw):
    conn = pymysql.connect(
        host = 'ec2-52-78-148-250.ap-northeast-2.compute.amazonaws.com',
        port = 3306,
        user = db_id,
        password = db_pw,
        db ='lolparty',
        charset ='utf8'
        )
    return conn

def check_connect():
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT VERSION()"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if rows:
            return True
        else:
            return False
    except:
        print("CONNECTION ERROR")
    return False

def call_error():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print(f"EXCEPTION IN ({filename}, LINE {lineno} '{line.strip()}'): {exc_obj}")

def check_exist(table,discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT * FROM {table} WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        rows = cursor.fetchall()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()
        return False if len(rows) > 0 else True


def get_streamer():
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT * FROM streamer"
        cursor.execute(sql)
        rows = cursor.fetchall()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()
        return rows if len(rows) > 0 else None
            

def set_streamer(info):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"INSERT INTO streamer VALUES('{info[0]}','{info[1]}','{info[2]}','{info[3]}','{info[4]}')"
        cursor.execute(sql)
        conn.commit()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()

def del_streamer(name):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"DELETE FROM streamer WHERE name='{name}'"
        cursor.execute(sql)
        conn.commit()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()

def up_streamer(discord_id,dec):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"UPDATE streamer SET dec='{dec}' WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()

def get_party(discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT party_name FROM member WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        rows = cursor.fetchone()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()
        return rows[0] if len(rows) > 0 else None


def set_party(discord_name,discord_id,party_name,party_dec):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"INSERT INTO party (discord_name,discord_id,party_name,party_dec) VALUES('{discord_name}','{discord_id}','{party_name}','{party_dec}')"
        cursor.execute(sql)
        conn.commit()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()

def set_partymemeber(party_name,discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"UPDATE member SET party_name='{party_name}' WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()

def del_partymember(discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"UPDATE member SET party is NULL WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()

def set_member(discord_id,discord_name,summoner_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"INSERT INTO member (discord_id,discord_name,summoner_id) VALUES('{discord_id}','{discord_name}','{summoner_id}') ON DUPLICATE KEY UPDATE summoner_id = '{summoner_id}', discord_name = '{discord_name}'"
        cursor.execute(sql)
        conn.commit()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()
        

def get_member(discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT * FROM member WHERE discord_id = '{discord_id}'"
        cursor.execute(sql)
        rows = cursor.fetchone()
        conn.commit()
    except:
        call_error()
    finally:
        cursor.close()
        conn.close()
        return rows if len(rows) > 0 else None


check=False
while check==False:
    db_id = input("Enter DB ID : ")
    db_pw = input("Enter DB PW : ")
    check = check_connect()