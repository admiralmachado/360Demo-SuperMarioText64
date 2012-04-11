'''
Created on Apr 11, 2012

@author: Spencer
'''

import time

def load_game():
    print('Itsa Me! Mario!')
    time.sleep(2)
    print('Okey Dokey')
    time.sleep(1)

def read_letter():
    print('Dear Mario, Please come to the castle. I have baked a cake for you.')
    print('Yours truly,')
    print('Princess Toadstool')
    print('Peach <3')

def go_up_endless_staircase(stars):
    direction = "up"
    if(stars < 70):
        while(direction == "up"):
            print('You ascend the staircase but still haven\'t reached the top')
            direction = raw_input()

#MAIN

load_game()

read_letter()

go_up_endless_staircase(50)