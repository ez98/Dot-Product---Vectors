#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

def dot_product(vector1,vector2):
    
    #first vector
    
    i = vector1[0]
    
    j = vector1[1]

    k = vector1[2]
    
    #second vector
    
    i2 = vector2[0]

    j2 = vector2[1]

    k2 = vector2[2]

    return (i*i2) + (j*j2) + (k*k2)

def NewCalc(): #Basically a restart function after first set of vectors have been entered
    
    new_calc = input('Recalulate? (Y or N): ').lower()
    
    if new_calc ==  'y':
        
        return 'y'
    else:
        return False
print("Welcome to Eric's dot product program.")

print('\n')
while True:
    
    time.sleep(1)
    
    i_j_k_1 = input("Enter your 1st vector in the following format-> i,j,k: ")

    vector1 = tuple(map(int, i_j_k_1.split(','))) #gets rid of the commas between the vector 
                                                  #and converts into a tuple

    print(vector1)

    i_j_k_2 = input("Enter your 2nd vector in the following format-> i,j,k: ")

    vector2 = tuple(map(int, i_j_k_2.split(',')))

    print(vector2)

    time.sleep(1.0)

    dp = dot_product(vector1,vector2)
    
    print(f'Dot Product: {dp}')
    
    time.sleep(1.2)
    
    if not NewCalc():
        time.sleep(1)
        print('Goodbye!')
        break


# In[ ]:




