import datetime

date_obj = datetime.datetime(2025 , 4, 5, 13, 45, 23)
date_string = date_obj.strftime("%d-%m-%Y %H:%M:%S")


year = date_obj.year
month = date_obj.month
day = date_obj.day
hour = date_obj.hour
minute = date_obj.minute
second = date_obj.second

print(year, month, day, hour, minute, second)
print(date_string)


# date_string_1 = "08-03-2022 15:45:00"
# date_obj = datetime.datetime.strptime(date_string_1, "%d-%m-%Y %H:%M:%S")
# print(date_obj)


# %a — аббревиатура дня недели (Sun, Mon, ...)
# %A — полное название дня недели (Sunday, Monday, ...)
# %w — день недели как число (0 — воскресенье, 6 — суббота)
# %d — день месяца (01–31)
# %b — аббревиатура месяца (Jan, Feb, ...)
# %B — полное название месяца (January, February, ...)
# %m — месяц как число (01–12)
# %y — год без столетия (00–99)
# %Y — год (четырехзначное число)
# %H — часы (00–23)
# %I — часы (01–12)
# %p — AM или PM
# %M — минуты (00–59)
# %S — секунды (00–59)
# %f — микросекунды (000000–999999)
# %z — смещение временной зоны UTC (+HHMM или -HHMM)
# %Z — название временной зоны
# %j — день года (001–366)
# %U — номер недели года (00–53), воскресенье — первый день недели
# %W — номер недели года (00–53), понедельник — первый день недели
# %c — локальная дата и время (например, Tue Aug 16 21:30:00 2022)
# %x — локальная дата (например, 08/16/22)
# %X — локальное время (например, 21:30:00)
# %%m — символ %