#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
int
main()
{
    time_t current_time = time(NULL)+32400;
    //UTCからJSTに変換
    int current_day = current_time/86400;
    int menu_number = (current_day -19936)%4;
    if(menu_number == 0){
        printf("Today's Soup is Soy Sauce Seaweed\n");
    }
    if(menu_number == 1){
        printf("Today's Soup is Salt Seaweed\n");
    } 
    if(menu_number == 2){
        printf("Today's Soup is Soy Sauce Egg\n");
    } 
    if(menu_number == 3){
        printf("Today's Soup is Salt Egg\n");
    }   
    return 0;
}
