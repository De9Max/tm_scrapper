import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS articles
                  (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  article_name TEXT NOT NULL,
                  article_url TEXT NOT NULL, 
                  telegram_sent BOOL DEFAULT FALSE,
                  added_time DATETIME DEFAULT CURRENT_TIMESTAMP
                  )
               """)


def execute_and_commit(sql, parameters=()):
    """Выполняем sql команду и сохраняем изменения"""
    try:
        print(sql)
        cursor.execute(sql, parameters)
        conn.commit()
    except Exception as e:
        print(e)


def execute_and_fetchall(sql, parameters=()):
    """Выполняем sql команду и возвращаем результат"""
    try:
        cursor.execute(sql, parameters)
        ret = cursor.fetchall()
        return ret
    except Exception as e:
        print(e)


def add_article(name, url):
    execute_and_commit("INSERT OR REPLACE into articles (article_name,article_url) values (?,?);", (name, url,))


def check_exist_article(name):
    result = execute_and_fetchall("SELECT * from articles WHERE article_name = ?;", (name,))
    if result:
        return True
    else:
        return False
