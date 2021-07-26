import heapq
import os
import sys

from funcoes_argumentos import organizar_input_garrafas, verificar_argumentos, lista_para_args
from funcoes_inputs import main as coletar_inputs

# todo comentar tudo
# todo mais testes
# todo documentação (prints)

# Disable
def parar_prints():
	sys.stdout = open(os.devnull, 'w')


# Restore
def ativar_prints():
	sys.stdout = sys.__stdout__


def main(**kwargs):
	if not kwargs['printar']:
		parar_prints()

	separador = 45 * '#'
	W = '\033[0m'
	B = '\033[34m'
	G = '\033[32m'
	R = '\033[31m'

	if len(kwargs) == 0:
		flag, galao, garrafas_dict, heap_garrafas = coletar_inputs()
	else:
		flag, galao, garrafas = verificar_argumentos(**kwargs)
		if not flag:
			ativar_prints()
			return False, [], -1
		garrafas_dict, heap_garrafas = organizar_input_garrafas(garrafas)

	if not flag:
		ativar_prints()
		return False, [], -1

	print(B + f'{separador}\nDados inseridos:')
	print(f'Galão com {galao} litros.')
	print(f'{len(garrafas_dict)} garrafas:')
	[print(f'Garrafa {ind}: {val} litros.') for ind, val in garrafas_dict.items()]
	print(f'{separador}' + W + '\nInício dos cálculos...')

	garrafas_lista = []
	dict_ordem = {}
	for key, val in garrafas_dict.items():
		garrafas_lista.append(val)
		if val in dict_ordem:
			dict_ordem[val].append(key)
		else:
			dict_ordem[val] = [key]

	total_litros = sum(garrafas_lista)
	if total_litros < galao:
		print(
			R + f'As garrafas possuem {round(total_litros, 5)} litros, não é possível encher o galão de {round(galao, 5)} litros, abortando..' + W)
		return False, [], -1

	escolhidas_volume = []

	# Começamos pela maior garrafa
	espaco_vazio = galao
	sobra, garrafa = 0, 0
	acabou = False

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

	if not acabou:
		print(f'Acabaram as garrafas, ainda tem {espaco_vazio} litros de espaço')
		if garrafa >= espaco_vazio:
			print(f'Usaremos a última garrafa')
			escolhidas_volume.append(garrafa)
			sobra = round(garrafa - espaco_vazio, 5)
			print(
				f'Utilizamos a garrafa de {garrafa} litros para completar o espaço de {espaco_vazio}, sobrando {sobra} litros.')
			print(G + f'Sucesso!! Galão completamente cheio!!' + W)

		else:
			print(
				f'A última garrafa é menor que o espaço no galão, utilizaremos ela inteira mais uma parte da penúltima')
			espaco_vazio = round(espaco_vazio - garrafa, 5)
			print(f'Adicionando a garrafa menor ({garrafa} litros) ainda sobram {espaco_vazio} de espaço no galão.')
			escolhidas_volume.append(garrafa_anterior)
			sobra = round(garrafa_anterior - espaco_vazio, 5)
			print(
				f'Utilizamos a garrafa de {garrafa_anterior} litros para completar o espaço de {espaco_vazio}, sobrando {sobra} litros.')
			print(G + f'Sucesso!! Galão completamente cheio!!' + W)

	ordem = []
	for l in escolhidas_volume:
		ordem.append(float(dict_ordem[l][0]))
		dict_ordem[l].pop(0)

	lista_zipada = zip(ordem, escolhidas_volume)
	lista_zipada_ordenada = sorted(lista_zipada)
	volumes_ordenados = [f'{element}L' for _, element in lista_zipada_ordenada]

	ativar_prints()
	print(f'Resposta: {volumes_ordenados}, sobra {sobra}L;')

	return True, volumes_ordenados, sobra


if __name__ == '__main__':
	print(f'Bem vindo ao programa para otimização de garrafas!')
	lista_args = sys.argv[1:]
	flag, dict_args = lista_para_args(lista_args)
	if flag:
		main(**dict_args)
