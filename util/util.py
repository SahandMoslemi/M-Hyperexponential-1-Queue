from numpy import random

def exponential_random(scale = None):
    if scale:
        return random.exponential(scale = scale)

    return random.exponential()

def search(values, intended_value):
    indexes = [index for index, value in enumerate(values) if value == intended_value]

    return indexes
    