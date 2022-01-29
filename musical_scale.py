#!/usr/bin/python
# 2022 by Willian Ferreira
# Reference: https://github.com/grimmdude/Scale-Generator/blob/master/scale_generator.py 

from ast import arg
import sys, os 
import itertools


def main():

    try:

        args = sys.argv[1:]
        if not args:
            print("Você deve informar a nota a ser gerada a escala. Utilize o --help ou -h para maiores informações.")
            sys.exit(1)

        if args[0] in ["--menor"] and  args[1] in ["C", "D", "E", "F", "G", "A", "B"]:
            print("Escala de {} Menor".format(args[1]))
            sys.exit(1)
        
        elif args[0] in ["--maior"] and args[1] in ["C", "D", "E", "F", "G", "A", "B"]:
            print("Escala de {} Maior".format(args[1]))
            sys.exit(1)
        else:
            print("Informação inválida. Utilize o --help ou -h para maiores informações.")
            sys.exit(1)
    except Exception as e:
        print("Erro inesperado identificado. Favor contatar o admonistrador. Erro: {}".format(e))
        sys.exit(1)
    
if __name__ == '__main__':
	main()