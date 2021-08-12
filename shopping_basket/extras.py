import datetime
from datetime import date
import random
import string


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().hour) + str(
                                                                                        datetime.datetime.now().minute)
    rand_str = "".join([random.choice(string.digits) for _ in range(4)])
    return '{}{}'.format(date_str, rand_str)
