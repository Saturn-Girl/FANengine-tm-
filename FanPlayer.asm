[BITS 64]

section .data
    index dq 4
    pointer dq 16

section .bss
    buffer resb 24
    array resb 32

section .text
    global _Init
    global PragramaOnce

_Init:
    mov rax,[index]
    mov rdi,[pointer]
    mov rcx,rax

    push rax
    push rdi
    push rcx 

    add rax,rdi
    add rax,rcx

    mov byte [buffer],32
    mov byte [array],42

PragramaOnce:

    mov rax,60
    mov rdi,rax
    push rax
    add rax,rdi