# Restaurant Menu Dictionary
menu = {
    "Paneer Tikka": 180,
    "Chicken Wings": 220,
    "Spring Rolls": 160,
    "French Fries": 120,
    "Butter Chicken": 320,
    "Paneer Butter Masala": 280,
    "Veg Biryani": 200,
    "Chicken Biryani": 250,
    "Tandoori Roti": 20,
    "Butter Naan": 30,
}

print("🍽️ Welcome to Vikram's Restaurant!")
print("Here's our menu")
print("""
    "Paneer Tikka": 180,
    "Chicken Wings": 220,
    "Spring Rolls": 160,
    "French Fries": 120,
    "Butter Chicken": 320,
    "Paneer Butter Masala": 280,
    "Veg Biryani": 200,
    "Chicken Biryani": 250,
    "Tandoori Roti": 20,
    "Butter Naan": 30,
""")

total_order = 0

item1 = input("enter item name: ")
if item1 in menu:
    total_order += menu[item1]
    print(f"{item1} is added to your order")
else:
    print(f"{item1} not found in menu")

item2= input("enter another item name:")

if item2 in menu:
    print(f"{item2} is added to your order!!")
    total_order += menu[item2]
else:
    print(f"{item2} not found in menu")
print(f"your total order is {total_order}")



























# # Show menu to user
# print("🍽️ Welcome to Vikram's Restaurant!")
# print("Here's our menu:\n")
# for item, price in restaurant_menu.items():
#     print(f"{item} - ₹{price}")

# print("\n📝 Let's take your order (type 'done' to finish):\n")

# # Take order from user
# order = {}
# while True:
#     item = input("Enter item name: ").strip()
#     if item.lower() == 'done':
#         break
#     elif item in restaurant_menu:
#         try:
#             quantity = int(input(f"Enter quantity for {item}: "))
#             if item in order:
#                 order[item] += quantity
#             else:
#                 order[item] = quantity
#         except ValueError:
#             print("❌ Please enter a valid number.")
#     else:
#         print("❌ Item not found in menu.")

# # Calculate total bill
# print("\n🧾 Your Bill Summary:\n")
# total = 0
# for item, quantity in order.items():
#     price = restaurant_menu[item]
#     cost = price * quantity
#     total += cost
#     print(f"{item} x {quantity} = ₹{cost}")

# print(f"\n💰 Total Amount to Pay: ₹{total}")
# print("\n🙏 Thank you for dining with us, come again!")

