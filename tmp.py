class MyError(Exception):
    def __init__(self, text):
        self.text = text


def exx ():
    raise MyError ('q[wfkwq')
    print('qfw')

try:
    exx()
    print("qfw")
except MyError as h:
    print(h)
    