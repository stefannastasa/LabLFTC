section .data
	 sum times 4 db 0
	 b times 4 db 0
	 a times 4 db 0
	 format db "%d", 0
section .text
	global _start
	extern exit

	extern scanf 

	extern printf 


_start:
	push dword a
	push dword format
	
	call scanf
	add ESP, 4 * 2

	push dword b
	push dword format
	
	call scanf
	add ESP, 4 * 2

	mov AL, [a]
	add AL, byte [b]
	mov [sum], AL

	push dword [sum]
	push dword format
	call printf
	add ESP, 4 * 2

	push dword 0
	call exit
