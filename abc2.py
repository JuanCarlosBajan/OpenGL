from cmath import acos, asin, pi, sin, sqrt
import pygame
from pygame.locals import *
import glm #pip install PyGLM

from shaders import *

from jcopengl import Renderer, Model

width = 960
height = 540

deltaTime = 0.1

ws_value = 0
ad_value = 0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

bg = pygame.image.load("./models/textures/dog.bmp")
bg = pygame.transform.scale(bg,(width,height))

rend = Renderer(screen, bg)

rend.setShaders(vertex_shader, fragment_shader)

face = Model("./models/face.obj", "./models/textures/face.bmp")
skull = Model("./models/skull.obj", "./models/textures/bn.bmp")
stone = Model("./models/Stone.obj", "./models/textures/bn.bmp")
cat = Model("./models/cat.obj", "./models/textures/cat.bmp")
dog = Model("./models/dog.obj", "./models/textures/dog.bmp")
fish = Model("./models/fish.obj", "./models/textures/fish.bmp")


face.position.z = 0
rend.pointLight.x =2
rend.pointLight.y =2
rend.pointLight.z =2

skull.position.z=0
skull.position.y = -2
skull.scale = glm.vec3(0.2,0.2,0.2)
skull.rotation.x = -90

stone.position.z = 0
stone.position.y = -2
stone.scale = glm.vec3(0.4,0.4,0.4)

cat.position.z=0
cat.position.y = -3
cat.scale = glm.vec3(0.2,0.2,0.2)
cat.rotation.x = -90

dog.position.z=0
dog.position.y = -3
dog.scale = glm.vec3(0.2,0.2,0.2)
dog.rotation.x = -90

fish.position.z=0
fish.scale = glm.vec3(0.2,0.2,0.2)
fish.rotation.x = -90

rend.scene.append( face )

rend.camPosition.z = 10

actual_x = rend.camPosition.x
actual_y = rend.camPosition.y
actual_z = rend.camPosition.z

isRunning = True

zoom = 0
scroll =(0,0)

#INSIDE OF THE GAME LOOP

while isRunning:
    screen.blit(bg,(0,0))

    events = pygame.event.get()

    keys = pygame.key.get_pressed()

    mouse = pygame.mouse

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            
            elif event.key == pygame.K_f:
                rend.filledMode()
        
            elif event.key == pygame.K_q:
                rend.wireframeMode()

    if keys[K_1]:
        rend.setShaders(vertex_shader, toon_shader)

    if keys[K_2]:
        rend.setShaders(big_shader, reflection_shader)

    if keys[K_3]:
        rend.setShaders(x_shader, nothing_shader)

    if keys[K_4]:
        rend.setShaders(small_shader, duende_shader)

    if keys[K_5]:
        rend.setShaders(hulk_shader, tiktok_shader)

    if keys[K_z]:
        rend.scene.pop()
        rend.scene.append(skull)

    if keys[K_x]:
        rend.scene.pop()
        rend.scene.append(stone)

    if keys[K_c]:
        rend.scene.pop()
        rend.scene.append(cat)

    if keys[K_v]:
        rend.scene.pop()
        rend.scene.append(dog)

    if keys[K_b]:
        rend.scene.pop()
        rend.scene.append(fish)

    if rend.camPosition.x > 0.00 and rend.camPosition.z > 0.00:
        rend.camRotation.y = ((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z )**2)))-pi/2)*(180/pi)).real
    if rend.camPosition.x > 0.00 and rend.camPosition.z < 0.00:
        rend.camRotation.y = (((acos((rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z )**2)))+pi/2)*(180/pi)).real)
    if rend.camPosition.x < 0.00 and rend.camPosition.z < 0.00:
        rend.camRotation.y = (((acos((rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z )**2)))+pi/2)*(180/pi)).real)
    if rend.camPosition.x < 0.00 and rend.camPosition.z > 0.00:
        rend.camRotation.y = (((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z )**2)))-pi/2)*(180/pi)).real)

    if mouse.get_pos()[0]-500 < -100:
        distance = abs(sqrt(rend.camPosition.x**2 + (rend.camPosition.z )**2))
        ad_value += (1 * deltaTime)%(2*pi)
        rend.camPosition.x = (sin(ad_value) * distance).real
        actual_x = rend.camPosition.x
        rend.camPosition.z = (sin(ad_value + pi/2) * distance).real
        actual_z = rend.camPosition.z

    elif mouse.get_pos()[0]-500 > 100:
        distance = abs(sqrt(rend.camPosition.x**2 + (rend.camPosition.z )**2))
        ad_value -= (1 * deltaTime)%(2*pi)
        rend.camPosition.x = (sin(ad_value) * distance).real
        actual_x = rend.camPosition.x
        rend.camPosition.z = (sin(ad_value + pi/2) * distance).real
        actual_z = rend.camPosition.z

    if mouse.get_pos()[1]<100:
        if rend.camPosition.y< 5:
            distancez = abs(sqrt((rend.camPosition.z )**2 +(rend.camPosition.y )**2 + (rend.camPosition.x )**2))
            ws_value += (1 * deltaTime)%(2*pi)
            rend.camPosition.y = (sin(ws_value) * distancez).real
            rend.update()

    elif mouse.get_pos()[1]>400:
        if rend.camPosition.y> -5:
            distancez = abs(sqrt((rend.camPosition.z )**2 +(rend.camPosition.y )**2 + (rend.camPosition.x )**2))
            ws_value -= (1 * deltaTime)%(2*pi)
            rend.camPosition.y = (sin(ws_value) * distancez).real
    
    for event in events:
            if event.type == pygame.QUIT:
                loop = 0
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if event.button == 4:
                    if abs(rend.camPosition.z) > 2 and rend.camPosition.z >0:
                        rend.camPosition.z -= deltaTime*3
                    if abs(rend.camPosition.z) > 2 and rend.camPosition.z <0:
                        rend.camPosition.z += deltaTime*3
                if event.button == 5:
                    if abs(rend.camPosition.z) > 2 and rend.camPosition.z >0:
                        rend.camPosition.z += deltaTime*3
                    if abs(rend.camPosition.z) > 2 and rend.camPosition.z <0:
                        rend.camPosition.z -= deltaTime*3
        


    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime

    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime

    if keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime

    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime

    deltaTime = clock.tick(60) / 1000

    rend.time += deltaTime
    #print(deltaTime)
    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()