from gpiozero import MotionSensor
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("WilhelmScream.wav")

pir = MotionSensor(4)

pir.wait_for_no_motion()

while True:
    print("Ready")
    pir.wait_for_motion()
    print("Motion detected")
    pygame.mixer.music.play()   
    time.sleep(3)	
