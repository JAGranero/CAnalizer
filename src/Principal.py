import sys
import os
from antlr4 import *
from GrammarCLexer import GrammarCLexer
from GrammarCParser import GrammarCParser
#sys.stdout = open('OutPut.txt', 'w')

def main(argv):

    # Crear para la salida del parser
    #file = open("myOutFile.txt", "w")
    #sys.stdout = open('OutPut.txt', 'w')

    # print(argv[1])

    for nombre_directorio, dirs, ficheros in os.walk(argv[1]):
        print(nombre_directorio)
        for nombre_fichero in ficheros:
            if nombre_fichero.endswith(".c"):
                print("   "+nombre_fichero)
                try:
                    input_stream = FileStream(nombre_directorio+"\\"+nombre_fichero)
                    lexer = GrammarCLexer(input_stream)
                    stream = CommonTokenStream(lexer)
                    parser = GrammarCParser(stream)
                    tree = parser.compilationUnit()
                    #print(tree.toStringTree(parser))

                except:
                    print("error en file -> "+nombre_directorio+"\\"+nombre_fichero)

    #file.close()

    # input_stream = FileStream(argv[1])
    # lexer = GrammarCLexer(input_stream)
    # stream = CommonTokenStream(lexer)
    # parser = GrammarCParser(stream)
    # tree = parser.compilationUnit()

if __name__ == '__main__':
    main(sys.argv)
