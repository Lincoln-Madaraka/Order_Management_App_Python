# Restaurant Menu Dictionary
restaurant_menu = {
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
    "Garlic Naan": 35,
    "Gulab Jamun": 70,
    "Ice Cream": 90,
    "Rasgulla": 60,
    "Masala Chai": 30,
    "Cold Drink": 40,
    "Lassi": 50,
    "Coffee": 45
}

























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

