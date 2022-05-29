#!/usr/bin/env python
# coding: utf-8

# In the below cell, I have defined a function to generate random numbers. I have used linear congruential generator algorithm

# In[ ]:


def linear_random(seed,modulus,a,c,n):
    result = [0]*n

    result[0]=seed
    for i in range(1,n):
        result[i]=((result[i-1]*a)+c)%modulus
    return result


# In the below cell, I have defined a function to generate random numbers between 0 and 1, this function is being used to calculate the value of pi. 

# In[27]:


def linear_random_float(seed,modulus,a,c,n):
    list2=linear_random(seed,modulus,a,c,n)
    for i in range(len(list2)):
        list2[i]=list2[i]/modulus
    return list2


# In[28]:


list1=linear_random(5,2**8,121,100,100)      # to generate a different set of values, change any value passed in this statement
print(list1)        #run this statement to print all the randomly generated values
list3=[seed]*n


# In[29]:


import matplotlib.pyplot as plt


# In the below cell I have displayed the random numbers generated, the Y-axis represents the seed used to generate values and the X-axis denotes the values generated. The values generated are shown by 'o'.

# In[32]:


plt.figure(figsize=(12,12))
plt.plot(list1, list3, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=4)
plt.xlabel('Random numbers generated')
plt.ylabel('Seed value')


# To calculate the value of pi, I have used the help of co-ordinate geometry. Considering the area of a square of side 2 and the circle that is inscribed inside it with radius 1. We consider only the first quadrant and then we randomly mark points in the first quadrant. Then we measure the number of points inside the circle. Once we have this value the approximate value of pi can be calculated with a simple formula mentioned in the below cell.

# In[50]:


# calculating the value of pi
n=10000
point_inside=0
total_points=n
X=linear_random_float(4,2**9,113,99,n)
Y=linear_random_float(7,2**9,169,101,n)
for i in range(n):
    x=X[i]
    y=Y[i]
    if (x*x+y*y)**0.5<1:
        point_inside+=1
pi=4*point_inside/n   #formula to calculate value of pi


# In[51]:


print(pi)


# In[ ]:




