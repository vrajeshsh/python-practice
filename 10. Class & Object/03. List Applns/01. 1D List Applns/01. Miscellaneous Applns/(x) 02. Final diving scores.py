import os
os.system("cls")

class DivingScores():
    def __init__(self, n):
        self.scores = []
        self.num = n

    def accept(self):
        for i in range(self.num):
            print("Enter score of judge #",i+1,": ",sep='', end='')
            self.scores.append(int(input()))

    def display(self):
        print("\nScores obtained: ",self.scores,"\n", sep='')
    
    def permissible_scores(self):
        p_scores = DivingScores(n - 2)
        ''' Oh GOD!!! How dare you delete scores of the candidate!! As it is a class's member variables
        are NEVER TO BE MODIFIED!!! '''
        # Redo the below code WITHOUT REMOVAL of any score from the list.
        self.scores.remove(max(self.scores))
        self.scores.remove(min(self.scores))
        p_scores.scores = self.scores
        print("Permissible scores of the diver: ", p_scores.scores, sep='')
    # The below code will automatically change as per the changes that would be made in the above functions. 
    def final_score(self):
        print("Diver's final score: ",round(sum(p_scores.scores)/(self.num-2), 2),"\n",sep='')

print("To display the mean of all permissible scores of a diver:")
n = int(input("Enter the number of judges: "))

obj = DivingScores(n)
obj.accept()
obj.display()
obj.permissible_scores()
obj.final_score()