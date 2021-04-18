class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self):
        print('Successful deposit')

    def withdraw(self):
        print('Successful withdrawal')

    def check_balance(self):
        print('This is your Current Balance')

    def transfer(self):
        print('Transfer successful')


food_budget = Budget('Food', 10000)
clothing_budget = Budget('Clothing', 8000)
entertainment_budget = Budget('Entertainment', 5000)



def init():
    print('======= Welcome to the Budget App =======')
    menu()


def menu():
    print('These are the options: ')
    try:
        selected_option = int(input('1. Deposit 2. Withdraw 3. Check Balance 4. Transfer 5. Quit \n'))
    except: 
        print('Invalid option')
        menu()
    
    if selected_option == 1:
        deposit()
    elif selected_option == 2:
        withdraw()
    elif selected_option == 3:
        check_balance()
    elif selected_option == 4:
        transfer()
    elif selected_option == 5:
        quit()
    else:
        print('Invalid option selected')
        menu()

    
def deposit():

    print('Please select the budget you wish to deposit to')

    selected_budget = int(input('1. Food Budget 2. Clothing Budget 3. Entertainment Budget \n'))

    if selected_budget == 1:
        print(food_budget.deposit())

    elif selected_budget == 2:
        print(clothing_budget.deposit())

    elif selected_budget == 3:
        print(entertainment_budget.deposit())
    else:
        print('Invalid option selected')
        deposit()


def withdraw():

    print('Please select from which budget you will like to withdraw from')

    selected_budget = int(input('1. Food Budget 2. Clothing Budget 3. Entertainment Budget \n'))

    if selected_budget == 1:
        print(food_budget.withdraw())

    elif selected_budget == 2:
        print(clothing_budget.withdraw())

    elif selected_budget == 3:
        print(entertainment_budget.withdraw())
    else:
        print('Invalid option selected')
        withdraw()


def check_balance():

    print('Please select a budget')

    selected_budget = int(input('1. Food Budget 2. Clothing Budget 3. Entertainment Budget \n'))

    if selected_budget == 1:
        print(food_budget.check_balance())

    elif selected_budget == 2:
        print(clothing_budget.check_balance())

    elif selected_budget == 3:
        print(entertainment_budget.check_balance())
    else:
        print('Invalid option selected')
        check_balance()


def transfer():

    print('Please select a Budget category')

    selected_budget = int(input('1. Food Budget 2. Clothing Budget 3. Entertainment Budget \n'))

    if selected_budget == 1:
        print(food_budget.transfer())

    elif selected_budget == 2:
        print(clothing_budget.transfer())

    elif selected_budget == 3:
        print(entertainment_budget.transfer())
    else:

        print('Invalid option selected')
        transfer()

def quit():
    try:

        option = int(input('Do you want to quit? 1. Yes 2. No \n'))
    except: 
        print('Invalid option')
        quit()

    if option == 1:
        exit()
    elif option == 2:
        menu()
    else:
        print('Invalid option')
        quit()

init()           
        
        

