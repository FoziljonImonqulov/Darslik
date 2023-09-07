import time
import redis
import psycopg2
from psycopg2.extras import DictCursor

con = redis.Redis(decode_responses=True)


class PG:
    con = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1',
        host='localhost',
        port='5432',
        cursor_factory=DictCursor
    )

    cur = con.cursor()

    def login_check(self, username, password):
        query = """select * from users where username= %s and password=%s"""
        params = username, password
        self.cur.execute(query, params)
        user = self.cur.fetchone()
        print(user)
        return user if user else None


def login():
    username = input("username: ")
    password = input("password: ")

    start = time.time()
    if not con.hgetall(username):
        user = PG().login_check(username, password)
        print("Use postgresql")
        if not user:
            print("Not found")
        con.hset(username, mapping=user)
    else:
        print("Use cache")
        user = con.hgetall(username)
    if user:
        print("saving login")
    else:
        print("login failed")
    print(time.time() - start)


login()
