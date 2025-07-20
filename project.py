cafe_menu = {
    "Cappuccino": 100,
    "Masala Chai": 50,
    "Cold Coffee with Ice Cream": 130,
    "Grilled Cheese Sandwich": 90,
    "Veg Wrap": 100,
    "French Fries": 70,
    "Pasta in White Sauce (Veg)": 140,
    "Caesar Salad": 110,
    "Chocolate Brownie (with Ice Cream)": 110,
    "Fresh Fruit Smoothie (Seasonal)": 120
}
print("Welcome to our café!")
print("Would you like to see our menu?")
customer=input("Yes or No :")
if customer.title()=='Yes': 
    print("Sure! Here is the menu")
    for item,price in cafe_menu.items():
      print(f"{item}:{price}")
#print("Can I take your order, please?")
orders_taken=[]
price=0
while True:
   item=input("please enter the item you want! :")
   if item in cafe_menu:
      print("Done! Your order has been added")
      orders_taken.append(item)
      price+=cafe_menu[item]
   elif item not in cafe_menu and item !="enough":
      print('your order is not availble!')
   if item=="enough":
      print("DOne! wait 2 min the order will be serve to you")
      break
print("Your ordered items are:",end="\n")
for item in orders_taken:
   print(f"{item}:{cafe_menu[item]}Rs")
print("Total bill you have to pay :",price)
while True:
  payment=input("payment Done or not :")
  if payment.title()=="Done":
   print("payment Recieved")
   print("Thank you for visiting! Have a great day!")
   break
  else :
   print("payment not received, Try it again")
  

