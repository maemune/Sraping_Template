# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True

import time
import datetime
import init

def main ():
    driver = init.option ()
    driver.get ('chrome://version/')

#------------------------------
def cur_time ():#Now Time
    date = datetime.datetime.now ()
    txt = date.strftime ("%H:%M")
    print (txt)

def pause ():
    input ('Please press ENTER >> ')
#----------------------------
if __name__ == '__main__':
    start_time = time.time ()
    main ()
    end_time = time.time ()
    print ()#Line Feed
    print ('complete >> {}sec'.format (round (end_time - start_time, 1)))
    init.quit ()
