from random import randint
from time import sleep
import pygame

pygame.init()
pygame.font.init()

ther = 'Trabalho-Final\images\\thermometer.png'
merc = 'Trabalho-Final\images\mercury.png'
icon = 'Trabalho-Final\images\icon.png'
temperature = 16  # ENTRADA LORAWAN
heightDisplay = 700
widthDisplay = 300
elements = {0: ther, 1: merc, 2: icon}
window = pygame.display.set_mode((widthDisplay, heightDisplay))

icon = pygame.image.load(elements[2])
pygame.display.set_caption('MQTT - Thermometer')
pygame.display.set_icon(icon)

quitGame = False

while not quitGame:
    #temperature = randint(16, 40)

    insert = pygame.image.load(elements[0])
    window.blit(insert, (0, 0))

    if (temperature <= 16):
        mercury_display = 0
    elif (temperature > 16 and temperature < 18):
        mercury_display = -10
    elif (temperature > 17 and temperature < 19):
        mercury_display = -20
    elif (temperature > 18 and temperature < 20):
        mercury_display = -30
    elif (temperature > 19 and temperature < 21):
        mercury_display = -40
    elif (temperature > 20 and temperature < 22):
        mercury_display = -50
    elif (temperature > 21 and temperature < 23):
        mercury_display = -100
    elif (temperature > 22 and temperature < 24):
        mercury_display = -150
    elif (temperature > 24):
        mercury_display = -200

    insert = pygame.image.load(elements[1])
    window.blit(insert, (0, mercury_display))

    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    fontColor = (0, 0, 0)
    text = myfont.render(f'{temperature}°C', False, (fontColor))
    window.blit(text, (108, 550))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame = True

    sleep(1)