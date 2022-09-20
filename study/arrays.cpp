#include <iostream>

int main()
{

    // Intialize an array of integers of size 5
    int example[5]; // Just a pointer to an array allocation in the memory
    int *ptr = example;
    example[0] = 1;
    example[4] = 5;

    // Sets every variable to 2
    // '<' operator is faster than '<='
    for (int i = 0; i < 5; ++i)
    {
        example[i] = 2;
    }

    // Both modify the same bit of data
    example[2] = 5;
    *(ptr + 2) = 6;

    // Creating arrays in the heap; Performs the same as the stack allocated memory above
    int *another = new int[5]; // Will live until destoryed unlike stack
    for (int i = 0; i < 5; ++i)
    {
        another[i] = 2;
    }

    delete[] another;
}