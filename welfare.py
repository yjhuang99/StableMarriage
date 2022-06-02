from StableMarriage import MarriageModel
import random
import itertools

guyprefers = {
    'abe': ['abi', 'bea', 'cat', 'dee'],
    'bob': ['bea', 'abi', 'dee', 'cat'],
    'col': ['cat', 'dee', 'abi', 'bea'],
    'dan': ['dee', 'cat', 'bea', 'abi']
}

galprefers = {
    'abi': ['dan', 'col', 'bob', 'abe'],
    'bea': ['col', 'dan', 'abe', 'bob'],
    'cat': ['bob', 'abe', 'dan', 'col'],
    'dee': ['abe', 'bob', 'col', 'dan']
}


guys = ['abe', 'ben', 'chr', 'dav', 'eli', 'fre', 'gar', 'har']
gals = ['ari', 'bet', 'cat', 'dor', 'emi', 'fan', 'gin', 'her']

guyprefers = {}
galprefers = {}

 
for guy in guys:
    guyprefers[guy] = list(random.choice(list(itertools.permutations(gals))))

    
for gal in gals:
    galprefers[gal] = list(random.choice(list(itertools.permutations(guys))))
    
print(galprefers,guyprefers)

welfare_lst = []
first_priority = 0 
for i in range(10):
    guys = ['abe', 'ben', 'chr', 'dav', 'eli', 'fre', 'gar', 'har']
    gals = ['ari', 'bet', 'cat', 'dor', 'emi', 'fan', 'gin', 'her']
    
    guyprefers = {}
    galprefers = {}
    
     
    for guy in guys:
        guyprefers[guy] = list(random.choice(list(itertools.permutations(gals))))
    
        
    for gal in gals:
        galprefers[gal] = list(random.choice(list(itertools.permutations(guys))))
    
    model = MarriageModel(guyprefers, galprefers)
    
    welfare = 0
    for key, value in model.random_path_to_stability().items():
        welfare += guyprefers[key].index(value)
        welfare += galprefers[value].index(key)
        if guyprefers[key].index(value) == 0 or galprefers[value].index(key) == 0:
            first_priority += 1
    
    welfare_lst.append(welfare)

avgwelfare = sum(welfare_lst)/len(welfare_lst)

print(avgwelfare, first_priority/10)
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
welfare_lst = []
first_priority = 0 
for i in range(10):    
    guys = ['abe', 'ben', 'chr', 'dav', 'eli', 'fre', 'gar', 'har']
    gals = ['ari', 'bet', 'cat', 'dor', 'emi', 'fan', 'gin', 'her']
    
    guyprefers = {}
    galprefers = {}
    
     
    for guy in guys:
        guyprefers[guy] = list(random.choice(list(itertools.permutations(gals))))
    
        
    for gal in gals:
        galprefers[gal] = list(random.choice(list(itertools.permutations(guys))))
    
    model = MarriageModel(guyprefers, galprefers)
    
    welfare = 0
    for key, value in model.Deferred_Acceptance()[0].items():
        welfare += guyprefers[key].index(value)
        welfare += galprefers[value].index(key)
        if guyprefers[key].index(value) == 0 or galprefers[value].index(key) == 0:
            first_priority += 1
            
    welfare_lst.append(welfare)

avgwelfare = sum(welfare_lst)/len(welfare_lst)

print(avgwelfare, first_priority/10)

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
welfare_lst = []
first_priority = 0 
for i in range(10): 
    guys = ['abe', 'ben', 'chr', 'dav', 'eli', 'fre', 'gar', 'har']
    gals = ['ari', 'bet', 'cat', 'dor', 'emi', 'fan', 'gin', 'her']
    
    guyprefers = {}
    galprefers = {}
    
     
    for guy in guys:
        guyprefers[guy] = list(random.choice(list(itertools.permutations(gals))))
    
        
    for gal in gals:
        galprefers[gal] = list(random.choice(list(itertools.permutations(guys))))

    model = MarriageModel(guyprefers, galprefers)

    welfare = 0
    for key, value in model.enumeration_stability()[0].items():
        welfare += guyprefers[key].index(value)
        welfare += galprefers[value].index(key)
        if guyprefers[key].index(value) == 0 or galprefers[value].index(key) == 0:
            first_priority += 1
            
    welfare_lst.append(welfare)

avgwelfare = sum(welfare_lst)/len(welfare_lst)

print(avgwelfare, first_priority/10)
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
welfare_lst = []
first_priority = 0 
for i in range(10): 
    guys = ['abe', 'ben', 'chr', 'dav', 'eli', 'fre', 'gar', 'har']
    gals = ['ari', 'bet', 'cat', 'dor', 'emi', 'fan', 'gin', 'her']
    
    guyprefers = {}
    galprefers = {}
    
     
    for guy in guys:
        guyprefers[guy] = list(random.choice(list(itertools.permutations(gals))))
    
    for gal in gals:
        galprefers[gal] = list(random.choice(list(itertools.permutations(guys))))

    model = MarriageModel(guyprefers, galprefers)
    guyprefers_copy = guyprefers.copy()
    galprefers_copy = galprefers.copy()
    
    dct = model.random_sd()[0]
    welfare = 0
    for key, value in dct.items():
        welfare += guyprefers_copy[key].index(value)
        welfare += galprefers_copy[value].index(key)
        if guyprefers_copy[key].index(value) == 0 or galprefers_copy[value].index(key) == 0:
            first_priority += 1
            
    welfare_lst.append(welfare)

avgwelfare = sum(welfare_lst)/len(welfare_lst)

print(avgwelfare, first_priority/10)
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
welfare_lst = []
first_priority = 0 
for i in range(10): 
    guys = ['abe', 'ben', 'chr', 'dav', 'eli', 'fre', 'gar', 'har']
    gals = ['ari', 'bet', 'cat', 'dor', 'emi', 'fan', 'gin', 'her']
    
    guyprefers = {}
    galprefers = {}
    
     
    for guy in guys:
        guyprefers[guy] = list(random.choice(list(itertools.permutations(gals))))
    
    for gal in gals:
        galprefers[gal] = list(random.choice(list(itertools.permutations(guys))))

    model = MarriageModel(guyprefers, galprefers)
    guyprefers_copy = guyprefers.copy()
    galprefers_copy = galprefers.copy()
    
    dct = model.random_ttc()[0]
    welfare = 0
    for key, value in dct.items():
        welfare += guyprefers_copy[key].index(value)
        welfare += galprefers_copy[value].index(key)
        if guyprefers_copy[key].index(value) == 0 or galprefers_copy[value].index(key) == 0:
            first_priority += 1
            
    welfare_lst.append(welfare)

avgwelfare = sum(welfare_lst)/len(welfare_lst)

print(avgwelfare, first_priority/10)

