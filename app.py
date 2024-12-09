import time
def Soup(number: int):
    current_time = time.time + 32400
    #UTCからJSTに変換
    current_day = current_time/86400
    Today_menu_number = (current_day -19936)%4
    Today_menu_number += number
    if menu_number == 0 :
        return "Soy Sauce Seaweed"
    if menu_number == 1 :
        return "Salt Seaweed!!!"
    if menu_number == 2 :
        return "Soy Sauce Egg"
    if menu_number == 3 :
        return "Salt Egg!!!"

