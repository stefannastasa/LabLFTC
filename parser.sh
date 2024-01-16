#!/bin/bash

flex lexer.l
yacc -dv parser.y
gcc -o compiler lex.yy.c y.tab.c
./compiler code.in
