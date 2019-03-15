# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:13:45 2018

@author: Raunak
"""

import math
import numpy as np, numpy.random
from itertools import combinations
import random

base = 50000
tax_free = 6100

population_size =100

def fitness_function(withdrawals):

    total_profit = 0
    interests = [0.50 ,0.635 ,0.782]

    for each, int in zip(withdrawals,interests):

        if each*int >tax_free:
                total_profit  += (each*int-tax_free)*0.7 +tax_free
        else:
            total_profit += each*int


    if math.ceil(sum(withdrawals))!=base:
        total_profit = 0
    
    return total_profit+0.04*total_profit

past_profit = 0
new_profit = 1

population = np.random.dirichlet(np.ones(3),size=population_size)*base
population_fitness = np.zeros(population_size)
past_max = 0
new_max = 1

def selection(fitness ,popula):
    global population_size

    f = np.argsort(fitness)

    uf = f[math.ceil(population_size/2):population_size]
    y = [x for x in combinations(f[0:math.ceil(population_size/2)],2)]

    for each in uf:
         selection  = np.random.choice( range(0,len(y)),1)

         l= np.append(population[y[selection[0]][0]] , population[y[selection[0]][1]])

         crossover = np.random.choice(l , 2)
         while sum(crossover)>base:
             crossover = np.random.choice(l , 2)

         popula[each] = np.append(crossover , [ base - sum(crossover)])
    return popula


past_max_wd = []
while 1 :
    for i in range(0 , len(population)):
        population_fitness[i] = fitness_function(population[i])

    population = selection(population_fitness  , population)
    new_max = np.max(population_fitness)
    print(past_max , past_max_wd , sum(past_max_wd))
    if past_max >= new_max:
        break;
    else:
        past_max = new_max
        past_max_wd = population[np.argmax(population_fitness)]
