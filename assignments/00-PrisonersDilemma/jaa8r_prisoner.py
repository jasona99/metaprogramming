class BillyBob:
    #An attempt to win.
    total_mean_bb = 0.0
    total_runs_bb = 0.0
    def __init__(self, both_confess_sentence,
                 none_confess_sentence, self_confess_sentence, other_confess_sentence):
        #Mainly just need these to check if angered...
        self.mean_small = both_confess_sentence
        self.mean_big = other_confess_sentence
        self.ideal = none_confess_sentence
        self.kind_big = self_confess_sentence
        if BillyBob.total_runs_bb == 100:
            BillyBob.total_runs_bb = 0
            BillyBob.total_mean_bb = 0

    def decide(self):

        if BillyBob.total_runs_bb >= 2:
            #Give 'em a chance'
            mean_score = BillyBob.total_mean_bb/BillyBob.total_runs_bb
            print("Meanness:", mean_score)
            if mean_score >= .1 and BillyBob.total_runs_bb == 100:
                #If scorned...
                return True
            else:
                return False
        else:
            return False

    def sentence(self, years):
        BillyBob.total_runs_bb += 1.0
        if years == self.mean_small or years == self.mean_big:
            BillyBob.total_mean_bb += 1
        return 0

import random
class BillyJoel:
        #How does it stack up against random (mostly above threshold)???
        def __init__(self, both_confess_sentence,
                     none_confess_sentence, self_confess_sentence, other_confess_sentence):
            return None
        def decide(self):
            return random.choice([True, True, True, True, False])
        def sentence(self, years):
            return 0

class BillyJoel2:
        #How does it stack up against random, mostly nice (below threshold)???
        def __init__(self, both_confess_sentence,
                     none_confess_sentence, self_confess_sentence, other_confess_sentence):
            return None
        def decide(self):
            return random.choice([True, False, False, False, False, False, False, False, False, False, False])
        def sentence(self, years):
            return 0
