#include<stdio.h>
#include<stdlib.h>

int main(int argc, char** argv, char** envp) {
    int frog_real = 0x474f5246;
    int frogi = 0x46524f47;
    char *frogc = ((char*)(&frog_real));
    printf("%p %c\n%p %c\n%p %c\n%p %c\n", frogc,frogc[0],frogc+1,frogc[1],frogc+2,frogc[2],frogc+3, frogc[3]);

    return 0;
}
