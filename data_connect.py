import pymysql.cursors
# 连接数据库
def sql_action(action,formulas=None):
    connect = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='111111',
    db='calculate',
    charset='utf8'
    )
    cursor = connect.cursor()
    if action == 1:
    #1为查询数据库操作
        sql = "SELECT * FROM formula"
        cursor.execute(sql)
        results = [row[0] for row in cursor.fetchall()]
        return results
    elif action == 2:
    #2为添加数据
        sql = "INSERT INTO formula VALUES('%s')"
        data = formulas
        cursor.execute(sql % data)
        connect.commit()
        return 2
    elif action ==3:
        sql = "DELETE FROM formula WHERE formula = '%s' "
        data = formulas
        cursor.execute(sql % data)
        connect.commit()
        return  3
    else :
        print('error')
        return 'error'