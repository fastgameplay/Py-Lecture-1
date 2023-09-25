from Dice import Dice

def main():
    while True:
        user_input = input("Enter a dice type (e.g.: D6, D20) or 'q' to quit: ").strip().lower()
        
        if user_input == 'q':
            break
        
        if user_input.startswith('d') and user_input[1:].isdigit():
            sides = int(user_input[1:])
            try:
                dice = Dice(sides)
                result = dice.roll()
                print(f"Rolled a {user_input} and got: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid input format. Please use 'D' followed by a number (e.g., D6, D20).")

if __name__ == "__main__":
    main()
