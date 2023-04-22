# python-zip-break
python破解zip密码，包含了单线程破解和多线程破解等

## 需要字典的同志，可以在issue里留一下言，但是我更希望同志们可以找一下


## 暴力破解法，字典法
## zipbreak.py：暴力破解，单线层，暴力破解使用到多线程更好喔，按我的字符集来的话，单线程就更加久了，如果密码是四位，使用单线程一下午的时间就可以搞定啦
## zipbreakDict.py:字典破解，多线程，使用到itertools库
## zipbreakDictmul.py:字典破解，多线程，使用到multiprocessing库，创建线程池，让线程去争逐时间片，大大的减少读取字典时对内存的消耗，同时调度GPU共同使用
