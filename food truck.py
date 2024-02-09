# Bank details dictionaries
name_dict = {
    '9245-1357-8624-4361': 'Rabbi Morales',
    '4257-3562-1548-5792': 'Clark Gabble',
    '3625-8674-2456-2561': 'Thompson Roy',
    '1242-6748-2135-3524': 'Krishnaswamy Chinnappa',
    '5145-3267-8756-1364': 'Raheem Salim'
}

pin_dict = {
    '9245-1357-8624-4361': '9248',
    '4257-3562-1548-5792': '1735',
    '3625-8674-2456-2561': '2154',
    '1242-6748-2135-3524': '1253',
    '5145-3267-8756-1364': '7280'
}

balance_dict = {
    '9245-1357-8624-4361': 250000,
    '4257-3562-1548-5792': 50000,
    '3625-8674-2456-2561': 140000,
    '1242-6748-2135-3524': 125000,
    '5145-3267-8756-1364': 85000
}

# class Bank Account
class Bank_Account:
    def __init__(self):
        self.card_num = ""

    # Verifying card number
    def cardnum(self):
        import re
        self.card_num = input("Please enter your 16-digit card number (include hyphens): ")
        if self.card_num in name_dict:
            print("")
            print("Hello,", name_dict.get(self.card_num))
        else:
            print("")
            print("Sorry, we do not detect your account in this bank.")
            quit()

        matched = re.match("[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", self.card_num)
        if bool(matched) and len(self.card_num) == 19:
            if self.card_num in name_dict:
                return matched
        else:
            print("")
            print("Incorrect entry of card number")
            quit()

    # Verifying PIN
    def PIN_num(self):
        import re
        PIN = input("Enter your PIN: ")
        matched2 = re.match("[0-9]{4}", PIN)
        if bool(matched2) and len(PIN) == 4:
            if PIN == pin_dict.get(self.card_num):
                print("")
            else:
                print("")
                print("Incorrect PIN")
                quit()

    # Withdraw option function
    def withdraw(self, total_bill):
        balance = balance_dict.get(self.card_num)
        amount = int(total_bill)
        print("Amount to be paid to Chindian Food Truck: Rs.", amount)
        if balance >= amount:
            balance -= amount
            self.OTP_check()
            balance = balance_dict.get(self.card_num)
            balance -= amount
            print("")
            print("Transaction of Rs.", amount, "successful")
            print("")
            print("------------------------------------------------------------------------------")
            print(
                "Please wait at the takeaway counter, while your delicious food is getting ready! Thank you for choosing Chindian Food Truck! :)")
            print("------------------------------------------------------------------------------")
            quit()
        else:
            print("")
            print("Insufficient balance ")

    # Verifying OTP for withdrawal
    def OTP_check(self):
        import random
        OTP_code = random.randint(1000, 9999)
        print("")
        print("The OTP sent to your registered mobile number is:", OTP_code)
        print("")
        OTP = input("Please enter the 4-digit OTP: ")
        if str(OTP) == str(OTP_code):
            return OTP
        else:
            print("")
            print("Incorrect OTP entered, your withdrawal has failed, please try again.")
            quit()


# Creating an object of Bank Account
s = Bank_Account()

# Price dictionaries
price = {
    1: 100,
    2: 120,
    3: 130,
    4: 150,
    5: 250,
    6: 190,
    7: 280,
    8: 200,
    9: 200,
    10: 370,
    11: 350,
    12: 280,
    13: 150,
    14: 170,
    15: 200,
    16: 180,
    17: 180,
    18: 200,
    19: 250,
    20: 300,
    21: 50,
    22: 50,
    23: 80,
    24: 70
}

# Code dictionaries
menu_code = {
    1: "hot and sour veg soup",
    2: "hot and sour chicken soup",
    3: "sweet corn veg soup",
    4: "sweet corn chicken soup",
    5: "gobi croquettes",
    6: "stir-fry vegetables",
    7: "paneer tikka",
    8: "babycorn skewers",
    9: "chilli chicken",
    10: "buttered prawns",
    11: "fish fingers",
    12: "dragon chicken",
    13: "veg fried rice",
    14: "paneer fried rice",
    15: "gobi manchurian",
    16: "veg tikka masala",
    17: "chicken fried rice",
    18: "seafood fried rice",
    19: "chicken manchurian",
    20: "seafood manchurian",
    21: "coffee",
    22: "tea",
    23: "green tea",
    24: "iced coffee"
}

# Cart
cart = []

# Order number generation
import random
order_no = random.randint(1000, 9999)

# Initializing bill
billtotal = 0

# Entry code
print("WELCOME TO CHINDIAN FOOD TRUCK!")
print("")
phno = input("Please enter your phone number: ")
if len(phno) == 10:
    pass
elif len(phno) != 10:
    print("Please enter a valid 10-digit phone number")
    phno = input("Please enter your phone number: ")
print("")
print("Please see the menu below: ")
print("")

# Soup
print("Soup:")
print("1 - Hot and Sour Veg Soup - 100")
print("2 - Hot and Sour Chicken Soup - 120 ")
print("3 - Sweet Corn Veg Soup - 130")
print("4 - Sweet Corn Chicken Soup - 150")
print("")

# Veg starters
print("Veg Starters:")
print("5 - Gobi Croquettes - 250")
print("6 - Stir-Fry Vegetables - 190")
print("7 - Paneer Tikka - 280")
print("8 - Babycorn Skewers - 200")
print("")

# Non-veg starters
print("Non-Veg Starters:")
print("9 - Chilli Chicken - 200")
print("10 - Buttered Prawns - 370")
print("11 - Fish Fingers - 350")
print("12 - Dragon Chicken - 380")
print("")

# Veg main course
print("Veg Main Course:")
print("13 - Veg Fried Rice - 150")
print("14 - Paneer Fried Rice - 170")
print("15 - Gobi Manchurian - 200")
print("16 - Veg Tikka Masala - 180")
print("")

# Non-veg main course
print("Non-Veg Main Course:")
print("17 - Chicken Fried Rice - 180")
print("18 - Seafood Fried Rice - 200")
print("19 - Chicken Manchurian - 250")
print("20 - Seafood Manchurian - 300")
print("")

# Drink menu
print("Drinks:")
print("21 - Coffee - 50")
print("22 - Tea - 50")
print("23 - Green Tea - 80")
print("24 - Iced Coffee - 70")
print("")

# Order
print("What would you like to have?")
while True:
    ans = int(input("Enter the subsequent code (0 - confirm cart): "))
    if ans in price:
        print("")
        cart.append(menu_code.get(ans))
        print("Your Cart:", cart)
        billtotal = billtotal + price.get(ans)
        print("")
        print("Anything else?")
    elif ans == 0:
        print("")
        print("YOUR FINALIZED CART:", cart)
        # GST Calculation in billtotal
        sgst = float(0.09 * billtotal)
        cgst = float(0.09 * billtotal)
        total_bill = sgst + cgst + billtotal
        print("--------------------------------")
        print("	   Chindian Food Truck")
        print("--------------------------------")
        print("			  Bill")
        print("--------------------------------")
        print("Customer Phone No:", phno)
        print("Order No:", order_no)
        print("--------------------------------")
        print("Items:", len(cart))
        print("--------------------------------")
        for i in cart:
            i.split('\t')[0]
            i = i.upper()
            print(i)
        print("--------------------------------")
        print("Total Amount:         Rs.", billtotal)
        print("CGST 5%:              Rs.", cgst)
        print("SGST 5%:              Rs.", sgst)
        print("--------------------------------")
        print("Total Bill:           Rs.", total_bill)
        print("--------------------------------")
        print("GRAND TOTAL:          Rs.", int(total_bill))
        print("--------------------------------")
        print("		 Thank You")
        print("		 Visit Again :)")
        print("--------------------------------\n")

        # Payment
        print("")
        print("")
        print("Payment:")
        print("1 -> Cash")
        print("2 -> Card")
        print("")
        pay = str(input("->"))
        print("")
        if "1" in pay:
            print("Payment done!")
            quit()
        elif "2" in pay:
            print("Welcome to MUFJ Bank!")
            print("")
            s.cardnum()
            print("")
            s.PIN_num()
            s.withdraw(total_bill)
        else:
            print("Invalid input")
            quit()
    else:
        print("Invalid input, please enter a valid menu code.")
