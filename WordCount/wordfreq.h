#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORD_LENGTH 20

void findMostFrequentWord(const char* str) {
    char word[MAX_WORD_LENGTH];
    char lowercaseWord[MAX_WORD_LENGTH];
    char mostFrequentWord[MAX_WORD_LENGTH];
    int frequency = 0;
    int maxFrequency = 0;

    const char* delimiters = " \t\n.,;:!\"\'()";
    char* token = strtok((char*)str, delimiters);
    while(token!=NULL){
        strcpy(word, token);

        for(int i = 0; word[i]; i++){
            lowercaseWord[i] = tolower(word[i]);
        }
        lowercaseWord[strlen(word)] = '\0';

        if(strlen(token)>0){
            frequency++;
            if(frequency>maxFrequency){
                maxFrequency = frequency;
                strcpy(mostFrequentWord, word);
            }
        }
        token = strtok(NULL, delimiters);
    }
    printf("Most frequent word: %s\n", mostFrequentWord);
    printf("Frequency: %d\n", maxFrequency);
}

// int main(int argc, char* argv[]){
//     if(argc!=2){
//         printf("Please provide file name and try again....\n");
//     } else {
//         FILE *file = fopen(argv[1], "r");

//         if(file==NULL){
//             printf("Failed to open the file.\n");
//             return 1;
//         }

//         char word[MAX_WORD_LENGTH];
//         while(fscanf(file, "%s", word)==1){
//             findMostFrequentWord(word);
//             //printf("%s\n", word);
//         }
//         fclose(file);
//     }

//     return 0;
// }
