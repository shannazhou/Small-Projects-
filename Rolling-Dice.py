# this project is to build a program that interact with the user to guess the sum of two rolling dice and determine who is the winner.
from random import randint
from time import sleep 

def get_user_guess():
  guess=int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll=randint(1, number_of_sides)
  second_roll=randint(1,number_of_sides)
  max_val=number_of_sides*2
  print "the maximun possible value is %d" % max_val  
  guess=get_user_guess()
  if guess>max_val:
    return "not valid number" 
  else:
    print "Rolling..."
    sleep(2)
    print "the first roll is %d" % first_roll
    sleep(1) 
    print "the second roll is %d" % second_roll
    sleep(1)
    total_roll=first_roll+ second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll: 
      print "You Won"
    else: 
      print "You lost"
 
roll_dice(6)
  
  
  
    
