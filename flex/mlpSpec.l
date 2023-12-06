
%{
#include <math.h>
#include <string.h>
#include "y.tab.h"
int lineNr = 0;

%}

DIGIT             [0-9]
NON_ZERO_DIGIT    [1-9]
ID                ([A-Za-z][a-zA-Z0-9_]*)("."[A-Za-z][a-zA-Z0-9_]*)?
START             [ ]*"#"[ ]*"include"[ ]*"<iostream>"

%%

{START} {
	char p[100];
	strcpy(p, yytext);
	yylval.f = p;
	printf("start detected\n");
	return START;
}

"0"|{NON_ZERO_DIGIT}{DIGIT}? {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p;
	return NUMBER;
}

{DIGIT}+"."{DIGIT}* {
        char p[100];
	strcpy(p, yytext);

	yylval.f = p;
        return RNUMBER;
}

"int"|"float"|"char" {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p;
	return TYPE;
}

"struct pereche" {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p;
	return STRUCT_TYPE;
}

"for" {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p; 
	return FOR;
}

"if" {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p; 
	return IF;
	
}

"int main" {

	char p[100];
	strcpy(p, yytext);

	yylval.f = p; 
	return CODE_BLOCK;
}
"std::cin" {

	char p[100];
	strcpy(p, yytext);

	yylval.f = p;
	return INPUT;
}

"std::cout" {

	char p[100];
	strcpy(p, yytext);

	yylval.f = p;
	return OUTPUT;
}

"'\\n'" {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p;
	return ENDLINE;
}

"+"|"-"|"/"|"%"|"*" {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p;
	return MATH_OP;

}

"=="|"!="|"<="|">="|"&&"|"||"|">"|"<" {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p;
	return LOGIC_OP;

}

"=" {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p;
	return ATTR;
}

"{" { return LCURLY; }
"}" { return RCURLY; }
";" { return POINT_COMMA; }
"(" { return LBRACE; }
")" { return RBRACE; }
"," { return COMMA; }
"<<" { return OUTPUT_SEP; }
">>" { return INPUT_SEP; }

{ID}      {
	char p[100];
	strcpy(p, yytext);

	yylval.f = p;

	if(strlen(yytext) <=8){
		return ID;
	}else{
		printf("Error on line %d: variable name %s is too long\n", lineNr, yytext);

	}

}
[\n]      ++lineNr;

[ \t]+

. printf("Not recognized: %s\n", yytext);

%%

int yywrap (){return -1;}
