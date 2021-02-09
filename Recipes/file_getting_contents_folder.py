Используйте функцию os.listdir() для получения списка файлов в каталоге:
import os
names = os.listdir('somedir')
Вы получите «сырой» список содержимого каталога, включающий все файлы, 
подкаталоги, символические ссылки и т. п. Если вам нужно как-то отфильтровать 
эти данные, используйте генератор списков вместе с  различными функциями 
библиотеки os.path(). Например:
import os.path
# Получить все обычные файлы
names = [name for name in os.listdir('somedir')
 if os.path.isfile(os.path.join('somedir', name))]
# Получить все каталоги
dirnames = [name for name in os.listdir('somedir')
 if os.path.isdir(os.path.join('somedir', name))]
Строковые методы startswith() и endswith() также могут быть полезны для фильт­
рации содержимого каталога. Например:
pyfiles = [name for name in os.listdir('somedir')
 if name.endswith('.py')]
Для поиска совпадений по имени файла вы можете использовать модули glob
или fnmatch. Например:
import glob
pyfiles = glob.glob('somedir/*.py')
from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
 if fnmatch(name, '*.py')]


# Пример получения содержимого каталога
import os
import os.path
import glob
pyfiles = glob.glob('*.py')
# Получение размеров файлов и дат модификации
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
 for name in pyfiles]
for name, size, mtime in name_sz_date:
 print(name, size, mtime)
# Альтернатива: получение метаданных
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
 print(name, meta.st_size, meta.st_mtime)
