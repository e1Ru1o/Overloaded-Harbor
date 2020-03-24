from math import log
from random import random
from collections import namedtuple

Event = namedtuple("Event", "time callback details")

def bublle_sort_last(data):
    '''
    Apply bublle sort algorithm
    to the last element of <data>
    '''
    for i in range(len(data) - 2, -1, -1):
        if data[i] > data[i + 1]:
            break
        data[i], data[i + 1] = data[i + 1], data[i]

def get_category(data):
    '''
    Return a category index given
    a <data> set representing the
    ocurrence probability of each one
    '''
    u = random()
    interval = 0
    for i, v in enumerate(data):
        interval += v
        if u <= interval:
            return i

def exponential(lamb):
    '''
    Simulate an exponential
    distribution of parameter <lamb>
    '''
    return -log(random()) / lamb

def normal(u, o):
    '''
    Simulate a normal
    distribution of mean <u>
    and variance <o>
    '''
    while(True):
        y1 = exponential(1)
        y2 = exponential(1)
        v = y2 - (((y1 - 1) ** 2) / 2)
        if v > 0:
            return v

def mean(data):
    '''
    Calculate the mean of <data>
    '''
    return sum(data) / len(data)

