import time
from datetime import datetime
from datetime import timedelta

def add8(t):
    date_time = datetime.fromtimestamp(t)
    eH = timedelta(hours=8)
    pay_time = date_time + eH
    ss = time.mktime(pay_time.timetuple())
    print ss
    return ss
d = 1513235193
add8(d)