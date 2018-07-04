import math
import os
import random
import re
import sys

def get_total_cost_of_meal():
    meal_cost = float(input())
    tip_percentage = int(input())
    tax_percentahe = int(input())

    tip = meal_cost*tip_percentage/100
    tax = meal_cost*tax_percentahe/100
    total_cost=int(round(meal_cost+tip+tax))
    return str(total_cost)

print('The total meal cost is ' + get_total_cost_of_meal() + ' dollars.')
