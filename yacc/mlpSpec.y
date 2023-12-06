%{

    #include <stdio.h> 
    #include <string.h>    
    #include <stdlib.h> 
    extern int yylex(void); 
    extern FILE* yyin;
    extern int lineNr; // Add yylineno declaration

    void yyerror(char *msg); 
    int  flag; 
     
    int i; 
    int n=0;

%}

%union { 
    char* f; 
} 
%token<f> START;
%token<f> NUMBER;
%token<f> RNUMBER;
%token<f> TYPE;
%token<f> STRUCT_TYPE;
%token<f> FOR;
%token<f> IF;
%token<f> CODE_BLOCK;
%token<f> INPUT;
%token<f> OUTPUT;
%token<f> ENDLINE;
%token<f> MATH_OP;
%token<f> LOGIC_OP;
%token<f> LCURLY;
%token<f> RCURLY;
%token<f> POINT_COMMA;
%token<f> LBRACE;
%token<f> RBRACE;
%token<f> COMMA;
%token<f> INPUT_SEP;
%token<f> OUTPUT_SEP;
%token<f> ID;
%token<f> ATTR;

%%

Program: program YYEOF { printf("Syntax is correct!\n"); }

program: START lista_declaratii program_code {printf("Checking...\n");}
       
lista_declaratii: declaratie POINT_COMMA lista_declaratii
        | decl_struct POINT_COMMA lista_declaratii
		| declaratie POINT_COMMA
        | decl_struct POINT_COMMA

declaratie: TYPE id_list 

decl_struct: STRUCT_TYPE LCURLY lista_declaratii RCURLY ID

id_list: id_list COMMA ID 
        | ID
        | error {fprintf(stderr, "Syntax error at line %d\n", lineNr);}

program_code: CODE_BLOCK LBRACE RBRACE LCURLY lista_instructiuni RCURLY 

lista_instructiuni: instructiune lista_instructiuni 
	    | instructiune

instructiune: declaratie POINT_COMMA | atribuire POINT_COMMA | decizie | repetitie | citire POINT_COMMA | scriere POINT_COMMA

atribuire: ID ATTR expresie 

expresie: ID | NUMBER| RNUMBER 
        | ID lista_operatii 
        | NUMBER lista_operatii
        | RNUMBER lista_operatii
lista_operatii: operatie lista_operatii
              | operatie
              

operatie: MATH_OP ID | MATH_OP NUMBER | MATH_OP RNUMBER 

decizie: IF LBRACE expresie_logica RBRACE LCURLY lista_instructiuni RCURLY

expresie_logica: ID | NUMBER| RNUMBER
                | ID lista_operatii_logice 
                | NUMBER lista_operatii_logice
                | RNUMBER lista_operatii_logice
lista_operatii_logice: operatie_logica lista_operatii_logice
                      | operatie_logica
operatie_logica: LOGIC_OP ID 
               | LOGIC_OP NUMBER
               | LOGIC_OP RNUMBER

repetitie: FOR LBRACE atribuire POINT_COMMA expresie_logica POINT_COMMA atribuire RBRACE LCURLY lista_instructiuni RCURLY

citire: INPUT INPUT_SEP ID 
scriere: OUTPUT OUTPUT_SEP ID OUTPUT_SEP ENDLINE 

%%


void yyerror(char *s) {
	fprintf(stderr, "%s on line %d\n", s, lineNr + 1);
	exit(1);
}
int main(int argc, char *argv[]) {
    FILE *file;

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    yyin = file; // Set the input file for Lex/Flex

    yyparse();

    fclose(file);

    return 0;
}

