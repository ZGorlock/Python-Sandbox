//intro to memory addresses

//include standard libraries
#include<stdio.h>
#include<stdlib.h>

//main function
//3 args
int main(int argc, char** argv, char** envp)
{
    //uninitialized variables are bad!
    //dont do this!
    //STALE STACK DATA
    char not_A;
    //still on the stack
    char *not_b = &not_A;

    //A is data on the stack
    //b is the location (memory address) of A on the stack
    char A = 'A';
    char *b = &A;

    //contains address 0x0 or NULL
    char *null_ptr = NULL; 
   
    //use %p to print memory addresses in a pretty hex format 
    printf("b %p %x\n", b, *b);
    
    printf("not_b %p %x\n", not_b, *not_b);

    //grabbing the value at address NULL or 0x0 will segfault
    //dont read, write, execture null pointers
    //example: printf("null %x %x\n", null_ptr, *null_ptr);
    printf("null %x\n", null_ptr);
    return 0;
}
