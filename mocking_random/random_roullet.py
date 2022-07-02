import random #importing the random module 

outcome=["red","black","green"]

#assgining the weights for the random result
result=random.choices(outcome, weights=[18,18,2],k=10)

print(result)