#Define the Menu of the Cafe
menu = {
    'Coffee': 120,
    'pasta': 140,
    'Maggi': 120,
    'Sandwich': 140,
    'Burger': 140,
    'Tea': 140,
    'Multgrain Biscuits': 80,
    'Fruit Cookies': 140,
    'Butter Almond cookies': 100,
    'Dry Fruit Biscuits': 120,
    'Chocolate Pastery': 120,
    'Black forest pastery': 140,
    'French Fries': 100,
    'Garlic Bread': 140,
}
#greeting to Customer
print("Welcome to Gomzi's Cafe")
print("This is our menu")
print("Coffee:Rs120\nPasta:RS140\nmaggi:Rs120\nsandwich:140\nburger:Rs140\nFrench Fries:Rs100\nGarlic Bread:Rs140\nTea:Rs140\nMultigrain Cookies:Rs80\nFruit Cookies:Rs140\nButter Almond cookies:Rs120\nDryFruits Biscuits:Rs140\nChocolate Pastery: Rs120\nBlackForest Pastery:Rs140\n")

order_total = 0
#120+140=160

#taking Order
print("Hello Sir/madam")
item_1 = input("Enter the Item You Want to order= ")
if item_1 in menu:
        order_total += menu[item_1]  #0+120
        print(f"Your item[item_1] has been added to your order")
else:
        print(f"ordered item[item_1] has not been avaliable")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the second item= ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item[item_2] has been added to your order")
    else:
        print(f"ordered item[item_2] has not been avaliable")
print(f"the total amount of the order to pay is {order_total}")
print("thanking You Visit again")
