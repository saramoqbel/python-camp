#!/usr/bin/env python
# coding: utf-8

# In[1]:


NumberOfSchoolDaysSoFar=int(input("Enter number of days you have studied so far:"))
print("convert to hours=",NumberOfSchoolDaysSoFar*24)


# In[2]:


Temperature=int(input("Enter the temperature in fahrenheit:"))
print("temperature in celsius=",(Temperature-32)*5/9)


# In[3]:


Price=int(input("Enter the product price:"))
print("Vat=",Price*(15/100))


# In[4]:


import random
mynum = random.randint(0,10)
guess  = int(input('Enter a number between 0 and 10:'))
count = 1
while guess != mynum and count < 3:
    if guess < mynum:
        print("Too Low")
    else:
        print("Too High")
    guess  = int(input('Enter a number between 0 and 10:'))
    count = count +1 

if guess == mynum:
    print("Great you got the correct number", mynum)
else:
    print("Game Over, you didn't got the number")
print('Your trials =  ', count)


# In[5]:


import turtle
turtle.shape('turtle')
y = 0
for x in range(60):
    for i in range(4):
        turtle.forward(100+y)
        turtle.right(90)
    turtle.right(5)
    y +=5

