import pandas as pd
import numpy as np

# Product Catalog
data = {
    "p_id": [101, 102, 103],
    "name": ["Lap", "Mouse", "Keyboard"],
    "price": [50000, 500, 1200],
    "q_avail": [20, 100, 50],
}

avail = pd.DataFrame(data)

# Empty Cart
cart = []


# Display Catalog
def dis_catalog():
    print("\nAvailable Products")
    print("-" * 40)
    print(avail)


# Add Product to Cart
def add_cart(p_id):

    found = False

    for i in range(len(avail)):

        if avail["p_id"][i] == p_id:

            item = {
                "p_id": avail["p_id"][i],
                "name": avail["name"][i],
                "price": avail["price"][i]
            }

            cart.append(item)

            print(avail["name"][i], "added to cart")

            found = True
            break

    if not found:
        print("Product not found")


# Checkout
def check_out():

    prices = []

    for item in cart:
        prices.append(item["price"])

    subtotal = np.sum(prices)

    gst = np.round(subtotal * 0.18, 2)

    final_total = subtotal + gst

    print("\nCheckout Summary")
    print("-" * 40)
    print("Subtotal :", subtotal)
    print("GST (18%) :", gst)
    print("Final Amount :", final_total)


# Main Menu
while True:

    print("\n")
    print("1. Display Catalog")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        dis_catalog()

    elif choice == 2:

        p_id = int(input("Enter Product ID: "))
        add_cart(p_id)

    elif choice == 3:

        print("\nCart Items")

        if len(cart) == 0:
            print("Cart is Empty")
        else:
            for item in cart:
                print(item)

    elif choice == 4:

        if len(cart) == 0:
            print("Cart is Empty")
        else:
            check_out()

    elif choice == 5:

        print("Thank You!")
        break

    else:
        print("Invalid Choice")