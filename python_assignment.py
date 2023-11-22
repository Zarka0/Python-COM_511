class ATM:
    def __init__(self):
        self.users = {}
        self.admin = {"admin": "admin123"}  # Admin credentials
        self.admin_balance = {100: 2, 2000: 5}
        self.min_balance = 5000
        self.max_user_balance = 300000
        self.max_user_withdrawal = 50000
        self.max_user_deposit = 100000

    def user_menu(self):
        print("1. Cash Deposit")
        print("2. Cash Withdrawal")
        print("3. Check Balance")
        print("4. Change User Name or Password")
        print("5. Exit")

    def admin_menu(self):
        print("1. Total Balance")
        print("2. Cash Deposit")
        print("3. Notification")
        print("4. Exit")

    def authenticate_user(self, user_id, password):
        if user_id in self.users and self.users[user_id]["password"] == password:
            return True
        else:
            return False

    def authenticate_admin(self, admin_id, password):
        if admin_id == "admin" and self.admin[admin_id] == password:
            return True
        else:
            return False

    def cash_deposit(self, user_id, password):
        if not self.authenticate_user(user_id, password):
            print("Invalid credentials. Please try again.")
            return

        amount = int(input("Enter the amount to deposit: "))
        if amount > self.max_user_deposit:
            print(f"Maximum deposit limit exceeded. Limit is {self.max_user_deposit}.")
            return

        denominations = [100, 200, 500, 2000]
        deposit_details = {}
        for denomination in denominations:
            count = int(input(f"Enter the number of {denomination} notes: "))
            deposit_details[denomination] = count

        total_deposit = sum(denomination * count for denomination, count in deposit_details.items())
        self.users[user_id]["balance"] += total_deposit

        print(f"Total deposit = {total_deposit}")

    def cash_withdrawal(self, user_id, password):
        if not self.authenticate_user(user_id, password):
            print("Invalid credentials. Please try again.")
            return

        amount = int(input("Enter the amount to withdraw: "))
        if amount > self.max_user_withdrawal:
            print(f"Maximum withdrawal limit exceeded. Limit is {self.max_user_withdrawal}.")
            return

        if amount > self.users[user_id]["balance"]:
            print("Insufficient balance.")
            return

        denominations = [100, 200, 500, 2000]
        withdrawal_details = {}
        for denomination in denominations:
            count = int(input(f"Enter the number of {denomination} notes: "))
            withdrawal_details[denomination] = count

        total_withdrawal = sum(denomination * count for denomination, count in withdrawal_details.items())
        self.users[user_id]["balance"] -= total_withdrawal

        print(f"Total withdrawal = {total_withdrawal}")

    def check_balance(self, user_id, password):
        if not self.authenticate_user(user_id, password):
            print("Invalid credentials. Please try again.")
            return

        print(f"Current balance: {self.users[user_id]['balance']}")

    def change_user_details(self, user_id, current_password):
        if not self.authenticate_user(user_id, current_password):
            print("Invalid credentials. Please try again.")
            return

        new_password = input("Enter new password: ")
        self.users[user_id]["password"] = new_password
        print("Password changed successfully.")

    def total_balance(self):
        print(f"Total balance: {sum(denomination * count for denomination, count in self.admin_balance.items())}")

    def cash_deposit_admin(self):
        denominations = [100, 200, 500, 2000]
        deposit_details = {}
        for denomination in denominations:
            count = int(input(f"Enter the number of {denomination} notes: "))
            deposit_details[denomination] = count

        total_deposit = sum(denomination * count for denomination, count in deposit_details.items())
        for denomination, count in deposit_details.items():
            self.admin_balance[denomination] += count

        print(f"Total deposit = {total_deposit}")

    def notification(self):
        total_admin_balance = sum(denomination * count for denomination, count in self.admin_balance.items())
        if total_admin_balance < 75000:
            print("Notification: Balance is less than 75k.")


# Main program
atm = ATM()

while True:
    print("*** Welcome to the ATM ***")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Create Account")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        user_id = input("Enter User ID: ")
        password = input("Enter Password: ")
        if atm.authenticate_user(user_id, password):
            while True:
                atm.user_menu()
                user_choice = int(input("Enter your choice: "))
                if user_choice == 1:
                    atm.cash_deposit(user_id, password)
                elif user_choice == 2:
                    atm.cash_withdrawal(user_id, password)
                elif user_choice == 3:
                    atm.check_balance(user_id, password)
                elif user_choice == 4:
                    atm.change_user_details(user_id, password)
                elif user_choice == 5:
                    break
                else:
                    print("Invalid choice. Please try again.")

    elif choice == 2:
        admin_id = input("Enter Admin ID: ")
        password = input("Enter Password: ")
        if atm.authenticate_admin(admin_id, password):
            while True:
                atm.admin_menu()
                admin_choice = int(input("Enter your choice: "))
                if admin_choice == 1:
                    atm.total_balance()
                elif admin_choice == 2:
                    atm.cash_deposit_admin()
                elif admin_choice == 3:
                    atm.notification()
                elif admin_choice == 4:
                    break
                else:
                    print("Invalid choice. Please try again.")

    elif choice == 3:
        user_id = input("Enter User ID: ")
        password = input("Enter Password: ")
        initial_balance = int(input("Enter Initial Balance: "))
        if initial_balance < atm.min_balance:
            print("Initial balance should be at least 5k.")
        else:
            atm.users[user_id] = {"password": password, "balance": initial_balance}
            print("Account created successfully.")

    elif choice == 4:
        break

    else:
        print("Invalid choice. Please try again.")
