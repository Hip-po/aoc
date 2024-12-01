section .bss
    num resb 5
    num_list resb 5001  ; 1000 numbers, each 5 bytes
    list_index resd 1

section .data
    newline db 10, 0

section .text
    global _start

_start:
    ; Initialize list index
    mov dword [list_index], 0

main_loop:
    ; Read a line from stdin
    call _read_line

    ; Check for end of input (empty line)
    cmp byte [num], 0
    je _print_list

    ; Check for end of input (newline)
    cmp byte [num], 10
    je _print_list

    ; Add number to list
    call _add_to_list

    ; Loop
    jmp main_loop

_exit:
    ; Exit
    mov eax, 1          ; sys_exit
    xor ebx, ebx        ; exit code 0
    int 0x80            ; call kernel

_print_list:
    ; Initialize list index
    mov ecx, 0
    jmp print_loop

print_loop:
    ; Check if we have printed all numbers
    cmp ecx, [list_index]
    jge _exit

    ; ; Print the current index
    ; mov eax, ecx
    ; add eax, '0'
    ; mov [num], eax
    ; call _print_num

    ; Calculate address of the current number
    lea esi, [num_list + ecx * 5]

    ; Copy the number to num
    mov edi, num
    mov ecx, 5
    rep movsb

    ; Print the number
    call _print_num

    ; Increment list index
    inc ecx

    ; Loop
    jmp print_loop

_print_num:
    ; Print the number
    mov esi, 4          ; sys_write
    mov edi, 1          ; file descriptor (stdout)
    mov ebp, num        ; buffer to write
    mov esp, 5          ; number of bytes to write
    int 0x80            ; call kernel

    ret

_read_line:
    ; Read a line from stdin
    mov eax, 3          ; sys_read
    mov ebx, 0          ; file descriptor (stdin)
    mov ecx, num        ; buffer to store input
    mov edx, 5          ; maximum number of bytes to read
    int 0x80            ; call kernel

    ; Null-terminate the input
    mov byte [ecx+eax], 0

    ret

_add_to_list:
    ; Get current list index
    mov ecx, [list_index]

    ; Calculate address to store the number
    lea edi, [num_list + ecx * 5]

    ; Copy the number to the list
    mov esi, num
    mov ecx, 5
    rep movsb

    ; Increment list index
    inc dword [list_index]

    ; ; Print the current index
    ; mov eax, [list_index]
    ; add eax, '0'
    ; mov [num], eax
    ; call _print_num

    ret
