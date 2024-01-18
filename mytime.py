import time

t = time.time()
print(t)

print(time.localtime().tm_year)

print(time.mktime((2009, 2, 17, 17, 3, 38, 1, 48, 0)))

print(time.strptime("2022-01-01","%Y-%m-%d"))

#days in week
days = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5:"Sat", 6: "Sun"}
lt = time.localtime()
print(days[lt.tm_wday])