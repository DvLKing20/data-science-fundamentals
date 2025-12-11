import numpy as np

class LinearRegression:
    def __init__(self):
        self.study_hours = np.array([1,2,3,4])
        self.marks_scores = np.array([2,4,6,9])
        self.m = 1
        self.b = 1
        
    def loss_function(self):
        #formula y = m*x+b
        total_errors = []

        for x,y in zip(self.study_hours,self.marks_scores):
            m = self.m
            b = self.b
            predict = m*x+b
            total_errors.append((y-predict))
           
            print("Predicted_Marks :",predict)
            
        errors = np.array(total_errors)
        mse = ((errors)**2).mean()
        print(mse)
        return errors,mse
    
    def gradient_descent(self,errors):
        lr = 0.1
        dm = -2*((self.study_hours * errors).sum()/len(errors))
        db = -2*(errors.sum()/len(errors))
        self.m = self.m - lr * dm
        self.b = self.b - lr * db
    
    
    def add_input(self):
        user_input = input("Enter the value of x: ")
        split = user_input.split(",")
        array = np.array([int(num) for num in split])
        print(array)
        for x in array:
            m = self.m 
            b = self.b
            predict = m*x+b
           
            print("Predicted_Marks :",predict)
    
    def main(self):
        while True:
         errors,mse = self.loss_function()
         self.gradient_descent(errors)
         if mse < 0.0980:
             break
        self.add_input()
    
p = LinearRegression()
p.main()