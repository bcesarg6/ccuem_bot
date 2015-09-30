#-*- coding: utf-8 -*-
#Linguagem Inglês, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
                ['Things', 'Chair', 'Fire', 'Oven', 'Strings'],
                ['Games', 'League of Legends', 'Defence of the Ancient', 'Tree of savior', 'Spore']
            ]

#Botões dos Keyboards
novojogo = 'New Game'
ajuda = 'Help'
rank = 'Rank'
ligar = 'Start'
desligar = 'Stop'
config = 'Settings'
voltar = 'Back'
cancelar = 'Cancel'
comandos = 'Commands'
entrar = 'Join'
sair = 'Quit'
fechar_jogo = 'Close game'
cancelar_jogo = 'Cancel game'
arriscar = 'Try!'
esta_fora = 'You are out of this game'

#Respostas iniciais
linguas = 'Choose your language:'
iniciar_msg = 'Starting'
mudar_lingua = 'Change successfull'
start_msg = 'Hi, I am Forca Bot (HangMan) and I will help you to play hangman games!\nPress "new game" to start.'
is_enabled = 'Forca Bot is already on'
stop_msg = 'Forca Bot stopped'
start_help_msg = 'There is no game, please use "new game" to start one'
config_help_msg = 'Choose the language of the Bot\nPs.: The words for the game depends on the language'
voltar_msg = 'Main menu'
cantdo_msg = 'You cant do this'
comandos_msg = 'Commands'
ocupado_msg = 'Bot occupied'
teclado_msg = 'Keyboard'

#respostas PreGame
def inicialMsg(u_name):
    return 'Starting a new game!\n'+u_name+' will be the manager of this game!'

inicial_msg = 'Lets start defining the players of this game, who wants to join please choose Enter '+emoji_sorriso
close_game_msg = 'The game will start! In your turn, click on the letter to try or click Try! to try a word\nYou will play in this order:'
palavra_msg = 'The word is: '
categoria_msg = 'Category: '
esta_dentro_msg = 'You are already in this game'
sem_jogador_msg = 'All players quited, game will be canceled'
is_out_msg = 'You are not in this game'
cancelar_jogo_msg = 'Game canceled by the manager'
vidas_msg = 'Lifes: '
pre_game_help_msg = 'The game is open to people to join\nManager: use Close Game to close the game and start or Cancel Game to cancel it'

def novoAdmMsg(u_name):
    return 'A new Admin has been selected! '+u_name+' is the new Admin.'

def playerQuitMsg(u_name):
    return 'The player '+u_name+' quited.'

def entrarMsg(u_name):
    return 'Ok '+u_name+', you gonna play this turn\nIf you want to quit just use Quit'

#repostas InGame
in_game_help_msg = 'Clique nas letras para chuta-las, se quiser mais opções vá em Comandos'
arriscar_msg = 'Ok, tell me then, what is the word? Think wisely, if you make a mistake you will be eliminated from the game!'
round_errado_msg = 'It is not your turn! Wait for your turn to play.'
acertou_letra_msg = 'Right!'
errou_letra_msg = 'Wrong...'
jachutada_msg = 'This letter has already been tried'
umavida_msg = 'One life remaining, play serious bitch'
gameover_msg = 'YOU LOSE'
fora_msg = 'You are out of this game, wait untill it is over to enter in a new one'
prox_round_msg = 'Now it is your turn, '
venceu_msg = 'Correct! Congratulations, you won this game!'
perdeu_msg = 'Wrong! And you are out of this game now!'
