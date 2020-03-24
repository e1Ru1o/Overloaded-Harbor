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
    return 0

def exponential(lamb):
    '''
    Simulate an exponential
    distribution of parameter <lamb>
    '''
    pass

def normal(u, o):
    '''
    Simulate a normal
    distribution of mean <u>
    and variance <o>
    '''
    pass

def mean(data):
    '''
    Calculate the mean of <data>
    '''
    return sum(data) / len(data)

