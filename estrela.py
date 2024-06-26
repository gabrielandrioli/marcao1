#Gabriel Augusto Andrioli e Alessandro da Rosa
import pygame
import tkinter as tk
from tkinter import simpledialog
import sys
import json
import os
import math

telatamanho = 800
telatamanho2 = 600
cor = (255, 255, 255)
pygame.init()
icone = pygame.image.load("assets/icone.png")
pygame.display.set_icon(icone)
tela = pygame.display.set_mode((telatamanho, telatamanho2))
pygame.display.set_caption('Space Marker')
clock = pygame.time.Clock()
fundo = pygame.image.load("assets/vasco.jpg")
ultimoponto = None
pontos = {} 
botaosalvar = pygame.Rect(10, 10, 150, 30)
botaocarregar = pygame.Rect(170, 10, 150, 30)
botaoexcluir = pygame.Rect(330, 10, 150, 30)
