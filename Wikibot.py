#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Sat Jul 18 10:39:54 2020

@author: smithbarbose
"""
# first importing librarys

import wikipedia
import random 

#creating multiple responses for greating user 
bot_response=["Hello Stay Safe  ","How may I hepl you???","Hey Wanna play???","Why not test Me??"]


bot_response=random.choice(bot_response)    #using random function to choose one 


print(bot_response)                         #printing the response


print("Enter what you wanna search")        #taking input from the user
user_input=input()                          #storing it in a variable 

#passing the input to the functions 

search(user_input)

summary(user_input)

page(user_input)

#creating a function for search of the user input

def search(user_input):
       print(wikipedia.search(user_input))

       print("This our your search results")
       print("      ")

#creating a function for summary of the user input      

def summary(user_input):
   try:
       print(wikipedia.summary(user_input))  
   except wikipedia.DisambiguationError as e :
       print("To many search!!!! the best one is for you")
       error=random.choice(e.options)
       print(wikipedia.summary(error))

#creating a function for finding the page of the user input             

def page(user_input):
    try: 
        print(wikipedia.page(user_input).title)
        print(wikipedia.page(user_input).content)
        print(wikipedia.page(user_input).url)
    except wikipedia.DisambiguationError as e:
        print("To many pages!!!! kindly specify one")
        print(e.options)
    except wikipedia.PageError as p:
        print(p)
