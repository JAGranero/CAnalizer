import sys
from antlr4 import *
from GrammarCLexer import GrammarCLexer
from GrammarCParser import GrammarCParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarCParser(stream)
    tree = parser.compilationUnit()


if __name__ == '__main__':
    main(sys.argv)
