#Pokemon Type Tester
#This program will take 2 types as input and output whether one is super-effective, normally effective, not very effective, or does not effect against the other.
#At this time, only single type Pokemon will be tested, but in the future, dual type Pokemon may be added as well.

def main():
    print("Welcome to the Pokemon Type Tester!")
    print("First, you will pick a type to use as the subject.")
    type1 = type_select()
    type2 = " "
    user_select = "0"
    while user_select != "3":
        user_select = main_menu()
        if user_select == "1":
            test(type1, type2)
        elif user_select == "2":
            change_select = type_change_menu()
            if change_select == "1":
                type1 = type_select()
            elif change_select == "2":
                type2 = type_select()
            else:
                print("Invalid Selection. Please try again.")
        elif user_select == "3":
            print("Exiting Program. Goodbye!")
        else:
            print("Invalid Selection. Please try again.")
def main_menu():
    print("Choose a number to select an option from the list.")
    print("1 - Type Effectiveness Tester")
    print("2 - Change Type")
    print("3 - Exit")
    selection = input("Selection:\n")
    return selection
def test(type1,type2):
    if type2 == " ":
        print("Pick a second to type to test against the first.")
        type2 = type_select()
    else:
        pass
def type_change_menu():
    print("Choose a number to select an option from the list.")
    print("1 - Change Type 1") #Type1 is the subject type you will be testing against.
    print("2 - Change Type 2") #Type2 is the type you will be testing against type1
    print("3 - Go Back.")
    selection = input("Selection:\n")
    return selection
def change_type():
    pass
def type_select():
    print("1 - Normal    10 - Flying")
    print("2 - Fire      11 - Psychic")
    print("3 - Water     12 - Bug")
    print("4 - Grass     13 - Rock")
    print("5 - Electric  14 - Ghost")
    print("6 - Ice       15 - Dragon")
    print("7 - Fighting  16 - Dark")
    print("8 - Poison    17 - Steel")
    print("9 - Ground    18 -Fairy")
    poke_type = input("Select your Pokemon type:\n")
    return poke_type

#Strength and Weakness Variables
status1 = "Does Not Effect"    #no_effect_mult = 0
status2 = "Not Very Effective" #little_effect_mult = 0.5
status3 = "Normal Effective"   #normal_effect_mult = 1.0
status4 = "Super-Effective"    #super_effect_mult = 2.0

#List of all Types
type_list = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

#Dictionary of each type with key/value pairs of the types it is super-effective against, not very effective against, and does not effect.
normal_dict = {status1: ["Ghost"], status2: ["Rock", "Steel"], status3: ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Dragon", "Dark", "Fairy"], status4: []}
fire_dict = {status1: [], status2: ["Fire", "Water", "Rock", "Dragon"], status3: ["Normal", "Electric", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Dark", "Steel", "Fairy"], status4: ["Grass", "Ice", "Bug", "Steel"]}
water_dict = {status1: [], status2: ["Water", "Grass", "Dragon"], status3: ["Normal", "Fire", "Electric", "Fighting", "Poison", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dark", "Steel", "Fairy"], status4: ["Fire", "Ground", "Rock"]}
grass_dict = {status1: [], status2: ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"], status3: ["Normal", "Water", "Electric", "Fighting", "Ground", "Psychic", "Ghost", "Dark", "Fairy"], status4: ["Water", "Ground", "Rock"]}
electric_dict = {status1: ["Ground"], status2: ["Electric", "Grass", "Dragon"], status3: ["Normal", "Fire", "Water", "Fighting", "Poison", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dark", "Steel", "Fairy"], status4: ["Water", "Flying"]}
ice_dict = {status1: [], status2: ["Fire", "Water", "Ice"], status3: ["Normal", "Fire", "Water", "Grass", "Electric", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Fairy"], status4: ["Grass", "Ground", "Rock"]}
fighting_dict = {status1: ["Ghost"], status2: ["Poison", "Flying", "Psychic", "Bug", "Fairy"], status3: ["Normal", "Fire", "Water", "Electric", "Ice", "Fighting", "Ground", "Rock", "Ghost", "Dragon", "Dark", "Steel"], status4: ["Normal", "Ice", "Rock", "Dark", "Steel"]}
poison_dict = {status1: ["Steel"], status2: ["Poison", "Ground", "Rock", "Ghost"], status3: ["Normal", "Fire", "Water", "Electric", "Fighting", "Flying", "Psychic", "Bug", "Dragon", "Dark", "Fairy"], status4: ["Grass", "Fairy"]}
ground_dict = {status1: ["Flying"], status2: ["Grass", "Bug"], status3: ["Normal", "Fire", "Electric", "Poison", "Rock", "Ghost", "Dragon", "Dark", "Fairy"], status4: ["Fire", "Electric", "Poison", "Rock", "Steel"]}
flying_dict = {status1: [], status2: ["Electric", "Rock", "Steel"], status3: ["Normal", "Fire", "Water", "Fighting", "Poison", "Ground", "Psychic", "Bug", "Ghost", "Dragon", "Dark", "Fairy"], status4: ["Grass", "Fighting", "Bug"]}
psychic_dict = {status1: ["Dark"], status2: ["Steel"], status3: ["Normal", "Fire", "Water", "Electric", "Fighting", "Poison", "Ground", "Flying", "Bug", "Rock", "Ghost", "Dragon", "Fairy"], status4: ["Fighting", "Poison"]}
bug_dict = {status1: [], status2: ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"], status3: ["Normal", "Water", "Electric", "Ground", "Psychic", "Dragon", "Dark"], status4: ["Grass", "Psychic", "Dark"]}
rock_dict = {status1: [], status2: ["Fighting", "Ground", "Steel"], status3: ["Normal", "Fire", "Poison", "Flying", "Psychic", "Bug", "Ghost", "Dragon", "Dark", "Fairy"], status4: ["Fire", "Ice", "Flying", "Bug"]}
ghost_dict = {status1: ["Normal"], status2: ["Fighting", "Poison"], status3: ["Electric", "Grass", "Ground", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Dark", "Steel", "Fairy"], status4: ["Psychic", "Ghost"]}
dragon_dict = {status1: ["Fairy"], status2: ["Steel"], status3: ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dark"], status4: ["Dragon"]}
dark_dict = {status1: [], status2: ["Fighting", "Dark", "Fairy"], status3: ["Normal", "Fire", "Water", "Electric", "Ice", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Steel"], status4: ["Psychic", "Ghost"]}
steel_dict = {status1: [], status2: ["Fire", "Fighting", "Ground"], status3: ["Normal", "Water", "Electric", "Poison", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Fairy"], status4: ["Ice", "Rock", "Fairy"]}
fairy_dict = {status1: [], status2: ["Fire", "Poison", "Steel"], status3: ["Normal", "Water", "Electric", "Fighting", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark"], status4: ["Fighting", "Dragon", "Dark"]}

#Program Code
if __name__ == "__main__":
    main()