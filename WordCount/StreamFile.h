#include <stdlib.h>
#include <stdio.h>

char* readFile(const char* filename) {    
    FILE* file = fopen(filename, "rb");
    if(file==NULL){
        printf("Failed to open the file.\n");
        return NULL;
    }

    // Determine the size of the file
    fseek(file, 0, SEEK_END);
    long fileSize = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Allocate memory to store the file contents
    char* buffer = (char*)malloc(fileSize + 1);
    if(buffer==NULL){
        printf("Failed to allocate memory.\n");
        fclose(file);
        return NULL;
    }

    // Read the file contents into the buffer
    fread(buffer, 1, fileSize, file);
    buffer[fileSize] = '\0'; // Null-terminate the string

    fclose(file);

    return buffer;
}