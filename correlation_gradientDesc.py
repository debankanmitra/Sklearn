# Find correlation between math and computer science using gradient descent
# exercise: https://youtu.be/vsWrXfO3wWw

import numpy as np
import math

def correlation(mathematics,cs):
    slope=0
    intercept=0
    iterations=1000000 
    n=len(mathematics) 
    learning_rate=0.0001  
    cost_previous=0  
    for i in range(iterations):        
        y_predicted=slope*mathematics+intercept
        cost=(1/n)*sum([val**2 for val in (cs-y_predicted)]) 
        derivative_m= -(2/n)*sum(mathematics*(cs-y_predicted))
        derivative_b= -(2/n)*sum(cs-y_predicted)        
        slope=slope-learning_rate*derivative_m
        intercept=intercept-learning_rate*derivative_b

        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            print("slope: {} , intercept: {},minimum_error: {}, iterations: {}".format(slope,intercept,cost,i))
            break

        cost_previous=cost
        














mathematics=np.array([92,56,88,70,80,49,65,35,66,67])    
cs=np.array([98,68,81,80,83,52,66,30,68,73])  
correlation(mathematics,cs)  
