import random as r
import math as m
def fruits():
    l=["apple","apricot","banana","bluberry","coconut","custardapple","pineapple",
       "date","fig","gooseberry","grapes","guava","jackfruit","lime","litchi",
       "mango","mulberry","muskmelon","orange","papaya","peach","pear","plum",
       "pomegranate","naseberry","starfruit","caper","chestnut","watermelon",
       "kiwi","cambuca","avocado","blackberry","cherry","durian"]
    a=r.random()
    a*=100
    a=m.floor(a)
    a=(a%35)
    return l[a]
