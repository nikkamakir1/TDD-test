import time
def Soup(number: int):
    current_time = time.time + 32400;
    #UTCからJSTに変換
    current_day = current_time/86400;
    Today_menu_number = (current_day -19936)%4;
    Today_menu_number += number
    if menu_number == 0 :
        printf("Today's Soup is Soy Sauce Seaweed\n");
    }
    if menu_number == 1 :
        printf("Today's Soup is Salt Seaweed\n");
    } 
    if menu_number == 2 :
        printf("Today's Soup is Soy Sauce Egg\n");
    } 
    if menu_number == 3 :
        printf("Today's Soup is Salt Egg\n");
    }   
    return 0;
}
