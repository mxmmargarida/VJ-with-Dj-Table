# vjhero.py
# Copyright 2013 Margarida Carvalho
# Licensed under the terms of GNU GENERAL PUBLIC LICENSE.
# http://www.gnu.org/licenses/gpl.html
# Work in progress: some buttons are not recognized yet
# using djhero controller of ps2
import pygame
from math import sin,cos
from pygame.locals import *

def draw_thing(screen,x,y,current_color):
    # Draw an ellipse
    pygame.draw.ellipse(screen,current_color,[35+x,0+y,80,45])
    
def rodar_image(x_coord,y_coord,theta):
    x_coord = x_coord -250
    y_coord = y_coord-250
    x_new = x_coord * cos(theta)+y_coord*sin(theta)+250 
    y_new = -1*x_coord*sin(theta)+y_coord*cos(theta)+250
    return x_new,y_new

pygame.init()
pygame.display.set_caption("VJ Hero")

#define colors
black = [0,0,0]
white = [255,255,255]
green = [0,255,0]
red = [255,0,0]
purple = [72,61,139]
theta = 0
current_color = white
#size of the screen
size = [600,650]
screen = pygame.display.set_mode(size)

# close when the user clicks to close
done = False
clock = pygame.time.Clock()

# Hide the mouse
pygame.mouse.set_visible(0)

# Current position
x_coord=150
y_coord=150


# Count the joysticks the computer has
# Set up the joystick
pygame.joystick.init()
joystick_count=pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print ("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
    print "Detected joystick '",my_joystick.get_name(),"'"

while done == False:
    
    rodar = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if joystick_count != 0:
            
            if event.type == JOYAXISMOTION:
                rodar = True
            elif event.type == JOYBUTTONDOWN:
                if event.button == 1: #green button
                    current_color = green
                elif event.button == 0: # purple button
                    current_color = purple
                elif event.button == 2: # red button
                    current_color = red
                elif event.button == 3: #big black button
                    black = [(black[i]+10)%256 for i in range(3)]
            elif event.type == JOYBUTTONUP:
                current_color = white                        
    # put background black and erase everything
    screen.fill(black)
         
    if x_coord>500:
        x_coord = 500
    if x_coord<0:
        x_coord = 0
    if y_coord<0:
        y_coord = 0
    if y_coord>500:
        y_coord = 500
    if rodar:
        theta =theta +0.01 
        x_coord,y_coord = rodar_image(x_coord,y_coord,theta)
    draw_thing(screen,x_coord,y_coord,current_color)
    
    pygame.display.flip()
    clock.tick(40)
    
pygame.quit() 
