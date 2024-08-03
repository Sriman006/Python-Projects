import random



MAX_LINES = 3
MAX_BET = 100
MIN_BET =1
ROWS = 3
COLS =3
symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}



symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_Winings(columns, lines, bet , values):
    winnings = 0 
    for line in range(lines):
        symbol = columns[line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet    
    return winnings

        
def get_slot_machines_slot(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_counts in symbols.items():
        
        for _ in range(symbol_counts):
            all_symbols.append(symbol)
    columns =  []          
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row  in range(len(columns[0])):
        for i , column in enumerate(columns) :
            if i != len(columns) - 1 :
                print(column[row], end =  "|")
            else:
                 print(column[row], end = "")

        print()                     



            
                                       
def deposite():
    while True:

        amount = input("what would you like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than zero.")

        else :
            print("Please type only a numbers")        


    return amount                          


def get_number_of_lines():
    while True:

        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES  :
                break
            else:
                print("Enter the valid number of lines.")

        else :
            print("Please type only a numbers")        


    return lines   

def get_bet():
    while True:

            bet = input("what would you like to bet?$ " )
            if bet.isdigit():
                bet = int(bet)
                if MIN_BET <= bet <= MAX_BET  :
                    break
                else:
                    print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")

            else :
                print("Please type only a numbers")        


    return bet 
                
def main():
  while True:
    balance = deposite()
    lines = get_number_of_lines()
    bet  = get_bet() 
    total_lines_bet = bet*lines
    if balance >= total_lines_bet:
        print(balance, lines, bet)
        break
    else:
        print(f"your total_lines to bet is {total_lines_bet} so you have not sufficient to bet with these balance {balance}")

    slot = get_slot_machines_slot(ROWS,COLS,symbol_count)   
    r = print_slot_machine(slot)     
    print(r)

main()





















            