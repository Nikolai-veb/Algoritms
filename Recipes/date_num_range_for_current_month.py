Вот функция, которая принимает любой объект datetime и возвращает кортеж, 
содержащий первую дату месяца и начальную дату следующего месяца:

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
 if start_date is None:
 start_date = date.today().replace(day=1)
 _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
 end_date = start_date + timedelta(days=days_in_month)
 return (start_date, end_date)
Получив эти данные, очень просто пройти в цикле по диапазону дат:
>>> a_day = timedelta(days=1)
>>> first_day, last_day = get_month_range()
>>> while first_day < last_day:
... print(first_day)
... first_day += a_day

2012-08-01
2012-08-02
2012-08-03
2012-08-04
2012-08-05
2012-08-06
2012-08-07
2012-08-08
2012-08-09
#... и так далее...

В идеальном случае стоит создать функцию, которая будет работать как встро-
енная range(), но с датами. К счастью, есть чрезвычайно простой способ сделать
это с помощью генератора:
def date_range(start, stop, step):
 while start < stop:
 yield start
 start += step
Вот пример ее использования:
>>> for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1),
timedelta(hours=6)):
... print(d)
...
2012-09-01 00:00:00
2012-09-01 06:00:00
2012-09-01 12:00:00
2012-09-01 18:00:00
2012-09-02 00:00:00
2012-09-02 06:00:00
