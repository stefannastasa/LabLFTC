
%{
#include <math.h>
int lineNr = 0;

%}

DIGIT             [0-9]
NON_ZERO_DIGIT    [1-9]
ID                ([A-Za-z][a-zA-Z0-9_]*)("."[A-Za-z][a-zA-Z0-9_]*)?
START             [ ]*"#"[ ]*"include"[ ]*"<iostream>"
%%

{START} {
  printf("1|%s\n", yytext);

}

"0"|{NON_ZERO_DIGIT}{DIGIT}? {

    printf("2|%d\n", atoi(yytext));
}

{DIGIT}+"."{DIGIT}* {

    printf("2|%g\n", atof(yytext));
}


int|float|"struct pereche"|for|if|main|std::cin|std::cout|"'\\n'"  {
    printf("1|%s\n", yytext);
}

"+"|"-"|"/"|"%"|"*"|"=="|"!="|"<="|">="|"="|"&&"|"||"|">"|"<" {

    printf("1|%s\n", yytext);
}

"{"|"}"|";"|"("|")"|","|"<<"|">>" {

    printf("1|%s\n", yytext);
}


{ID}      printf("3|%s\n", yytext);

[\n]      ++lineNr;

[ \t]+

. printf("Not recognized: %s\n", yytext);

%%

int main(argc, argv)
int argc;
char** argv;
{
  --argc; ++argv;
  if(argc > 0){
    yyin = fopen(argv[0], "r");

  }else{
    yyin = stdin;

  }
  yylex();
}

