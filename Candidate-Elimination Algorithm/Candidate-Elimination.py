#importing libraries
import numpy as np
import pandas as pd

#We will be using the same dataset that we created for FindS Algorithm

#reading data from the csv file
data = pd.read_csv('FINDS')
print(data)

#array of all the attributes
concept = np.array(data)[:,:-1]
print("The attributes are: \n",concept)

#Our target is 'Preferred' column

#Taking out target into separate dataframe
target = np.array(data)[:,-1]
print("The target is: ",target)

#Now we train the function to implement Candidate-Elimination Algorithm

def train(c,t):
    
    '''c= a dataframe with all the attributes
       t= a dataframe with output values'''
    
    #First we initialise Specific Hypothesis and General Hypothesis
    for i, val in enumerate(t):
        if val == "YES":
            specific_h = c[i].copy()
            break
            
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    
    print("General Hypothesis is: \n", general_h)
    print("Specific Hypothesis is: \n", specific_h)
    
    #training iterations
    for i, val in enumerate(c):

        # Checking if the hypothesis has a positive target
        if t[i] == "YES":
            for x in range(len(specific_h)):
                # Change values in S & G only if values change
                if val[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        # Checking if the hypothesis has a negative target
        if t[i] == "NO":
            for x in range(len(specific_h)):
                # For negative hyposthesis change values only in G
                if val[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

        print("\nInstance",i+1,":")
        print(specific_h)
        print(general_h)
        
    
     # Indices where we have empty rows, meaning those that are unchanged
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        # remove those rows from general_h
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    
    
    # Return final values
    return specific_h, general_h
  
  S, G = train(concept, target)
print("\nFinal General Hypothesis:", G, sep="\n")
print("\nFinal Specific Hypothesis:", S, sep="\n")
