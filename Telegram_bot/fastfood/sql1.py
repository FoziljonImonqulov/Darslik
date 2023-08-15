from dataclasses import dataclass

import psycopg2

con = psycopg2.connect(
    database='postgres',
    user='postgres',
    host='localhost',
    port=5432,
    password='11'
)
cur = con.cursor()


@dataclass
class Tbot:
    user_id: int = None
    is_bot: str = None,
    first_name: str = None,
    last_name: str = None,
    username: str = None,
    language_code: str = None,
    phone_number: str = None

    def insert_data(self):
        query = """
        insert into users(user_id,is_bot,first_name,last_name,username,language_code)
        values (%s,%s,%s,%s,%s,%s)
         """
        parametrs = (self.user_id, self.is_bot, self.first_name, self.last_name, self.username, self.language_code)

        cur.execute(query, parametrs)
        con.commit()

    def check_is_available(self):
        query = """
            select * from users where user_id = %s
        """
        param = (self.user_id,)
        cur.execute(query, param)
        if cur.fetchall():
            return True
        return False

    def update_data(self):
        query = """
            update users set phone_number=%s,first_name=%s where user_id = %s
        """
        params = (self.phone_number, self.first_name, self.user_id)
        cur.execute(query, params)
        con.commit()

    def update_name(self):
        query = """
            update users set first_name=%s where user_id = %s
        """
        params = (self.first_name,self.user_id)
        cur.execute(query, params)
        con.commit()

    def update_number(self):
        query = """
            update users set phone_number=%s where user_id = %s
        """
        params = (self.phone_number,self.user_id)
        cur.execute(query, params)
        con.commit()

