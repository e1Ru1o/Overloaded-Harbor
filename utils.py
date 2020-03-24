from math import log
from random import random
from collections import namedtuple

Event = namedtuple("Event", "time callback details")

def get_category(data):
    '''
    Return a category index given
    a <data> set representing the
    ocurrence probability of each one
    '''
    pass

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

