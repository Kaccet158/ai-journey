class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1] 

    def personal_best(self):
        return max(self.scores) 

    def personal_top_three(self):
        h = sorted(self.scores, reverse=True) 
        return h[:3] 




        
