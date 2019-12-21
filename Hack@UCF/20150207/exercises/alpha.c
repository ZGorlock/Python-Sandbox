//including standard libraries
#include<stdio.h>
#include<stdlib.h>

//main is the first thing called
//3 args: number of args, list of args, list of environment variables
int main(int argc, char** argv, char** envp)
{
    //char is one byte, we can fit 0-26 in it
    //i will be our looping variable
    char i = 0;

    //beginning of uppercase alphabet
    // 0x41 is the actual value in memory
    char A = 0x41;


    //loop to iterate over the bytes that 
    //correspond to the uppercase ascii characters
    while(i < 26)
    {
        //use %c to interpret 0x41 to as an ascii character
        //use %x to see the actual hex value
        printf("%c %x\n",A,A);
        //increment i to end the loop
        i = i + 1;
        //increment the byte to get the next letter
        A = A + 1;
    }

    return 0;
}
