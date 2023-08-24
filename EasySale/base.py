from dataclasses import dataclass

import psycopg2

con = psycopg2.connect(
    database='postgres',
    user='postgres',
    host='localhost',
    port=5432,
    password='1221'
)
cur = con.cursor()


@dataclass
class DB:
    user_id: int = None
    is_bot: str = None,
    first_name: str = None,
    last_name: str = None,
    username: str = None,
    language_code: str = None,
    phone_number: str = None

    def insert_data(self, user_id, is_bot, first_name, last_name, username, language_code):
        query = """
        insert into bot_user(user_id,is_bot,first_name,last_name,username,language_code)
        values (%s,%s,%s,%s,%s,%s)
         """
        parametrs = (user_id, is_bot, first_name, last_name, username, language_code)

        cur.execute(query, parametrs)
        con.commit()

    def check_is_available(self, user_id):
        query = """
            select * from bot_user where user_id = %s
        """
        param = (user_id,)
        cur.execute(query, param)
        if cur.fetchall():
            return True
        return False

    def update_data(self, phone_number,user_id):
        query = """
            update bot_user set phone_number=%s where user_id = %s
        """
        params = (phone_number, user_id)
        cur.execute(query, params)
        con.commit()
