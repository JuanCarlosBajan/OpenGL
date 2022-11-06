from cmath import acos, asin, pi, sin, sqrt
import pygame
from pygame.locals import *

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

face = Model("./model.obj", "model.bmp")

face.position.z = -5

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
        rend.setShaders(x_shader, toon_shader)

    if keys[K_4]:
        rend.setShaders(small_shader, duende_shader)

    if keys[K_5]:
        rend.setShaders(hulk_shader, tiktok_shader)


    if keys[K_a]:
        distance = abs(face.position.z)
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
        distance = abs(face.position.z)
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
        distance = abs(face.position.z)
        if(distance > 1):
            face.position.z += deltaTime

    elif keys[K_s]:
        distance = abs(face.position.z)
        if(distance < 10):
            face.position.z -= deltaTime
        
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