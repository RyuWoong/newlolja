import pymysql,log,linecache,sys,getpass,datetime
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

def call_error(ex):
    raise ex

def check_exist(table,discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT * FROM {table} WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        rows = cursor.fetchall()
    except Exception as ex:
        call_error(ex)
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
    except Exception as ex:
        call_error(ex)
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
    except Exception as ex:
        call_error(ex)
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
    except Exception as ex:
        call_error(ex)
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
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def get_partyList():
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT * FROM party"
        cursor.execute(sql)
        rows = cursor.fetchall()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()
        return rows if len(rows) > 0 else None

def get_party(discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT party_name FROM member WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        rows = cursor.fetchone()
    except Exception as ex:
        call_error(ex)
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
    except Exception as ex:
        call_error(ex)
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
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def del_partymember(discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"UPDATE member SET party_name = NULL WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def get_partyInfo(party_name):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT * FROM party WHERE party_name = '{party_name}'"
        cursor.execute(sql)
        rows = cursor.fetchone()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()
        return rows if len(rows) > 0 else None

def set_partydec(leader_id,dec):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"UPDATE party SET party_dec = '{dec}' WHERE discord_id='{leader_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()


def set_member(discord_id,discord_name,summoner_id):
    today = datetime.datetime.now()
    now = today.strftime('%Y-%m-%d %H:%M:%S')
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"INSERT INTO member (discord_id,discord_name,summoner_id,birthday) VALUES('{discord_id}','{discord_name}','{summoner_id}','{now}') ON DUPLICATE KEY UPDATE summoner_id = '{summoner_id}', discord_name = '{discord_name}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
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
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()
        return rows if len(rows) > 0 else None

def renew(discord_id,tier):
    today = datetime.datetime.now()
    now = today.strftime('%Y-%m-%d %H:%M:%S')
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        if tier == None:
            sql = f"UPDATE member SET renew='{now}',summoner_tier = NULL WHERE discord_id='{discord_id}'"
        else:
            sql = f"UPDATE member SET renew='{now}',summoner_tier='{tier}' WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def get_notice():
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT * FROM server"
        cursor.execute(sql)
        rows = cursor.fetchone()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()
        return rows if len(rows) > 0 else None


def set_notice(notice):
    today = datetime.datetime.now()
    now = today.strftime('%Y-%m-%d %H:%M:%S')
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"UPDATE server SET notice='{notice}', date='{now}' WHERE no = 1"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def get_teacher():
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT * FROM academy"
        cursor.execute(sql)
        rows = cursor.fetchall()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()
        return rows if len(rows) > 0 else None

def set_teacher(discord_id,discord_name,line,dec):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"INSERT INTO academy (discord_id,discord_name,teacher_line,teacher_dec) VALUES('{discord_id}','{discord_name}','{line}','{dec}') ON DUPLICATE KEY UPDATE teacher_line = '{line}', teacher_dec = '{dec}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def find_teacher(discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"SELECT teacher_id FROM member WHERE discord_id='{discord_id}' "
        cursor.execute(sql)
        rows = cursor.fetchone()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()
        return rows[0] if len(rows) > 0 else None

def del_teacher(discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"DELETE FROM academy WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def set_student(discord_id,teacher_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"UPDATE member set teacher_id='{teacher_id}' WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def del_student(discord_id):
    try:
        conn = open(db_id,db_pw)
        cursor = conn.cursor()
        sql = f"UPDATE member set teacher_id = NULL WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()


check=False
while check==False:
    db_id = "lolparty"
    db_pw = "rhqor01"
    check = check_connect()