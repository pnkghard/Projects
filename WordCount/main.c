// #include <stdio.h>
// #include "StreamFile.h"
// #include "wordfreq.h"

// int main(int argc, char* argv[]){
//     if(argc!=2){
//         printf("If you want to enter manual enter (y) otherwose (n)\n");
//         char ch;
//         scanf("%c", &ch);
//         if(ch=='y'){
//             const char* string;
//             scanf("%s", &string);
//             findMostFrequentWord(string);
//         } else {
//             return -1;
//         }
//     }
//     const char* filename = argv[1];
//     char* fileContent = readFile(filename);

//     if(fileContent!=NULL){
//         printf("File content:\n%s\n", fileContent);
//         findMostFrequentWord(fileContent);
//         free(fileContent);
//     }
// }

#include <stdio.h>
#include <stdlib.h>
#include "StreamFile.h"
#include "wordfreq.h"

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("If you want to enter manually, enter 'y'. Otherwise, enter 'n'\n");
        char ch;
        scanf(" %c", &ch);  // Added space before %c to consume newline character
        if (ch == 'y') {
            char string[100];  // Assuming a maximum input length of 100 characters
            printf("%s", string);
            scanf("%s", &string);
            findMostFrequentWord(string);
        } else {
            return -1;
        }
    } else {
        const char* filename = argv[1];
        char* fileContent = readFile(filename);

        if (fileContent != NULL) {
            printf("File content:\n%s\n", fileContent);
            findMostFrequentWord(fileContent);
            free(fileContent);
        }
    }

    return 0;
}
