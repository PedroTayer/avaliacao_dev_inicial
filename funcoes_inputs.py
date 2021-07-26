import heapq

def verificar_numero(valor_str, pode_float=True):
	'''

	:param valor_str: valor do input
	:param pode_float: flag para informar se pode ser float, ex: número de garrafas não pode ser float, tem q ser inteiro
	:return: valor_num: valor do input em valor numérico
	'''
	R = '\033[31m'
	W = '\033[0m'
	print(f'Valor inserido: {valor_str}')
	try:
		if pode_float:
			valor_num = float(valor_str)
		else:
			valor_num = int(valor_str)
		if valor_num < 0:
			print('Valor negativo inserido. Favor inserir valor positivo.')
			return -1
		return valor_num

	except ValueError:
		if pode_float:
			print(R + 'Valor não numérico! Favor inserir valor numérico, separador decimal é ".", exemplo: 5.8' + W)
		else:
			print(R + 'Número não inteiro! Favor inserir número inteiro, exemplo: 5.' + W)
		return -1


def coletar_input(texto, pode_float=True):
	'''

	:param texto: texto para ser mostrado no prompt
	:param pode_float: flag para informar se pode ser float, ex: número de garrafas não pode ser float, tem q ser inteiro
	:return: valor numérico do input
	'''
	valor_str = input(f'{texto}')
	valor = verificar_numero(valor_str, pode_float)

	if valor == -1:
		return coletar_input(texto, pode_float)
	else:
		return valor


def main():
	'''
	Função para coletar todos os inputs
	:return:
	galao: capacidade do galão
	garrafas_dict: dicionário de garrafas no formato: {1: 4.0, 2: 8.9} {número da garrafa: capacidade}
	heap_garrafas: heap com as garrafas: [-8.9, 4.0]
	'''
	R = '\033[31m'
	G = '\033[32m'
	W = '\033[0m'
	B = '\033[94m'
	separador = 45 * '#'

	print(f'\nDigite 0 para sair a qualquer momento.\n{separador}')

	galao = coletar_input('Insira o volume do galão (em litros): ', pode_float=True)

	if galao == 0:
		print('0 inserido.. Obrigado por utilizar o programa!!')
		return False, 0, {}, []

	qtd_garrafas = coletar_input('Insira a quantidade de garrafas: ', pode_float=False)

	if qtd_garrafas == 0:
		print('0 inserido.. Obrigado por utilizar o programa!!')
		return False, 0, {}, []

	# Criação da heap
	# O(n)
	garrafas_dict = {}
	heap_garrafas = []
	for garrafa in range(1, qtd_garrafas + 1):
		garrafas_dict[garrafa] = coletar_input(f'Insira a quantidade na garrafas {garrafa}: ', pode_float=True)
		if garrafas_dict[garrafa] == 0:
			print('0 inserido.. Obrigado por utilizar o programa!!')
			return False, 0, {}, []
		heapq.heappush(heap_garrafas, -garrafas_dict[garrafa])

	return True, galao, garrafas_dict, heap_garrafas
