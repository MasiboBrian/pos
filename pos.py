from datetime import datetime

# Store the item prices in a list
# in the same order as shown in the menu
itemPrice = [10, 8.75, 9.5, 10.25, 9.5, 11.25]
# To store the total price of the items selected
total = 0.0
# To store the total calculated bill
bill = 0.0
again = ''
# To store the senior discount
seniorDiscount = 0.0
# Store the tax to be added
tax = 0.0
# Store the gift money
giftMoney = 0.0
#Store the MondayLunch
mondayLunch = 0.0


# Function to calculate lunch money discount
def mondayLunch(price):
    discount = 0
    # Extract the week
    week = datetime.today().weekday()
    # Extract current time
    current_time = datetime.now()
    # Check if the week and time are as required
    # week = 1 for monday
    if week == 0 and 11 <= current_time.hour <= 15:
        discount += 0.05 * bill
    # Return the discount calculated
    return discount


# Function to calculate the senior discount
def seniorDiscountCalc(price):
    discount = 0
    # User input if older than 65 or not
    old = input('Are you 65 years old or older (Y or N) ? ')
    # Input validation
    while (old != 'y' and old != 'Y' and old != 'n' and old != 'N'):
        old = input('Invalid choice. Are you 65 years old or older (Y or N) ? ')
    # Calculate discount based on the input
    if (old == 'y' or old == 'Y'):
        discount += 0.1 * price
    # Return the discount calculated
    return discount


# Loop till the user wants to continue
while (True):
    # Show menu
    print('Dish No.  Dish Name      Price')
    print('------------------------------')
    print('1.        Gang Gai      $10.00')
    print('2.        Pad Thai      $8.75')
    print('3.        Pad Cashew    $9.50')
    print('4.        Pad Prik      $10.25')
    print('5.        Peanut Curry  $9.50')
    print('6.        Curry Noodle  $11.25')
    # User input for the item number
    item = int(input('Enter the item number you want (1-6) : '))
    # Input validation
    while (item < 1 or item > 6):
        item = int(input('Invalid item choice. Enter valid item number (1-6) : '))
    # Add the price of the item into total
    total = total + itemPrice[item - 1]

    # Call the function and store the discount
    old = seniorDiscountCalc(itemPrice[item - 1])
    # Add the senior discount returned
    seniorDiscount = seniorDiscount + old

    # Ask if the user wants to continue
    again = input('Would you like to order another item (Y or N) ? ')
    # User validation
    while (again != 'y' and again != 'Y' and again != 'n' and again != 'N'):
        again = input('Invalid choice. Would you like to order another item (Y or N) ? ')
    # Exit the loop if user enters n or N
    if (again == 'n' or again == 'N'):
        break
    print()

# Store total in bill
bill = total
# Deduct senior discount
bill = bill - seniorDiscount
# Function call and store th ereturned value
mondayLunchSpecial = mondayLunch(total)
# Deduct the lunch discount
bill = bill - mondayLunchSpecial
# Calculate tax
tax = 0.06 * bill
# Add the tax intobill
bill = bill + tax

# Ask user for giftcard
gift = input('Do you have a gift card (Y or N) ? ')
while (gift != 'y' and gift != 'Y' and gift != 'n' and gift != 'N'):
    gift = input('Invalid choice. Do you have a gift card (Y or N) ? ')
    if (gift == 'n' or gift == 'N'):
        break

# Ask user for gift money to be used if user enters y or Y
if (gift == 'y' or gift == 'Y'):
    giftMoney = float(input('How much money would you like to apply from card ? '))
# Deduct gift money from bill
bill = bill - giftMoney

# Display the bill
print('\n              Bill Information                   ')
print('---------------------------------------------')
print('Total of all items       :             $', round(total, 2))
print('Total senior discounts   :            -$', round(seniorDiscount, 2))
print('Lunch special discount   :            -$', round(mondayLunchSpecial, 2))
print('Tax                      :            +$', round(tax, 2))
print('Gift card amount applied :            -$', round(giftMoney, 2))
print('                ---------------')
print('                 Bill : $', round(bill, 2))