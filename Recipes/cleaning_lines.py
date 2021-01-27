s = 'pýtĥöñ\fis\tawesome\r\n

Первый шаг – удалить пробел. Сделаем небольшую таблицу перевода и задействуем translate():

remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None # Удален
}

a = s.translate(remap) #'pýtĥöñ is awesome\n'

Как вы можете увидеть, символы пробелов, такие как \t и \f , были приведены к единой форме. Символ возврата каретки \r был удален.
Вы можете продолжить идею и создать намного более крупные таблицы перевода. Например, давайте удалим все комбинирующиеся символы:

import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
... if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a) #'pýtĥöñ is awesome\n'

b.translate(cmb_chrs) #'python is awesome\n'

Еще один пример – таблица перевода, которая отображает все десятичные цифры Unicode на их эквиваленты в ASCII:

digitmap = { c: ord('0') + unicodedata.digit(chr(c))
... for c in range(sys.maxunicode)
... if unicodedata.category(chr(c)) == 'Nd' }
len(digitmap) #460
# Арабские цифры
x = '\u0661\u0662\u0663
 x.translate(digitmap) #'123'

Еще один прием для чистки текста использует функции кодирования и декодирования ввода-вывода. Идея состоит в выполнении некоторой первичной очистки
текста, а затем пропускании его через encode() и decode() для срезания символов или изменения. Например:

>>> a
'pýtĥöñ is awesome\n'
>>> b = unicodedata.normalize('NFD', a)
>>> b.encode('ascii', 'ignore').decode('ascii')
'python is awesome\n'



