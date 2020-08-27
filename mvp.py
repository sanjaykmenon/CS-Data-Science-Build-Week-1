import numpy as np 
import matplotlib.pyplot as pyplot

def most_found(array):
    list_of_words = []
    for i in range(len(array)):
        if array[i] not in list_of_words:
            list_of_words.append(array[i])

    most_counted = ''
    n_of_most_counted = None 

    