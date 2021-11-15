import os

os.system("cls" if os.name == "nt" else "clear")

#começo

print(''' ▄▄▄      ▓█████▄  ██▓ ██▒   █▓ ██▓ ███▄    █  ██░ ██  ▄▄▄      
▒████▄    ▒██▀ ██▌▓██▒▓██░   █▒▓██▒ ██ ▀█   █ ▓██░ ██▒▒████▄    
▒██  ▀█▄  ░██   █▌▒██▒ ▓██  █▒░▒██▒▓██  ▀█ ██▒▒██▀▀██░▒██  ▀█▄  
░██▄▄▄▄██ ░▓█▄   ▌░██░  ▒██ █░░░██░▓██▒  ▐▌██▒░▓█ ░██ ░██▄▄▄▄██ 
 ▓█   ▓██▒░▒████▓ ░██░   ▒▀█░  ░██░▒██░   ▓██░░▓█▒░██▓ ▓█   ▓██▒
 ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓     ░ ▐░  ░▓  ░ ▒░   ▒ ▒  ▒ ░░▒░▒ ▒▒   ▓▒█░
  ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░   ░ ░░   ▒ ░░ ░░   ░ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░
  ░   ▒    ░ ░  ░  ▒ ░     ░░   ▒ ░   ░   ░ ░  ░  ░░ ░  ░   ▒   
      ░  ░   ░     ░        ░   ░           ░  ░  ░  ░      ░  ░
           ░               ░                                    ''')
           
print('\033[1;34mCarregando...\033[1;34m')
import time
time.sleep (10) 

#cores

preto = ('\033[1;30m')

vermelho = ('\033[1;31m')

verde = ('\033[1;32m')

amarelo = ('\033[1;33m')

azul = ('\033[1;34m')

#End(cores)
           
nome = str(input(f'{amarelo}Qual é o seu nome?: '))

print(f'{vermelho}Olá {preto}{nome}{preto}, seja bem vindo ao meu jogo feito em python.')

continuacao = str(input('Vamos começar? (s/n): '))

if continuacao == ('s'):
	print(' ')
else:
	print('flwkk')
	exit()

niveis = int(input('Digite o numero 1 pra continuar: '))

if niveis == (1):
	print('''
	
	
1 = Ciências
	
2 = Matematica
	
3 = Geografia
	
	''')
	temas = int(input('Escolha o tema: '))
	
####################################

if temas == (1):
	
	os.system("cls" if os.name == "nt" else "clear")
	print(f'{preto}=== Ciências ===')
	print(f'''{verde}
	
	Alternativas: 

1) = É o processo pelo qual as plantas verdes e alguns organismos usam a luz do sol para transformar o CO2 e a água em açúcares e oxigênio.
    
2) = É o processo pelo qual as plantas se reproduzem, pra soltar oxigênio
    
3) = É o processo pelo qual as plantas entram em estado de decomposição
    
4)   = É whatsapp
	
	{verde}''')
	
	qc1 = int(input('O que é fotosintese?: '))
	if qc1 == (1):
		print('Acertou!!!')
		print('Proxima, faltam 3 perguntas ')
		time.sleep (3)
	else:
		print('Errou, era a (1)')
		exit()

####################################

	os.system("cls" if os.name == "nt" else "clear")
	print(f'{preto}=== Ciências ===')
	print(f'''{azul}

1) Tem entre 2 a 4 litros. São retirados 455 mililitros
	
2) Tem entre 4 a 6 litros. São retirados 450 mililitros

3) Tem 10 litros. São retirados 2 litros

4) Tem 7 litros. São retirados 1,5 litros

5) Tem 0,5 litros. São retirados 0,5 litros

{azul}''')
	qc2 = int(input(f'''{preto}
Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?: {preto}'''))
	if qc2 == (2):
		print(f'{vermelho}Acertou! proxima, faltam 2{vermelho}')
		time.sleep (3)
	else:
		print('Errou, era a alternativa 2')
		exit()
	
####################################

	os.system("cls" if os.name == "nt" else "clear")
	print(f'{preto}=== Ciências ===')
	print(f'''{vermelho}

1) 12 minutos

2) 1 dia

3) 12 horas

4) 8 minutos

5) segundos

{vermelho}''')
	qc2 = int(input(f'''{preto}
Quanto tempo a luz do Sol demora para chegar à Terra?: {preto}'''))
	if qc2 == (4):
		print(f'{vermelho}Acertou! proxima, falta apenas 1 pergunta {vermelho}')
		time.sleep (3)
	else:
		print('Errou, era a alternativa 4')
		exit()

####################################

	os.system("cls" if os.name == "nt" else "clear")
	print(f'{preto}=== Ciências ===')
	print(f'''{amarelo}

1) Tubarão branco, crocodilo e sucuri

2) Tigre, gavião e orca

3) Hiena, urso branco e lobo cinzento

4) Orca, onça e tarântula

5) Leão, tubarão branco e urso cinzento

{amarelo}''')
	qc2 = int(input(f'''{preto}
Quais são os três predadores do reino animal reconhecidos pela habilidade de caçar em grupo, se camuflar para surpreender as presas e possuir sentidos apurados, respectivamente: {preto}'''))
	if qc2 == (3):
		print(f'{vermelho}Acertou!{vermelho}')
		time.sleep (3)
	else:
		print('Errou, era a alternativa 3')
		exit()
	os.system("cls" if os.name == "nt" else "clear")

	print(''' ▄▄▄      ▓█████▄  ██▓ ██▒   █▓ ██▓ ███▄    █  ██░ ██  ▄▄▄      
▒████▄    ▒██▀ ██▌▓██▒▓██░   █▒▓██▒ ██ ▀█   █ ▓██░ ██▒▒████▄    
▒██  ▀█▄  ░██   █▌▒██▒ ▓██  █▒░▒██▒▓██  ▀█ ██▒▒██▀▀██░▒██  ▀█▄  
░██▄▄▄▄██ ░▓█▄   ▌░██░  ▒██ █░░░██░▓██▒  ▐▌██▒░▓█ ░██ ░██▄▄▄▄██ 
 ▓█   ▓██▒░▒████▓ ░██░   ▒▀█░  ░██░▒██░   ▓██░░▓█▒░██▓ ▓█   ▓██▒
 ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓     ░ ▐░  ░▓  ░ ▒░   ▒ ▒  ▒ ░░▒░▒ ▒▒   ▓▒█░
  ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░   ░ ░░   ▒ ░░ ░░   ░ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░
  ░   ▒    ░ ░  ░  ▒ ░     ░░   ▒ ░   ░   ░ ░  ░  ░░ ░  ░   ▒   
      ░  ░   ░     ░        ░   ░           ░  ░  ░  ░      ░  ░
           ░               ░                                    ''')
           
	print('Obg por usar!! ;)')
	time.sleep(4)
	os.system("cls" if os.name == "nt" else "clear")
	exit()

####################################

#Questão 6
	if temas == (2):
		os.system("cls" if os.name == "nt" else "clear")
		print(f'{preto}=== Matematica ===')
		print(f'''{azul}
	
1) 2700.

2) 2800.

3) 2900.

4) 3000.
	
	{azul}''')
	
		ms1 = int(input(f'{preto}Por qual número devemos multiplicar o número 0,75 de modo que a raiz quadrada do produto obtido seja igual a 45?: '))
		if ms1 == (1):
			print('Acertou!!!')
			print('Proxima, faltam 3 perguntas ')
			time.sleep (3)
		else:
			print('Errou, era a 1')
			exit()

####################################

####################################

#Questão 13
	if temas == (2):
		os.system("cls" if os.name == "nt" else "clear")
		print(f'{preto}=== Matematica ===')
		print(f'''{verde}
	
1) Carla tem 14, Paula tem 12, Leila tem 10 e Vivian tem 8.

2) Vivian tem 8, Leila tem 10, Paula tem 12 e Carla tem 14.

3) Carla tem 9, Paula tem 11, Leila tem 13 e Vivian tem 15.

4) Carla tem 10, Paula tem 12, Leila tem 14 e Vivian tem 16.

5) Vivian tem 9, Leila tem 11, Paula tem 13 e Carla tem 15.
	
	{verde}''')
	
		ms1 = int(input(f'{preto}Carla tem 2 reais a mais que Paula, Paula tem dois reais a mais que Leia e Leia tem dois reais a mais que Vivian. As 4 juntas possuem 48 reais. Quanto cada uma tem individualmente?: '))
		if ms1 == (5):
			print('Acertou!!!')
			print('Proxima, faltam 2 perguntas ')
			time.sleep (3)
		else:
			print('Errou, era a 5')
			exit()

###################################

####################################

#Questão 14
	if temas == (2):
		os.system("cls" if os.name == "nt" else "clear")
		print(f'{preto}=== Matematica ===')
		print(f'''{vermelho}
	
A parábola de equação y = ax² passa pelo vértice da parábola y = 4x – x²

1) 1.

2) 2.

3) 3.

4) -1.

5) nda.
	
	{vermelho}''')
	
		ms1 = int(input(f'{preto}Ache o valor de a: '))
		if ms1 == (1):
			print('Acertou!!!')
			print('Proxima, falta apenas 1 pergunta ')
			time.sleep (3)
		else:
			print('Errou, era a 1')
			exit()

###################################

####################################

#Questão 17
	if temas == (2):
		os.system("cls" if os.name == "nt" else "clear")
		print(f'{preto}=== Matematica ===')
		print(f'''{amarelo}
	
1) R/2.

2) 2R.

3) 4R.

4) 5R.

5) 16R.
	
	{amarelo}''')
	
		ms1 = int(input(f'{preto}Uma loja de materiais de construção vende dois tipos de caixas-d’água: tipo A e tipo B. Ambas têm formato cilíndrico e possuem o mesmo volume, e a altura da caixa d’água do tipo B é igual a 25% da altura da caixa d’agua do tipo A. Se R denota o raio da caixa d’água do tipo A, então o raio da caixa d’água do tipo B é: '))
		if ms1 == (2):
			print('Acertou!!!')
			time.sleep (2)
		else:
			print('Errou, era a 2')
			exit()
	os.system("cls" if os.name == "nt" else "clear")
	print(''' ▄▄▄      ▓█████▄  ██▓ ██▒   █▓ ██▓ ███▄    █  ██░ ██  ▄▄▄      
▒████▄    ▒██▀ ██▌▓██▒▓██░   █▒▓██▒ ██ ▀█   █ ▓██░ ██▒▒████▄    
▒██  ▀█▄  ░██   █▌▒██▒ ▓██  █▒░▒██▒▓██  ▀█ ██▒▒██▀▀██░▒██  ▀█▄  
░██▄▄▄▄██ ░▓█▄   ▌░██░  ▒██ █░░░██░▓██▒  ▐▌██▒░▓█ ░██ ░██▄▄▄▄██ 
 ▓█   ▓██▒░▒████▓ ░██░   ▒▀█░  ░██░▒██░   ▓██░░▓█▒░██▓ ▓█   ▓██▒
 ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓     ░ ▐░  ░▓  ░ ▒░   ▒ ▒  ▒ ░░▒░▒ ▒▒   ▓▒█░
  ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░   ░ ░░   ▒ ░░ ░░   ░ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░
  ░   ▒    ░ ░  ░  ▒ ░     ░░   ▒ ░   ░   ░ ░  ░  ░░ ░  ░   ▒   
      ░  ░   ░     ░        ░   ░           ░  ░  ░  ░      ░  ░
           ░               ░                                    ''')
           
	print('Obg por usar!! ;)')
	time.sleep(4)
	os.system("cls" if os.name == "nt" else "clear")
	exit()
###################################	
if temas == (3):
	os.system("cls" if os.name == "nt" else "clear")
	print(f'{preto}=== Geografia ===')
	print(f'''{vermelho}
	
1) Vaticano e Rússia

2) Nauru e China

3) Mônaco e Canadá

4) Malta e Estados Unidos

5) São Marino e Índia
	
	{vermelho}''')
	gs1 = int(input(f'{preto}Quais o menor e o maior país do mundo?: '))
	if gs1 == (1):
		print('Acertou!!!')
		print('Proxima, faltam mais 3 perguntas')
		time.sleep (3)
	else:
		print('Errou, era a 1')
		exit()

###################################

###################################	
if temas == (3):
	os.system("cls" if os.name == "nt" else "clear")
	print(f'{preto}=== Geografia ===')
	print(f'''{azul}
	
1) Pico da Neblina

2) Pico Paraná

3) Monte Roraima

4) Pico Maior de Friburgo

5) Pico da Bandeira
	
	{azul}''')
	gs1 = int(input(f'{preto}Qual a montanha mais alta do Brasil?: '))
	if gs1 == (1):
		print('Acertou!!!')
		print('Proxima, faltam mais 2 perguntas')
		time.sleep (3)
	else:
		print('Errou, era a 1')
		exit()

###################################

###################################	
if temas == (3):
	os.system("cls" if os.name == "nt" else "clear")
	print(f'{preto}=== Geografia ===')
	print(f'''{verde}
	
1) Índia

2) Filipinas

3) Moçambique

4) Macau

5) Portugal
	
	{verde}''')
	gs1 = int(input(f'{preto}Em qual local da Ásia o português é língua oficial?: '))
	if gs1 == (3):
		print('Acertou!!!')
		print('Proxima, falta apenas 1 pergunta ')
		time.sleep (3)
	else:
		print('Errou, era a 4')
		exit()

###################################

###################################	
if temas == (3):
	os.system("cls" if os.name == "nt" else "clear")
	print(f'{preto}=== Geografia ===')
	print(f'''{azul}
	
1) Rússia

2) Filipinas

3) Istambul

4) Groenlândia

5) Tanzânia
	
	{azul}''')
	gs1 = int(input(f'{preto}Qual destes países é transcontinental?: '))
	if gs1 == (1):
		print('Acertou!!!')
		time.sleep (2)
	else:
		print('Errou, era a 4')
		exit()

	os.system("cls" if os.name == "nt" else "clear")
	print(''' ▄▄▄      ▓█████▄  ██▓ ██▒   █▓ ██▓ ███▄    █  ██░ ██  ▄▄▄      
▒████▄    ▒██▀ ██▌▓██▒▓██░   █▒▓██▒ ██ ▀█   █ ▓██░ ██▒▒████▄    
▒██  ▀█▄  ░██   █▌▒██▒ ▓██  █▒░▒██▒▓██  ▀█ ██▒▒██▀▀██░▒██  ▀█▄  
░██▄▄▄▄██ ░▓█▄   ▌░██░  ▒██ █░░░██░▓██▒  ▐▌██▒░▓█ ░██ ░██▄▄▄▄██ 
 ▓█   ▓██▒░▒████▓ ░██░   ▒▀█░  ░██░▒██░   ▓██░░▓█▒░██▓ ▓█   ▓██▒
 ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓     ░ ▐░  ░▓  ░ ▒░   ▒ ▒  ▒ ░░▒░▒ ▒▒   ▓▒█░
  ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░   ░ ░░   ▒ ░░ ░░   ░ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░
  ░   ▒    ░ ░  ░  ▒ ░     ░░   ▒ ░   ░   ░ ░  ░  ░░ ░  ░   ▒   
      ░  ░   ░     ░        ░   ░           ░  ░  ░  ░      ░  ░
           ░               ░                                    ''')
           
	print('Obg por usar!! ;)')
	time.sleep(4)
	os.system("cls" if os.name == "nt" else "clear")
	exit()

###################################