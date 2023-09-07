import time

from new_task import send_email

email_list = [
    "turgunovjamshid32@gmail.com",
    "nurullomahmud@gmail.com",
    "diyorbekdilmurodov1@gmail.com",
    "ahmatovdilshodbek@gmail.com",
    "nabiyevadilnavoz736@gmail.com",
    "khayrullo.devs@gmail.com",
    "mohirmirahmadov@gmail.com",
    "isomiddinwtu@gmail.com",
    "samidilloravshanov13@gmail.com",
    "1006695@mail.ru",
    "suratovdoniyor@gmail.com",
]

start = time.time()
for i in email_list:
    send_email.delay(i)

print(time.time() - start)
