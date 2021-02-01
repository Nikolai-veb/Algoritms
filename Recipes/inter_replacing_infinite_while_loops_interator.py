Вполне обычный код для программ, работающих с вводом-выводом:
CHUNKSIZE = 8192
def reader(s):
 while True:
 data = s.recv(CHUNKSIZE)
 if data == b'':
 break
 process_data(data)
Такой код часто можно заменить использованием iter(), как показано ниже:
def reader(s):
 for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
 process_data(data)
Если вы сомневаетесь, будет ли это работать, то можете попробовать похожий 
пример для обработки файлов:
>>> import sys
>>> f = open('/etc/passwd')
>>> for chunk in iter(lambda: f.read(10), ''):
... n = sys.stdout.write(chunk)
...
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
..
