# Importing libraries
import pandas as pd
import numpy as np

#reading data in the csv file
data = pd.read_csv('FindS')
print(data)

#array of all the attributes
concept = np.array(data)[:,:-1]
print("The attributes are: \n",concept)

#segragating the target that has YES and NO Values. Here in our file it is the 'Preferred?' column
target = np.array(data)[:,-1]
print("The target is: ",target)

#training function to implement find-s algorithm
def train(c,t):
    
    #global specific_h
    
    for i, val in enumerate(t):
        if val == "YES":
            specific_h = c[i].copy()
            break
             
    for i, val in enumerate(c):
        if t[i] == "YES":
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                else:
                    pass
                
    return specific_h
  
print('The most specific hypothesis is: ',train(concept, target))
