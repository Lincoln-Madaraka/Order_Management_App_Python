🍔 Command-Line Food Ordering App
A Python-based command-line application that simulates a food ordering system. Forked and enhanced from vikram-singh9/Order_Management_App_Python, this project has been upgraded with better user experience, extended functionalities, and cleaner code structure.

🚀 Features
📋 Menu Display – Browse through a categorized food menu (e.g., Main Course, Drinks, Desserts).

🛒 Order Management – Add, remove, and view items in your cart before placing an order.

💸 Billing System – Get an itemized bill with totals and taxes at checkout.

🔁 Repeat Ordering – Loop back to main menu after completing an order to continue or exit.

🧼 Code Improvements – Modular structure, better input handling, and user prompts.

🛠 Modifications by Lincoln Madaraka
✅ Improved input validation (handles edge cases and invalid entries more gracefully).

✅ Added category-based filtering for menu items.

✅ Enhanced order summary formatting for better readability.

✅ Modularized code into multiple functions for clarity and maintainability.

✅ Customizable tax and discount features added for experimentation.

✅ Added session timestamps and order IDs for better tracking (optional).

📂 Project Structure
bash
Copy
Edit
Order_Management_App/
├── main.py               # Entry point for the CLI app
├── menu.py               # Contains the menu data and helper functions
├── order.py              # Functions related to order/cart management
├── billing.py            # Billing and invoice generation logic
├── utils.py              # Utility functions (e.g., input validation)
└── README.md             # Project documentation
Note: Some of these files may vary depending on your structure; feel free to adjust.

▶️ Getting Started
🔧 Prerequisites
Python 3.7+

No external packages required (fully standard library)

📦 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Lincoln-Madaraka/Order_Management_App_Python.git
cd Order_Management_App_Python
Run the application:

bash
Copy
Edit
python main.py
🧪 Example Usage
bash
Copy
Edit
Welcome to the Food Ordering App!

Please choose an option:
1. View Menu
2. Place Order
3. View Cart
4. Checkout
5. Exit

> 1

----- MENU -----
1. Burger - $5.99
2. Fries - $2.99
3. Soda - $1.99
...
At checkout:

pgsql
Copy
Edit
----- ORDER SUMMARY -----
1 x Burger       $5.99
2 x Fries        $5.98
-------------------------
Subtotal:        $11.97
Tax (10%):       $1.20
Total:           $13.17

Thank you for your order!
🔍 Future Improvements
 Add JSON or SQLite-based order history persistence.

 Support for user profiles and saved preferences.

 Add CLI color formatting for enhanced visuals using colorama.

 Enable export of bill to text or PDF.
