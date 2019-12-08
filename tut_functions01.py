'''
EXERCISE
How functions declare variables when the first time a function is read.
Be careful because it sets the variable once.

Below is how to fix this, taken from Corey Shafer's video,
5 Common Python Mistakes and How to Fix Them
'''

import time
from datetime import datetime

#V1 here the time is set once when the function is read, and it does not update.
# def display_time(time=datetime.now()):
#     print(time.strftime('%B %d, %Y %H:%M:%S'))

#V2 This version works because 'time' isn't stuck at the first time it runs.
def display_time(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime('%B %d, %Y %H:%M:%S'))

display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
time.sleep(1)
