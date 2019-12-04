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
    else:
        conn.close()
        return rows

def set_streamer(info):
    try:
        cursor = conn.cursor()
        sql = f"INSERT INTO streamer VALUES('{info[0]}','{info[1]}','{info[2]}','{info[3]}','{info[4]}')"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        log.logger.error(ex)
    else:
        conn.close()

def del_streamer(info):
    try:
        cursor = conn.cursor()
        sql = f"DELETE FROM streamer WHERE name={info}"
        cursor.execute(sql)
        conn.commit()
    except Exception as ex:
        log.logger.error(ex)
    else:
        conn.close()
