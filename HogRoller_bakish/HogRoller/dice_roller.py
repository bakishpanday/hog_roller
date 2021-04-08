from objects import Dice
from objects import Die

def main():
    print("The Dice Roller program") 
    print()

    # get number of dice from user 
    count = int(input("Enter the number of dice to roll: "))
    
    # Dice object and add Die objects to it 
    dice = Dice.Dice()
    for i in range(count): 
        die = Die.Die()
        dice.addDie(die) 
        
    while True:
        print( "Be Patient Your Lucky Dice is Rolling......", end="")      
        # roll the dice dice.rollAll()
        for die in dice.list:
            die.roll ()
            print(die.value, end=" ") 

        print("\n")

        choice = input("Roll again? (y/n): ") 

        
        if choice == "y" or choice =="yes" or choice =="Yes":
            return main()
        elif choice == "n" or choice =="no" or choice =="No":
            print("Bye Bye Have A Nice Day !!!")
            break

if __name__ == "__main__": 
    main()