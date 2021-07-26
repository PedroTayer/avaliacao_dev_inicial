import heapq
import os
import sys

from funcoes_argumentos import organizar_input_garrafas, verificar_argumentos, lista_para_args
from funcoes_inputs import main as coletar_inputs


# Função para parar os prints
def parar_prints():
	sys.stdout = open(os.devnull, 'w')


# Função para reativar os prints
def ativar_prints():
	sys.stdout = sys.__stdout__


# Função principal
def main(**kwargs):
	'''
	Função principal para calcular as garrafas.
	Complexidade de tempo: O(nlogn), pois utilizou-se heap
	Pode ser rodado passando argumentos ou inserindo pelo prompt (ver readme)

	:param kwargs:
	galao: litros no galao (float), ex: galao=5.6
	garrafas: litros em cada garrafa separados por virgula (string), ex: garrafas='2,6,4.6'
	printar: se passado, printa o passo a passo, ex: printar
	exemplo:
	main galao=5.6 garrafas='2,6,4.6' printar

	:return:
	flag: se foi possível fazer o cálculo (bool)
	volumes_ordenados: lista com as garrafas utilizadas, na ordem que foram passadas (lista de strings), ex: ['4.5L', '0.4L']
	sobra: sobra (float)
	'''

	# Se não é para printar, desativar prints
	if not kwargs['printar']:
		parar_prints()

	# Constantes de print
	separador = 45 * '#'
	W = '\033[0m'  # Cor branca
	B = '\033[34m'  # Cor azul
	G = '\033[32m'  # Cor verde
	R = '\033[31m'  # Cor vermelha

	# Se não for passado nenhum input, coletar inputs pelo prompt
	if len(kwargs) == 1:
		# O(n)
		flag, galao, garrafas_dict, heap_garrafas = coletar_inputs()
		# Se algum erro, retornar flag False
		if not flag:
			ativar_prints()
			return False, [], -1

	# Se for passado algum input, verificar e organizar argumentos
	else:
		# O(n)
		# Verificar se os inputs estão no formato certo
		flag, galao, garrafas = verificar_argumentos(**kwargs)
		# Se algum erro, retornar flag False
		if not flag:
			ativar_prints()
			return False, [], -1
		# Criar dicionário de garrafas e a heap
		garrafas_dict, heap_garrafas = organizar_input_garrafas(garrafas)

	# galao: capacidade do galão (float)
	# garrafas_dict: dicionário de garrafas no formato: {1: 4.0, 2: 8.9} {número da garrafa: capacidade}
	# heap_garrafas: heap com as garrafas: [-8.9, 4.0]	# Print dos dados inseridos para verificação

	# printar dados inseridos
	print(B + f'{separador}\nDados inseridos:')
	print(f'Galão com {galao} litros.')
	print(f'{len(garrafas_dict)} garrafas:')
	[print(f'Garrafa {ind}: {val} litros.') for ind, val in garrafas_dict.items()]
	print(f'{separador}' + W + '\nInício dos cálculos...')

	# Criação da lista de garrafas e do dicionário de ordem
	# Serão utilizados para mapear os volumes selecionados com a ordem que foram passadas
	# Isso é necessário pois o print está na ordem que as garrafas foram passadas
	garrafas_lista = []
	dict_ordem = {}

	# Tempo: O(n)
	for key, val in garrafas_dict.items():
		garrafas_lista.append(val)
		if val in dict_ordem:
			dict_ordem[val].append(key)
		else:
			dict_ordem[val] = [key]

	# Total de litros, se houver menos litros nas garrafas do que a capacidade do galão, retornar Falso
	total_litros = sum(garrafas_lista)
	if total_litros < galao:
		print(
			R + f'As garrafas possuem {round(total_litros, 5)} litros, não é possível encher o galão de {round(galao, 5)} litros, abortando..' + W)
		return False, [], -1

	##### INÍCIO DOS CÁLCULOS ####

	# Vetor que recebe as garrafas escolhidas (volume delas)
	escolhidas_volume = []

	# Inicialização de variáveis
	# Espaço vazio é o que ainda tem de espaço no galao
	espaco_vazio = galao
	# Sobra é quanto sobra, garrafa é o volume da garrafa a ser iterada
	sobra, garrafa = 0, 0
	# Flag para saber se o galão está cheio
	acabou = False

	# LÓGICA:
	# Queremos montar o vetor escolhidas_volume que receberá os volumes das garrafas utilizadas
	# Com a heap, as garrafas já estão ordenadas de forma descendente
	# Da maior para a menor, tentamos:
	# Adicionar a garrafa no galão se ela for menor que o espaço vazio no galão
	# Se o espaco vazio for 0, o galão está cheio, fim
	# Se não, tentamos a próxima garrafa, até a última garrafa
	# O(n log n) pois devemos reordenar a heap após cada remoção
	while len(heap_garrafas) > 0 and not acabou:
		garrafa_anterior = garrafa
		garrafa = -heapq.heappop(heap_garrafas)

		print(f'Galão ainda tem {espaco_vazio} litros de espaço, avaliando garrafa com {garrafa} litros')

		if espaco_vazio >= garrafa:
			print(f'Garrafa de {garrafa} litros cabe dentro do galão')
			espaco_vazio = round(espaco_vazio - garrafa, 5)
			print(f'Agora galão tem {espaco_vazio} litros de espaço')
			escolhidas_volume.append(garrafa)

		if espaco_vazio == 0:
			print(G + f'Sucesso!! Galão completamente cheio!!' + W)
			acabou = True

	# Se as garrafas 'acabarem' e ainda estiver espaço no galão, completamos com a menor e teremos sobra
	if not acabou:
		print(f'Acabaram as garrafas, ainda tem {espaco_vazio} litros de espaço')
		print(f'Usaremos a última garrafa')
		escolhidas_volume.append(garrafa)
		sobra = round(garrafa - espaco_vazio, 5)
		print(
			f'Utilizamos a garrafa de {garrafa} litros para completar o espaço de {espaco_vazio}, sobrando {sobra} litros.')
		print(G + f'Sucesso!! Galão completamente cheio!!' + W)

	# Processo para printar os valores na ordem que foram passados
	ordem = []
	# Criar um vetor para receber a ordem das garrafas
	for l in escolhidas_volume:
		ordem.append(float(dict_ordem[l][0]))
		dict_ordem[l].pop(0)

	# Ordenar as escolhidas (previamente ordenadas em volume) com relação ao vetor ordem (ordenados pela ordem)
	# O(1)
	lista_zipada = zip(ordem, escolhidas_volume)
	# O(k log k)
	lista_zipada_ordenada = sorted(lista_zipada)
	# O(k)
	volumes_ordenados = [f'{element}L' for _, element in lista_zipada_ordenada]

	# Reativar prints
	ativar_prints()

	# Printar respostas
	print(f'Resposta: {volumes_ordenados}, sobra {sobra}L;')

	# Retornar
	return True, volumes_ordenados, sobra


if __name__ == '__main__':
	print(f'Bem vindo ao programa para otimização de garrafas!')
	lista_args = sys.argv[1:]
	if len(lista_args) == 0:
		main(printar=True)
	else:
		flag, dict_args = lista_para_args(lista_args)
		if flag:
			main(**dict_args)
