import pymysql,log
import myfunction as fc

get_info = fc.GET_KEY("info.txt")

conn = pymysql.connect(
    host=get_info[0],
    port=3306,
    user=get_info[1],
    password=get_info[2],
    db='lolparty',
    charset='utf8'
    )

def get_streamer():
    try:
        cursor = conn.cursor()
        sql = f"SELECT * FROM streamer"
        cursor.execute(sql)
        rows = cursor.fetchall()
    except Exception as ex:
        log.logger.error(ex)
    finally:
        cursor.close()
        conn.close()
        return rows if len(rows) > 0 else None
            

def set_streamer(info):
    try:
        cursor = conn.cursor()
        sql = f"INSERT INTO streamer VALUES('{info[0]}','{info[1]}','{info[2]}','{info[3]}','{info[4]}')"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        log.logger.error(ex)
    finally:
        cursor.close()
        conn.close()

def del_streamer(name):
    try:
        cursor = conn.cursor()
        sql = f"DELETE FROM streamer WHERE name='{name}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        log.logger.error(ex)
    finally:
        cursor.close()
        conn.close()

def up_streamer(discord_id,dec):
    try:
        cursor = conn.cursor()
        sql = f"UPDATE streamer SET dec='{dec}' WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        log.logger.error(ex)
    finally:
        cursor.close()
        conn.close()

def get_party(discord_id):
    try:
        cursor = conn.cursor()
        sql = f"SELECT party_name FROM member WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        rows = cursor.fetchone()
    except Exception as ex:
        log.logger.error(ex)
    finally:
        cursor.close()
        conn.close()
        return rows[0] if len(rows) > 0 else None


def set_party(name,dec,leader_id,leader_name):
    try:
        cursor = conn.cursor()
        sql = f"INSERT INTO party(name,dec,leader_id,leader_name) VALUES('{name}','{dec}','{leader_id}','{leader_name}')"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        log.logger.error(ex)
    finally:
        cursor.close()
        conn.close()
        set_partymemeber(name,leader_id)

def set_partymemeber(party_name,discord_id):
    try:
        cursor = conn.cursor()
        sql = f"UPDATE member SET party='{party_name}' WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        log.logger.error(ex)
    finally:
        cursor.close()
        conn.close()

def del_partymember(discord_id):
    try:
        cursor = conn.cursor()
        sql = f"UPDATE member SET party is NULL WHERE discord_id='{discord_id}'"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        log.logger.error(ex)
    finally:
        cursor.close()
        conn.close()

def set_member(discord_id,summoner_id):
    try:
        cursor = conn.cursor()
        sql = f"INSERT INTO member (discord_id, summoner_id) VALUES('{discord_id}','{summoner_id}')"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        log.logger.error(ex)
    finally:
        cursor.close()
        conn.close()