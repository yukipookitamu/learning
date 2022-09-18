#include <iostream>

#define LOG(x) cout << x << endl; // an unchanging const
using namespace std;

// reviewing pointers before practicing arrays

int main()
{

    // void* ptr = 0; // void means completely typeless
    // void* ptr = NULL;
    void *ptr = nullptr; // all three statements do the same thing

    /*
    Pointer types simply allows us to understand
    the data type that the pointer is pointing to

    '0' is not a valid memory address, thus the pointer
    is not a valid pointer. It is actually equivalent to null
    */

    int var = 8;

    // What if we want to find the memory address of this pointer?

    int *ptr = &var; // Holds the memory address of the variable

    /*
    The fact that this is an int pointer does not change anything.
    The type of the pointer is simply for the user to know what
    the data type that the pointer is pointed to simply is.
    */

    // Dereferencing

    /*
    This is where specifying the pointer type is important. We need
    to tell the compiler the type so it knows how many bytes to
    allocate at the given memory address.

    The '*' essentially grabs whatever data is stored at the address
    the pointer points to.
    */

    *ptr = 10; // '*' dereferences; changing the value to 10
    LOG(var);  // should now output 10

    // What if we want a certain amount of memory?
    char *buffer = new char[8]; // asking for 8 bytes of memory
    memset(buffer, 0, 8);       // https://www.geeksforgeeks.org/memset-in-cpp/

    // delete[] buffer; // to delete the data (unnecessary)
    char **ptr = &buffer; // pointer that points to a pointer; simply points to the memory address of the pointer
    cin.get();
    return 0;
}