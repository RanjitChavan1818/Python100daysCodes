# some time this code run but sum time not
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num=randint(0,6)
print(dice_images[dice_num])

#Ans:->Because for need to print anything inside a list you have to access them only by indexing.
#but problem is that my random function generate 1 to 5 it never be genrate 0 , so it give error some time  
 