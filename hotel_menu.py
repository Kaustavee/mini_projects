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

item_1 = input("enter the name of the item you want to order =   ")
#we will first check if the ordered items are available in our restaurant or not....
if item_1 in menu:#we are using membership operator
    print("item available in our menu")
    order_total += menu[item_1] #0 + odereditems price computation...
    print("your order is placed successfully")
    print(f"your item{item_1} has been added to your order")
else:
    print(f"ordered item{item_1} is not available yet")
    
another_order = input("do you want to order something else along with this---?(yes/no)")
if another_order == "yes":
    item_2 = input("enter the name of the item you want to order =   ")
    if item_2 in menu:
        print("item available in our menu")
        order_total += menu[item_2]
        print("your order has been placed successfully")
    else:
        print(f"ordered item{item_2} is not available yet")
print(f"the total amount of ordered items is -- {order_total}")
print("thank you for visiting us.....:)")
        
    



