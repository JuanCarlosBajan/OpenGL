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

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)

face = Model("./models/face.obj", "./models/textures/face.bmp")
skull = Model("./models/skull.obj", "./models/textures/bn.bmp")
stone = Model("./models/Stone.obj", "./models/textures/bn.bmp")
cat = Model("./models/cat.obj", "./models/textures/cat.bmp")


face.position.z = -5

skull.position.z=-15
skull.position.y = -2
skull.scale = glm.vec3(0.2,0.2,0.2)
skull.rotation.x = -90

stone.position.z = -10
stone.position.y = -2
stone.scale = glm.vec3(0.4,0.4,0.4)

cat.position.z=-15
cat.position.y = -3
cat.scale = glm.vec3(0.2,0.2,0.2)
cat.rotation.x = -90

rend.scene.append( face )


isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

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
        pass

    if keys[K_b]:
        pass


    if keys[K_a]:
        distance = abs(rend.scene[0].position.z)
        ad_value += (1 * deltaTime)%(2*pi)
        rend.camPosition.x = (sin(ad_value) * distance).real
        ws_value += (1 * deltaTime)%(2*pi)
        rend.camPosition.z = (sin(ws_value + pi/2) * distance).real -distance
        if rend.camPosition.x > 0.00 and rend.camPosition.z+distance > 0.00:
            #print(((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real)
            rend.camRotation.y = ((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real
        if rend.camPosition.x > 0.00 and rend.camPosition.z+distance < 0.00:
            #print(((acos((rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))+pi/2)*(180/pi)).real)
            rend.camRotation.y = (((acos((rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))+pi/2)*(180/pi)).real)
        if rend.camPosition.x < 0.00 and rend.camPosition.z+distance < 0.00:
            #print(((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real)
            rend.camRotation.y = (((acos((rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))+pi/2)*(180/pi)).real)
        if rend.camPosition.x < 0.00 and rend.camPosition.z+distance > 0.00:
            #print(((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real)
            rend.camRotation.y = (((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real)

    elif keys[K_d]:
        distance = abs(rend.scene[0].position.z)
        ad_value -= (1 * deltaTime)%(2*pi)
        rend.camPosition.x = (sin(ad_value) * distance).real
        ws_value -= (1 * deltaTime)%(2*pi)
        rend.camPosition.z = (sin(ws_value + pi/2) * distance).real -distance
        if rend.camPosition.x > 0.00 and rend.camPosition.z+distance > 0.00:
            #print(((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real)
            rend.camRotation.y = ((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real
        if rend.camPosition.x > 0.00 and rend.camPosition.z+distance < 0.00:
            #print(((acos((rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))+pi/2)*(180/pi)).real)
            rend.camRotation.y = (((acos((rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))+pi/2)*(180/pi)).real)
        if rend.camPosition.x < 0.00 and rend.camPosition.z+distance < 0.00:
            #print(((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real)
            rend.camRotation.y = (((acos((rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))+pi/2)*(180/pi)).real)
        if rend.camPosition.x < 0.00 and rend.camPosition.z+distance > 0.00:
            #print(((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real)
            rend.camRotation.y = (((acos(-(rend.camPosition.x/sqrt(rend.camPosition.x**2 + (rend.camPosition.z +distance)**2)))-pi/2)*(180/pi)).real)

    if keys[K_w]:
        distance = abs(rend.scene[0].position.z)
        if(distance > 1):
            rend.scene[0].position.z += deltaTime

    elif keys[K_s]:
        distance = abs(rend.scene[0].position.z)
        if(distance < 10):
            rend.scene[0].position.z -= deltaTime
        
    if keys[K_SPACE]:
        if(rend.camPosition.y < 2):
            rend.camPosition.y += deltaTime

    elif keys[K_LSHIFT]:
        if(rend.camPosition.y > -2):
            rend.camPosition.y -= deltaTime
    
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