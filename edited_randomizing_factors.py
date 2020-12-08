import random
from random import randint

def get_random_total_num_voters():
    min_num_people_who_voted = 1_000
    max_num_people_who_voted = 10_000
    random.randint(1,17)
    value = randint(min_num_people_who_voted, max_num_people_who_voted)
    return value

def get_random_number(population):
    votes = []
    min_value_possible = 0
    max_value_possible = 4

    prcent_factor = 0.95
    majority = int(population * prcent_factor)
    minority = population - majority
    historicly_accurate_majority(population)
    historicly_accurate_minority(population)

def get_historicly_accurate_number(population):
    total_votes = []
    total_votes = historicly_accurate_majority(population) + historicly_accurate_minority(population)

    return total_votes

def historicly_accurate_majority(population):
    votes = []
    prcent_factor = 0.95
    majority = int(population * prcent_factor)
    min_possible_value = 0
    max_possible_value = 1

    for _ in range(0, int(majority)):
        vote = randint(min_possible_value, max_possible_value)
        votes.append(vote)

    return votes

def historicly_accurate_minority(population):
    votes = []
    prcent_factor = 0.95
    majority = int(population * prcent_factor)
    minority = population - majority
    min_possible_value = 2
    max_possible_value = 4

    for _ in range(0, int(minority)):
        vote = randint(min_possible_value, max_possible_value)
        votes.append(vote)
    return votes