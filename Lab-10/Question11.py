#Compute statistical functions such as mean, median, standard deviation, and variance for an array containing  student marks.
import numpy as np

def statistical(data):
    mean=float(np.mean(data))   
    median=float(np.median(data))
    std=float(np.std(data))  
    variance=float(np.var(data))
    return {
        "Mean" : mean,
        "Median" : median,
        "Standard Deviation" : std,
        "Variance" : variance
    }

student_marks=np.array([90,95,60,70,55,82,65])
value=statistical(student_marks)
print("Statistical Function: ",value)
