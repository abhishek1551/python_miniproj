import random
MAX_LINES = 3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3

# Defining the symbols and their counts
symbol_count ={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
# Defining the values associated with symbols
symbol_value ={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
# Function to check for winning combinations
def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines =[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check =column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

# Function to generate a random slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
     # Populate all_symbols with symbols based on their counts
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    columns= []
    for _ in range(cols):
        column=[]
        current_symbols= all_symbols[:] #copying a list called all_symbols
        for _ in range(rows):
            value= random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

# Function to print the slot machine display
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i !=len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# Function to get the initial deposit amount from the user
def deposit():
    while True:
        amount= input("How much would you want to deposit? $")
        if amount.isdigit():
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("please enter a number.")

    return amount 
# Function to get the number of lines to bet on
def get_number_of_lines():
    while True:
        lines= input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        
        if lines.isdigit():
            lines= int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("please enter a number.")

    return lines

# Function to get the bet amount
def get_bet():
    while True:
        amount= input("What would you like to bet on each line?")
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET<= amount<=MAX_BET:
                break
            else:
                print(f"Amount must be in between {MIN_BET} and ${MAX_BET}.")
        else:
            print("please enter a number.")

    return amount 
# Function to spin the slot machine and calculate winnings
def spin(balance):
    lines= get_number_of_lines()
    while True:
        bet= get_bet()
        total_bet= bet*lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots= get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won {winnings}.")
    print(f"You won on lines:", *winning_lines) # * PASSES all lines in the print statement..
    return winnings- total_bet

    

#Main game loop
def main():
    balance= deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer= input ("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


main()

