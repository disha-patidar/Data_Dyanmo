import matplotlib.pyplot as plt 
import matplotlib.pyplot as mpimg
import numpy as np 
#Scattter plot
RollNo=[1,2,3,4,5,6,7,8,9,10]
marks=[10,20,30,40,50,60,70,80,90,100]
print(plt.scatter(RollNo,marks))
print(plt.scatter(RollNo,marks,color:'yellow'))
print(plt.figure(figsize=(12,8)))
print(plt.scatter(RollNo,marks,color:'yellow',marker:'*'))
print(plt.show())
temp_pune=[25,34,21,45,28,6,43,18,7,2]
humidity_pune=[28,25,29,20,26,15,19,29,52,55]
temp_banglore=[34,35,36,37,28,27,26,25,31,20]
humidity_banglore=[48,38,36,35,42,44,41,40,34,45]
print(plt.figure(figsize=(8,8)))
print(xtixks(np.arange(0,60,5)))
print(yticks(np.arange(10,60,5)))
print(plt.scatter(temp_pune,humidity_pune,'ro',markersize=15))
print(plt.xlabel('temp'))
print(plt.ylabel('humidity'))
print(plt.show())
#line plot
RollNo=[1,2,3,4,5,6,7,8,9,10]
marks=[10,20,30,40,50,60,70,80,90,100]
print(plt.scatter(RollNo,marks,linestyle='-'))
print(plt.scatter(RollNo,marks,'r-'))
print(plt.scatter(RollNo,marks,linestyle='--'))
print(plt.scatter(RollNo,marks,linestyle='.',color:'red'))
print(plt.show())
hours=[2,3,4,4,5,6,7,7,8,9,9,10,11,11,12]
marks=[6,10,15,20,34,44,55,67,70,80,90,99,100]
print(plt.figure(figsize=(8,8)))
print(xtixks(np.arange(0,15,1)))
print(yticks(np.arange(0,100,5)))
print(plt.plot(hours,marks,'r-'))
print(plt.xlabel('hours'))
print(plt.ylabel('marks'))
print(plt.show())
subjects=['Maths','English','Science','Hindi','SocialScience']
marks=[98,95,90,89,78]
print(plt.bar(subjects,marks))
print(plt.show())
subjects=['Maths','English','Science','Hindi','SocialScience']
marks=[98,95,90,89,78]
print(plt.pie(marks,labels=classes))
print(plt.pie(marks,labels=classes,colors=colors))
print(plt.show())
RollNo=[1,2,3,4,5,6,7,8,9,10]
marks=[10,20,30,40,50,60,70,80,90,100]
print(plt.subplot(2,2,1))
print(plt.plot(RollNo.,marks))