#!/bin/bash
yacc -d parser.y
gcc -o compiler lex.yy.c y.tab.c
./compiler test_program.mpl ;