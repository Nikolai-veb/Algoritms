from operator import itemgetter
from itertools import groupby

rows = [
 {'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Итерируем в группах
for date, items in groupby(rows, key=itemgetter('date')):
 print(date)
 for i in items:
 print(' ', i)

 """
 Если ваша цель – просто сгруппировать данные вместе в  крупную структуру
данных с произвольным доступом, то вам больше поможет функция defaultdict(),
которая создает «мультисловарь», как было описано в рецепте 1.6. Например:
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
 rows_by_date[row['date']].append(row)
Это позволяет легко получить доступ к записям для каждой даты:
>>> for r in rows_by_date['07/01/2012']:
... print(r)
 """
