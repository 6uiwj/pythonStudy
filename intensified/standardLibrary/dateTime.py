import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023,4,5)
diff = day2 - day1
print(diff.days)

#요일(월요일0 ~ 일요일6)
day= datetime.date(2021, 12,14)
print(day.weekday())

#월요일1 ~ 일요일7로 출력하기
print(day.isoweekday())

