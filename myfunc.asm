
   global myfunc     ;must be declared for linker (ld)

   section	.text

myfunc:	            ;tells linker entry point
   mov	rdx,len     ;message length
   mov	rcx,msg     ;message to write
   mov	rbx,1       ;file descriptor (stdout)
   mov	rax,4       ;system call number (sys_write)
   int	0x80        ;call kernel
	
   mov	eax,1       ;system call number (sys_exit)
   int	0x80        ;call kernel

section	.data
msg db 'Hello, world!', 0xa  ;string to be printed
len equ $ - msg     ;length of the stringnams