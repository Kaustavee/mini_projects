#define the menu of the restaurant
menu = {   #we are using dictionary data set.
    'burger': 5.99,
    'fries': 2.99,
    'drink': 1.99,
    'pasta' : 3.56,
    'salad' : 2.99,
    'pizza' : 4.99,
}
print("WELCOME TO OUR FINE DINE RESTAURANT !!!!!")
print("Our special MENU for today-----")
print("prices are in USD")
print("1.PIZZA :4.99\n2.PASTA :3.56\n3.SALAD :2.99\n4.FRIES :2.99\n5.BURGER:5.99\n6.COMPLEMENTARY DRINK :1.99")
order_total = 0 #used for calculting the total amount(price) of the orderd items.
#eg - 5.99+2.99
while True:
    operation = int(input("enter 1 for placing order\n enter 2 for updating order\n enter 3 for closing order placements"))
    if operation == 1:
        item_1 = input("enter the name of the item you want to order =   ")
        if item_1 in menu:#we are using membership operator
           print("item available in our menu")
           order_total += menu[item_1] #0 + odereditems price computation...
           print("your order is placed successfully")
           print(f"your item{item_1} has been added to your order")
        else:
            print("item not available in our menu")
    elif operation == 2:
        another_order = input("do you want to order something else along with this---?(yes/no)")
        if another_order == "yes":
            item_2 = input("enter the name of the item you want to order =   ")
            if item_2 in menu:
                print("item available in our menu")
                order_total += menu[item_2] #0 + odereditems price computation...
                print("your order is placed successfully")
                print(f"your item{item_2} has been added to your order")
            else:
                print("item not available in our menu")
    elif operation == 3:
        print("your order is closed")
        print(f"your total bill is {order_total}")
        break
    else :
        print("invalid input")

                
    
    