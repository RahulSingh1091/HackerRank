import math
import os
import random
import re
import sys

input_num = int(raw_input())
if (input_num % 2 == 0
    and input_num >=2
    and input_num <=5):
    print('Not Weird')
elif (input_num % 2 == 0
    and input_num >20):
    print('Not Weird')
else:
    print('Weird')
