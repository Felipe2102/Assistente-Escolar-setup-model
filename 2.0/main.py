from datetime import datetime
import PySimpleGUI as sg
import os

Dia = datetime.now().weekday()

def setup():
	#Define o tema
	sg.theme('DarkGrey13')
	#Cria as pastas
	os.mkdir('./Data')
	os.mkdir('./Data/Lessons')

	#Cria os arquivos
	ASEG = open('Data/Lessons/Aulas_seg.txt','w')
	ATER = open('Data/Lessons/Aulas_ter.txt','w')
	AQUA = open('Data/Lessons/Aulas_qua.txt','w')
	AQUI = open('Data/Lessons/Aulas_qui.txt','w')
	ASEX = open('Data/Lessons/Aulas_sex.txt','w')
	#Fecha os arquivos criados
	ASEG.close()
	ATER.close()
	AQUA.close()
	AQUI.close()
	ASEX.close()
	#Reabre os arquivos como leitura e escrita
	ASEG = open('Data/Lessons/Aulas_seg.txt','r+')
	ATER = open('Data/Lessons/Aulas_ter.txt','r+')
	AQUA = open('Data/Lessons/Aulas_qua.txt','r+')
	AQUI = open('Data/Lessons/Aulas_qui.txt','r+')
	ASEX = open('Data/Lessons/Aulas_sex.txt','r+')
	#Pega o input do usuário e salva as alterações 
	sg.popup("parece que você não tem nenhuma aula configurada ;-;")
	ASEG.write(sg.PopupGetText('Quais aulas você tem na segunda?'))
	ATER.write(sg.PopupGetText('Quais aulas você tem na terça?'))
	AQUA.write(sg.PopupGetText('Quais aulas você tem na quarta?'))
	AQUI.write(sg.PopupGetText('Quais aulas você tem na quinta?'))
	ASEX.write(sg.PopupGetText('Quais aulas você tem na sexta?'))
	sg.popup('configuração finalizada!')
	#Fecha os arquivos
	ASEG.close()
	ATER.close()
	AQUA.close()
	AQUI.close()
	ASEX.close()

def Redefinir():
	#Define o tema
	sg.theme('DarkGrey13')
	#Remove os arquivos
	os.remove('./Data/Lessons/Aulas_seg.txt')
	os.remove('./Data/Lessons/Aulas_ter.txt')
	os.remove('./Data/Lessons/Aulas_qua.txt')
	os.remove('./Data/Lessons/Aulas_qui.txt')
	os.remove('./Data/Lessons/Aulas_sex.txt')
	#Cria os arquivos
	ASEG = open('Data/Lessons/Aulas_seg.txt','w')
	ATER = open('Data/Lessons/Aulas_ter.txt','w')
	AQUA = open('Data/Lessons/Aulas_qua.txt','w')
	AQUI = open('Data/Lessons/Aulas_qui.txt','w')
	ASEX = open('Data/Lessons/Aulas_sex.txt','w')
	#Fecha os arquivos criados
	ASEG.close()
	ATER.close()
	AQUA.close()
	AQUI.close()
	ASEX.close()
	#Reabre os arquivos como leitura e escrita
	ASEG = open('Data/Lessons/Aulas_seg.txt','r+')
	ATER = open('Data/Lessons/Aulas_ter.txt','r+')
	AQUA = open('Data/Lessons/Aulas_qua.txt','r+')
	AQUI = open('Data/Lessons/Aulas_qui.txt','r+')
	ASEX = open('Data/Lessons/Aulas_sex.txt','r+')
	#Pega as informações das aulas do úsuario e escreve as alterações nos arquivos
	ASEG.write(sg.PopupGetText('Quais aulas você tem na segunda?'))
	ATER.write(sg.PopupGetText('Quais aulas você tem na terça?'))
	AQUA.write(sg.PopupGetText('Quais aulas você tem na quarta?'))
	AQUI.write(sg.PopupGetText('Quais aulas você tem na quinta?'))
	ASEX.write(sg.PopupGetText('Quais aulas você tem na sexta?'))
	#Informa ao úsuario que é presciso reiniciar o programa para concluir as configurações
	sg.popup('configuração finalizada, reinicie o programa para aplicar as novas configurações.')
	#Fecha os arquivos novamente 
	ASEG.close()
	ATER.close()
	AQUA.close()
	AQUI.close()
	ASEX.close()
	#Fecha a janela
	window.close()

try:
	ASEG = open('Data/Lessons/Aulas_seg.txt','r').read()
	ATER = open('Data/Lessons/Aulas_ter.txt','r').read()
	AQUA = open('Data/Lessons/Aulas_qua.txt','r').read()
	AQUI = open('Data/Lessons/Aulas_qui.txt','r').read()
	ASEX = open('Data/Lessons/Aulas_sex.txt','r').read()

except FileNotFoundError:
	setup()

if Dia == 0:
	Aulas = ASEG
elif Dia == 1:
	Aulas = ATER
elif Dia == 2:
	Aulas = AQUA
elif Dia == 3:
	Aulas = AQUI
elif Dia == 4:
	Aulas = ASEX

sg.theme('DarkGrey13')
layout = [
	[sg.Text('Suas aulas são:')],
	[sg.Text(Aulas)],
	[sg.Button('Redefinir'), sg.Exit()]
]
window = sg.Window('Teste', layout, size=(150,100), element_justification='center', finalize=True)

while True:
	event, values = window.read()

	if event == 'Redefinir':
		window.hide()
		Redefinir()
	if event == sg.WIN_CLOSED:
		break
	if event == 'Exit':
		break