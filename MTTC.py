from StableMarriage import MarriageModel
from time import process_time
import random
import itertools


avg_time_dct = {}
avg_round_dct = {}

for i in range(2,22,2):
    time_lst = []
    round_lst = []
    
    for j in range(10):
        guys = list(range(int(i/2)))
        gals = list(range(int(i/2),i))
        
        guyprefers = {}
        galprefers = {}
        
         
        for guy in guys:
            guyprefers[guy] = list(random.choice(list(itertools.permutations(gals))))
        
        for gal in gals:
            galprefers[gal] = list(random.choice(list(itertools.permutations(guys))))
        
        model = MarriageModel(guyprefers, galprefers)
    
        t = process_time()
        round_lst.append(model.random_ttc()[1])
        elapsed_time = process_time() - t
        time_lst.append(elapsed_time)
    
    avg_time_dct[i] = sum(time_lst)/len(time_lst)
    avg_round_dct[i] = sum(round_lst)/len(round_lst)
    
print(avg_time_dct)
print(avg_round_dct)