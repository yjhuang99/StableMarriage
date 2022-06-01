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

guyprefers = {
    'abe': ['ari', 'bet', 'cat', 'dor'],
    'ben': ['bet', 'ari', 'dor', 'cat'],
    'chr': ['cat', 'dor', 'ari', 'bet'],
    'dav': ['dor', 'cat', 'bet', 'ari']
}

galprefers = {
    'ari': ['dav', 'chr', 'ben', 'abe'],
    'bet': ['chr', 'dav', 'abe', 'ben'],
    'cat': ['ben', 'abe', 'dav', 'chr'],
    'dor': ['abe', 'ben', 'chr', 'dav']
}


model = MarriageModel(guyprefers, galprefers)
print(model.random_path_to_stability(print_rounds = True))
print(model.Deferred_Acceptance(print_rounds = True))
print(model.enumeration_stability())
print(model.random_sd())
print(model.random_ttc())





