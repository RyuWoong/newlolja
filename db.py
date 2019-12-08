import pymysql,log
import myfunction as fc

get_info = fc.GET_KEY("info.txt")

def open(get_info):
    conn = pymysql.connect(
        host=get_info[0],
        port=3306,
        user=get_info[1],
        password=get_info[2],
        db='lolparty',
        charset='utf8'
        )
    return conn

def call_error(ex):
    raise ex

def check_exist(table,discord_id):
    try:
        conn = open(get_info)
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
        conn = open(get_info)
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
        conn = open(get_info)
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
        conn = open(get_info)
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
        conn = open(get_info)
        cursor = conn.cursor()
        sql = f"UPDATE streamer SET dec='{dec}' WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def get_party(discord_id):
    try:
        conn = open(get_info)
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
        conn = open(get_info)
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
        conn = open(get_info)
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
        conn = open(get_info)
        cursor = conn.cursor()
        sql = f"UPDATE member SET party is NULL WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def set_member(discord_id,discord_name,summoner_id):
    try:
        conn = open(get_info)
        cursor = conn.cursor()
        sql = f"INSERT INTO member (discord_id,discord_name,summoner_id) VALUES('{discord_id}','{discord_name}','{summoner_id}') ON DUPLICATE KEY UPDATE summoner_id = VALUES('{summoner_id}')"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()

def get_member(discord_id):
    try:
        conn = open(get_info)
        cursor = conn.cursor()
        sql = f"SELECT * FROM member WHERE discord_id = '{discord_id}'"
        rows = cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        call_error(ex)
    finally:
        cursor.close()
        conn.close()
        return rows if len(rows) > 0 else None
