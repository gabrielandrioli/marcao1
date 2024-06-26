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

def novaestrela(posicao, nome):
    global ultimoponto
    pontos[posicao] = nome
    ultimoponto = posicao

def desenhapontos():
    for (x, y), nome in pontos.items():
        pygame.draw.circle(tela, cor, (x, y), 5)
        font = pygame.font.Font(None, 20)
        text = font.render(nome, True, cor)
        tela.blit(text, (x + 10, y - 10))

def pede_nomeestrela():
    root = tk.Tk()
    root.withdraw()
    nome = simpledialog.askstring('Nome da Estrela', 'Digite o nome da estrela:')
    root.destroy()
    return nome if nome else 'Desconhecido'

def desenhabotoes():
    pygame.draw.rect(tela, (255, 255, 255), botaosalvar)
    pygame.draw.rect(tela, (255, 255, 255), botaocarregar)
    pygame.draw.rect(tela, (255, 255, 255), botaoexcluir)
    font = pygame.font.Font(None, 25)
    texto_salvar = font.render("Salvar Marcações", True, (0, 0, 0))
    texto_carregar = font.render("Carregar Marcações", True, (0, 0, 0))
    texto_excluir = font.render("Excluir Marcações", True, (0, 0, 0))
    tela.blit(texto_salvar, (botaosalvar.x + 5, botaosalvar.y + 5))
    tela.blit(texto_carregar, (botaocarregar.x + 5, botaocarregar.y + 5))
    tela.blit(texto_excluir, (botaoexcluir.x + 5, botaoexcluir.y + 5))
    
def savepontos():
    with open('savefile.txt', 'w') as file:
        pontos_str = {f"{x},{y}": nome for (x, y), nome in pontos.items()}
        json.dump(pontos_str, file)
    print("Marcações salvas.")
