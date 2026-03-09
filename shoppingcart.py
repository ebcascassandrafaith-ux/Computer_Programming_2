class Cart:
  def __init__(product):
     product.cart = []

  def addItem(product):
    item = input("Enter item you want to add: ")
    product.cart.append(item)
    print(f"{item} added to cart")

  def removeItem(product):
    removeYarn = input("Enter item you want to remove: ")
    if removeYarn in product.cart:
     product.cart.remove(removeYarn)
     print(f"{removeYarn} has been successfully deleted!")
    else:
     print(f"{removeYarn} not found in cart")

  def viewItem(product):
   if not product.cart:
    print("Empty Cart")

   else: 
    print("--- Your Cart ---")
    for idx, item in enumerate(product.cart, 1):
      print(f"{idx}.) {item}")

  
  def checkOut(product):
   if not product.cart:
    print("Empty Cart")
    return
   product.viewItem()
   print("Payment has been processed. Done Check Out. Thank you!")
   product.cart = []

cart = Cart()

while True: 
  
 print("---Your shopping cart---")
 print("Main menu")
 print("A. Add to Cart")
 print("B. Remove Cart")
 print("C. View Cart")
 print("D. Check out na yarn")
 print("E. Exit Cart")
 choice = input("Enter letter: ").upper()

 if choice == "A":
   cart.addItem()
 elif choice == "B":
   cart.removeItem()
 elif choice == "C":
   cart.viewItem()
 elif choice == "D":
   cart.checkOut()
 elif choice == "E":
   exit(0)
 else:
   print("Invalid input")


