Предположим, что у вас есть огромный каталог с файлами логов, который вы хотите обработать:

foo/
 access-log-012007.gz
 access-log-022007.gz
 access-log-032007.gz
 ...
 access-log-012008
bar/
 access-log-092007.bz2
 ...
 access-log-022008
Предположим, каждый файл содержит такие строки данных:
124.115.6.12 - - [10/Jul/2012:00:18:50 -0500] "GET /robots.txt ..." 200 71
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /ply/ ..." 200 11875
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /favicon.ico ..." 404 369
61.135.216.105 - - [10/Jul/2012:00:20:04 -0500] "GET /blog/atom.xml ..." 304 -
...
Чтобы обработать эти файлы, вы могли бы создать коллекцию небольших гене-
раторов, которые будут выполнять специфические замкнутые в себе задачи:
import os
import fnmatch
import gzip
import bz2
import re
def gen_find(filepat, top):
 '''
 Находит все имена файлов в дереве каталогов,
 которые совпадают с шаблоном маски оболочки
 '''
 for path, dirlist, filelist in os.walk(top):
 for name in fnmatch.filter(filelist, filepat):
 yield os.path.join(path,name)
def gen_opener(filenames):
 '''
 Открывает последовательность имен файлов, которая
 раз за разом производит файловый объект.
 Файл закрывается сразу же после перехода
 к следующему шагу итерации.
 '''
 for filename in filenames:
 if filename.endswith('.gz'):
 f = gzip.open(filename, 'rt')
 elif filename.endswith('.bz2'):
 f = bz2.open(filename, 'rt')
 else:
 f = open(filename, 'rt')
 yield f
 f.close()

 def gen_concatenate(iterators):
 '''
 Объединяет цепочкой последовательность
 итераторов в одну последовательность.
 '''
 for it in iterators:
 yield from it
def gen_grep(pattern, lines):
 '''
 Ищет шаблон регулярного выражения
 в последовательности строк
 '''
 pat = re.compile(pattern)
 for line in lines:
 if pat.search(line):
 yield line
Теперь вы можете легко совместить эти функции для создания обрабатываю-
щего канала. Например, чтобы найти все файлы логов, которые содержат слово
python, вы можете поступить так:
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
 print(line)
Если вы хотите еще расширить функциональность канала, то можете скарм-
ливать данные выражениям-генераторам. Например, эта версия находит коли­
чество переданных байтов и подсчитывает общую сумму:
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
bytecolumn = (line.rsplit(None,1)[1] for line in pylines)
bytes = (int(x) for x in bytecolumn if x != '-')
print('Total', sum(bytes))
