def executeSQL(sql, param):
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1111',
        database='lvzhoureading',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = db.cursor()
    cursor.execute(sql, param)
    res = cursor.fetchall()
    db.commit()
    db.close()
    return res

import pymysql
