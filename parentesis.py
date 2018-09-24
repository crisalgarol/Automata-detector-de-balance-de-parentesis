#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import subprocess
import platform
import random
from Tkinter import * #Para evitar el main

def expand(letra, next_symbol):

	if(next_symbol != '(' and next_symbol != ')'):
		return "*"

	if(letra == 'B'):
		if(next_symbol == '('):
			return "(RB"
		else: #Checar esto
			return "^"

	elif(letra == 'R'):
		if(next_symbol == ')'):
			return ")"
		elif(next_symbol == '('):
			return "(RR"

def generar_cadena():

	cad = []
	a = '('
	b = ')'

	for i in range(0, (random.randint(2,15))):

		if(random.randint(0,1)):
			cad.append('(')
		else:
			cad.append(')')

	return str((''.join(cad)))


def evaluar(cadena):


	if(cadena == "" or (cadena[0] != "(" and cadena[0] != ")")):
		print("Cadena no valida")
		return

	archivo = open("Historial.txt", "w")

	tam = len(cadena)
	balanceado = False

	print("\nLa cadena ingresada es: " + cadena)
	print("\n\nLa evaluacion es: \n")
	archivo.write("La cadena ingresada es: " + cadena)
	archivo.write("\n\nLa evaluacion es: \n\n" )

#------------------------------------------------------------------------

	evaluacion = cadena[0]
	j = "B"
	pos_ev = 0
	balanceado = False

	print(j)
	archivo.write(str(j)+ "\n")

	for i in range (0, tam):
		
		c = 0
		expanding = expand(j, cadena[i])
		aux = evaluacion

		if(expanding == '*'):
					derivation_letters = ""
					break

		elif(expanding == '^'):
			derivation_letters = ""
			print("Se interrumpió el proceso.")
			archivo.write("Se interrumpió el proceso")
			break;
		
		if(pos_ev != 0):

			aux = evaluacion[0:(pos_ev)] + expanding + evaluacion[(pos_ev+1):len(evaluacion)]
			evaluacion = aux
			
			c = 0

			for k in evaluacion:

				if(k == "R" or k == "B"):

					if(k == "B" and c == len(evaluacion)-1 and i == len(cadena)-1):
						aux = evaluacion
						aux = evaluacion[0:len(evaluacion)-1]
						evaluacion = aux
						balanceado = True
						break
				
					pos_ev = c
					j = evaluacion[c]
					break


				c+=1


		else:
			evaluacion = expanding
			pos_ev = 1
			j = "R"

		print("Regla: \"" + expanding  + "\" ---> " + evaluacion + "\n")
		archivo.write("Regla: \"" + expanding  + "\" ---> " + evaluacion + "\n")

		if(balanceado):
			break




	if(balanceado):
		archivo.write(evaluacion)
		archivo.write("\n\nLos paréntesis están balanceados")
		print("\nLos paréntesis estan balanceados")

	elif (expanding == '*'):
		print("Cadena no valida")

	else:
		print("\nLos paréntesis NO están balanceados")
		archivo.write(evaluacion)
		archivo.write("\n\nLos paréntesis NO están balanceados\n")
		archivo.write(cadena)

	archivo.close()

def main():
	

	while(True):

		os.system('clear')

		print("		---PROGRAMA DE BALANCEO DE PARÉNTESIS---\n")
		print("\n1) Generar cadena aleatoria y evaluar")
		print("2) Ingresar una cadena")
		print("3) Leer desde archivo")
		print("4) Salir")
		opc = raw_input("--->")


		if(opc == "1"):
			cadena = generar_cadena()
			print("La cadena generada es: " + cadena + "\n\n")
			os.system('clear')
			evaluar(generar_cadena())
			raw_input()

		elif(opc == "2"):
			cadena = raw_input("Ingresa una cadena: ")
			os.system('clear')
			evaluar(cadena)
			raw_input()

		elif (opc == "3"):
			file_name = raw_input("Ingresa el nombre del archivo, no olvides poner la extensión: ")

			try:
				file = open(file_name, "r")
			except:
				raw_input("\nArchivo no encontrado")
				continue

			cadena = file.readline()
			evaluar(cadena)
			raw_input()


		elif (opc == "4"):
			break;

		else:
			raw_input("Opción no valida, inténtelo de nuevo")
			cadena = raw_input("--->")

main()