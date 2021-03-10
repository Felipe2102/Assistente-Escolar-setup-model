import PySimpleGUI as sg
import os
import os.path
from pathlib import Path

def setup():
	global Aulas
	#Cria os arquivos
	os.mkdir('./Data')
	os.mkdir('./Data/Lessons')
	Aulas = open('Data/Lessons/Aulas.txt','w')
	Aulas.close()
	Aulas = open('Data/Lessons/Aulas.txt','r+')
	#Pega as informações das aulas do úsuario
	sg.popup("parece que você não tem nenhuma aula configurada ;-;")
	#Escreve as alterações nos arquivos
	Aulas.write(sg.PopupGetText('Quais aulas você tem na segunda?') + '\n\n' )
	Aulas.write(sg.PopupGetText('Quais aulas você tem na terça?') + '\n\n' )
	Aulas.write(sg.PopupGetText('Quais aulas você tem na quarta?') + '\n\n' )
	Aulas.write(sg.PopupGetText('Quais aulas você tem na quinta?') + '\n\n' )
	Aulas.write(sg.PopupGetText('Quais aulas você tem na sexta?') + '\n\n' )
	sg.popup('configuração finalizada!')
	Aulas.close()

def Redefinir():
	#Cria os arquivos
	global Aulas
	os.remove('./Data/Lessons/Aulas.txt')
	Aulas = open('Data/Lessons/Aulas.txt','w')
	Aulas.close()
	Aulas = open('Data/Lessons/Aulas.txt','r+')
	#Pega as informações das aulas do úsuario
	#Escreve as alterações nos arquivos
	Aulas.write(sg.PopupGetText('Quais aulas você tem na segunda?') + '\n\n' )
	Aulas.write(sg.PopupGetText('Quais aulas você tem na terça?') + '\n\n' )
	Aulas.write(sg.PopupGetText('Quais aulas você tem na quarta?') + '\n\n' )
	Aulas.write(sg.PopupGetText('Quais aulas você tem na quinta?') + '\n\n' )
	Aulas.write(sg.PopupGetText('Quais aulas você tem na sexta?') + '\n\n' )
	sg.popup('configuração finalizada, reinicie o programa para aplicar as novas configurações.')
	Aulas.close()
	window.close()

try:
	Aulas = open('Data/Lessons/Aulas.txt', 'r').read()
	print(Aulas)

except FileNotFoundError:
	setup()

sg.theme('DarkGrey13')
layout = [
	[sg.Text('Suas aulas são:')],
	[sg.Text(Aulas)],
	[sg.Button('Redefinir'), sg.Exit()]
]
window = sg.Window('Teste', layout, size=(300,300),finalize=True)

while True:
	event, values = window.read()
	if event == 'Redefinir':
		window.hide()
		Redefinir()
	if event == sg.WIN_CLOSED:
		break
	if event == 'Exit':
		break