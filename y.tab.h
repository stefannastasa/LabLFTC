#ifndef _yy_defines_h_
#define _yy_defines_h_

#define INCLUDE 257
#define NAMESPACE 258
#define ISTREAM 259
#define OSTREAM 260
#define DATA_TYPE 261
#define PLUS 262
#define MINUS 263
#define OR 264
#define DIVIDE 265
#define ASSIGN 266
#define COMMA 267
#define SEMICOLON 268
#define LAQ 269
#define RAQ 270
#define SIN 271
#define SOUT 272
#define LPR 273
#define RPR 274
#define MAIN 275
#define RETURN 276
#define ID 277
#define CONST 278
#ifdef YYSTYPE
#undef  YYSTYPE_IS_DECLARED
#define YYSTYPE_IS_DECLARED 1
#endif
#ifndef YYSTYPE_IS_DECLARED
#define YYSTYPE_IS_DECLARED 1
typedef union YYSTYPE {
	char * value;
} YYSTYPE;
#endif /* !YYSTYPE_IS_DECLARED */
extern YYSTYPE yylval;

#endif /* _yy_defines_h_ */
