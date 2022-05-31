Name=input("Welcome cashier! Please type your name: ")
print("Welcome,",Name)

print("You have selected selling mode, please enter the products and the prices(in dollars). Please remember! You can only sell 5 products to each costumer.")

good1=input("First product: ")
price1=int(input("Product's price: "))
print("you selected",good1,"with a price of",price1,"dollars")

good2=input("Second product: ")
price2=int(input("Product's price: "))
print("you selected",good2,"with a price of",price2,"dollars")

good3=input("Third product: ")
price3=int(input("Product'super price: "))
print("you selected",good3,"with a price of",price3,"dollars")

good4=input("Fourth product: ")
price4=int(input("Product's price: "))
print("you selected",good4,"with a price of",price4,"dollars")

good5=input("Fifth product: ")
price5=int(input("Product's price: "))
print("you selected",good5,"with a price of",price5,"dollars")

subtotal=price1+price2+price3+price3+price5
print("The subtotal is",subtotal,"dollars")

iva=subtotal*0.16

total=subtotal+iva

print("Your total is",total,"dollars")
print("Printing ticket...")

print("---------Ticket---------")
print("1.",good1,"price",price1)
print("2.",good2,"price",price2)
print("3.",good3,"price",price3)
print("4.",good4,"price",price4)
print("5.",good5,"price",price5)
print("Subtotal =",subtotal)
print("Iva = 16%")
print("Total =",total)
print("You have been attended by",Name)