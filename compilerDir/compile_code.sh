#!/bin/bash
nasm -f elf32 asmCode.asm -o asm
ld -m elf_i386 -o programel asm -lc -dynamic-linker /lib/ld-linux.so.2
