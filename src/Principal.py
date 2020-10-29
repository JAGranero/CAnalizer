import sys
import os
from antlr4 import *
from GrammarCLexer import GrammarCLexer
from GrammarCParser import GrammarCParser


def main(argv):

    # Crear para la salida del parser
    file = open("myOutFile.txt", "w")

    # print(argv[1])

    for nombre_directorio, dirs, ficheros in os.walk(argv[1]):
        file.write(nombre_directorio)
        file.write("\n")
        for nombre_fichero in ficheros:
            file.write("   ")
            file.write(nombre_fichero)
            file.write("\n")
            if nombre_fichero.endswith(".c"):
                file.write("             -->Entre\n")
                input_stream = FileStream(nombre_directorio+"\\"+nombre_fichero)
                lexer = GrammarCLexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = GrammarCParser(stream)
                tree = parser.compilationUnit()
                file.write("             -->Paso\n")

    file.close()

    # input_stream = FileStream(argv[1])
    # lexer = GrammarCLexer(input_stream)
    # stream = CommonTokenStream(lexer)
    # parser = GrammarCParser(stream)
    # tree = parser.compilationUnit()

if __name__ == '__main__':
    main(sys.argv)
