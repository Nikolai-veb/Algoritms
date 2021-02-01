from collections import deque
class linehistory:
 def __init__(self, lines, histlen=3):
 self.lines = lines
 self.history = deque(maxlen=histlen)
 def __iter__(self):
 for lineno, line in enumerate(self.lines,1):
 self.history.append((lineno, line))
 yield line
 def clear(self):
 self.history.clear()
Вы можете обращаться с этим классом так же, как с обычным генератором. 
Однако, поскольку он создает экземпляр, вы можете обращаться к внутренним атрибутам, таким как history или метод clear(). 
Например:

with open('somefile.txt') as f:
 lines = linehistory(f)
 for line in lines:
 if 'python' in line:
 for lineno, hline in lines.history:
 print('{}:{}'.format(lineno, hline), end='')
