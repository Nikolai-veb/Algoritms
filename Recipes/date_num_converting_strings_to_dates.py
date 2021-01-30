from datetime import datetime
>>> text = '2012-09-20'
>>> y = datetime.strptime(text, '%Y-%m-%d')
>>> z = datetime.now()
>>> diff = z - y
>>> diff
datetime.timedelta(3, 77824, 177393)

Предположим, что ваша программа генерирует объект datetime, но вам нужно 
создать из него красивую, понятную людям дату, чтобы потом вставить ее в заголовок автоматически создаваемого письма или отчета:
>>> z
datetime.datetime(2012, 9, 23, 21, 37, 4, 177393)
>>> nice_z = datetime.strftime(z, '%A %B %d, %Y')
>>> nice_z
'Sunday September 23, 2012'

Например, если вы знаете, что даты представлены в формате «YYYY-MM-DD», то можете написать такую функцию:
from datetime import datetime
def parse_ymd(s):
 year_s, mon_s, day_s = s.split('-')
 return datetime(int(year_s), int(mon_s), int(day_s))
При тестировании эта функции оказалась более чем в  7 раз быстрее метода datetime.strptime(). 
Это стоит держать в  голове, если вы обрабатываете большие объемы данных с датами.
