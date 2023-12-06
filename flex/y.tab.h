/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    START = 258,                   /* START  */
    NUMBER = 259,                  /* NUMBER  */
    RNUMBER = 260,                 /* RNUMBER  */
    TYPE = 261,                    /* TYPE  */
    STRUCT_TYPE = 262,             /* STRUCT_TYPE  */
    FOR = 263,                     /* FOR  */
    IF = 264,                      /* IF  */
    CODE_BLOCK = 265,              /* CODE_BLOCK  */
    INPUT = 266,                   /* INPUT  */
    OUTPUT = 267,                  /* OUTPUT  */
    ENDLINE = 268,                 /* ENDLINE  */
    MATH_OP = 269,                 /* MATH_OP  */
    LOGIC_OP = 270,                /* LOGIC_OP  */
    LCURLY = 271,                  /* LCURLY  */
    RCURLY = 272,                  /* RCURLY  */
    POINT_COMMA = 273,             /* POINT_COMMA  */
    LBRACE = 274,                  /* LBRACE  */
    RBRACE = 275,                  /* RBRACE  */
    COMMA = 276,                   /* COMMA  */
    INPUT_SEP = 277,               /* INPUT_SEP  */
    OUTPUT_SEP = 278,              /* OUTPUT_SEP  */
    ID = 279,                      /* ID  */
    ATTR = 280                     /* ATTR  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define START 258
#define NUMBER 259
#define RNUMBER 260
#define TYPE 261
#define STRUCT_TYPE 262
#define FOR 263
#define IF 264
#define CODE_BLOCK 265
#define INPUT 266
#define OUTPUT 267
#define ENDLINE 268
#define MATH_OP 269
#define LOGIC_OP 270
#define LCURLY 271
#define RCURLY 272
#define POINT_COMMA 273
#define LBRACE 274
#define RBRACE 275
#define COMMA 276
#define INPUT_SEP 277
#define OUTPUT_SEP 278
#define ID 279
#define ATTR 280

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 18 "../yacc/mlpSpec.y"
 
    char* f; 

#line 121 "y.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
