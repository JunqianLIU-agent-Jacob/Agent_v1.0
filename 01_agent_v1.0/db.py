import pymysql

def get_db_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="你自己的密码",
        database="自己的库名",
        charset="utf8mb4"
    )
def save_chat(user_input, ai_response):
    conn = get_db_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO chat_history(user_input, ai_response) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (user_input, ai_response))
        conn.commit()
        print('保存成功')
    except Exception as e:
        print(f'错误原因:{e}')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def get_history():
    conn = get_db_conn()
    cursor = conn.cursor()
    sql = "SELECT * FROM chat_history"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except Exception as e:
        print(f'错误是{e}')
    finally:
        cursor.close()
        conn.close()

