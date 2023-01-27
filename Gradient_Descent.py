import numpy as np

# To gradually approaching towards the minima , we need slope and learning rate , slope provides direction and learning_rate provies the length of step
# at first we start with any value of slope and intercept (which is preferably zero) and no of iterations to reach minima
# and also we start with any value of learning rate ( preferably 0.001 or 0.0001)
def grad_descent(x,y):
    slope=0
    intercept=0
    iterations=10000 #if you give 1 lakh iterations the final cost will be 1.0998945606533629e-25(larger than 10k iterartions) this means we are exceeding the minima value and there we need to lower the iterations
    n=len(x) # n is the no of data points
    learning_rate=0.001
    #cost=(1/n)*sum([val**2 for val in (y-y_predicted)])      # to check how well is our calculated slope and intercept we print cost , the cost should be reduce in each iterations
                # cost is also called cost function or minimum squared error
    for i in range(iterations):
        # partial derivative gives a slope 
        y_predicted=slope*x+intercept
        cost=(1/n)*sum([val**2 for val in (y-y_predicted)]) # description above
        derivative_m= -(2/n)*sum(x*(y-y_predicted))
        derivative_b= -(2/n)*sum(y-y_predicted)
        # for step we use learning rate
        slope=slope-learning_rate*derivative_m
        intercept=intercept-learning_rate*derivative_b

        print("slope: {} , intercept: {},minimum_error: {}, iterations: {}".format(slope,intercept,cost,i))

        # with the calculated slope and intercept now we can predict future values







x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

grad_descent(x,y)