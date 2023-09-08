"""
Celery bu funksiyalarni tezroq ishlashini taminlab beradi.
yani bir faylda biron bir task bajarilayotganda boshqa tasklar ham malum bir vatqda bajaralishi kerak bols u funktsiyalar
boshqa faylad ishlatilib qoyiladi yani misol uchun 3 ta funksiya mavuz har biri ishga tushishi uchun 30 secund dan vaqt ketadi
bu holatda 90 secund vatdan yutqzamiz celery esa buni ossonlashtradi u hamma funktsiyani 30 second ichida ishlatib yuboradi,
odatda celery ni multithreading yoki multiproccesing ga oxshatish mumkun

"""