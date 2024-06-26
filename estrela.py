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

def main():
    global ultimoponto
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                savepontos()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    savepontos()
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if botaosalvar.collidepoint(x, y):
                        savepontos()
                    elif botaocarregar.collidepoint(x, y):
                        carregapontos()
                    elif botaoexcluir.collidepoint(x, y):
                        excluimarcacoes()
                    else:
                        nomeestrela1 = pede_nomeestrela()
                        novaestrela((x, y), nomeestrela1)

        tela.blit(fundo, (0, 0))
        desenhapontos()
        desenhalinhas()
        desenhabotoes()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

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

def desenhalinhas():
    posicoes = list(pontos.keys())
    for i in range(len(posicoes) - 1):
        pygame.draw.line(tela, cor, posicoes[i], posicoes[i + 1], 2)
        distancia = calculardistancia(posicoes[i], posicoes[i + 1])
        font = pygame.font.Font(None, 20)
        text = font.render(f"{distancia:.2f} anos luz", True, cor)
        tela.blit(text, ((posicoes[i][0] + posicoes[i + 1][0]) // 2, (posicoes[i][1] + posicoes[i + 1][1]) // 2))

def calculardistancia(p1, p2):
    return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))

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


def carregapontos():
    global pontos, ultimoponto
    if os.path.exists('savefile.txt'):
        with open('savefile.txt', 'r') as file:
            pontos_str = json.load(file)
        pontos = {tuple(map(int, k.split(','))): v for k, v in pontos_str.items()}
        if pontos:
            ultimoponto = list(pontos.keys())[-1]
        print("Marcações carregadas.")
    else:
        print("Nenhum arquivo de salvamento encontrado.")

def excluimarcacoes():
    global pontos, ultimoponto
    pontos = {}
    ultimoponto = None
    print("Todas as marcações foram excluídas.")

if __name__ == '__main__':
    main()