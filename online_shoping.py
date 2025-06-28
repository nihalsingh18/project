
# ==================== User Module ====================
users = {}  # Stores user credentials
current_user = None

def register():
    print("\n📝 User Registration")
    username = input("Enter a new username: ")
    if username in users:
        print("❌ Username already exists.")
        return False
    password = input("Enter password: ")
    users[username] = password
    print("✅ Registration successful!")
    return True

def login():
    global current_user
    print("\n🔐 User Login")
    username = input("Username: ")
    password = input("Password: ")
    if users.get(username) == password:
        current_user = username
        print(f"✅ Welcome, {username}!")
        return True
    print("❌ Invalid credentials.")
    return False

# ==================== Product and Cart ====================
class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        return f"{self.product_id} [{self.category}] - {self.name} - ₹{self.price}"

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.catalog = []
        self.cart = []
        self.sales_tracker = {}  # product_id -> total_quantity_sold
        self.feedbacks = []      # list of (username, feedback)

    def add_product(self, product):
        self.catalog.append(product)

    def show_products(self, category_filter=None):
        print("\n🛍️ Available Products:")
        found = False
        for product in self.catalog:
            if not category_filter or product.category.lower() == category_filter.lower():
                print(product.display())
                found = True
        if not found:
            print("❌ No products in this category.")

    def add_to_cart(self, product_id, quantity):
        for product in self.catalog:
            if product.product_id == product_id:
                self.cart.append(CartItem(product, quantity))
                print(f"✅ Added {quantity} x {product.name} to cart.")
                return
        print("❌ Product not found.")

    def remove_from_cart(self, product_id):
        for item in self.cart:
            if item.product.product_id == product_id:
                self.cart.remove(item)
                print(f"🗑️ Removed {item.product.name} from cart.")
                return
        print("❌ Item not found in cart.")

    def view_cart(self):
        print("\n🧺 Your Cart:")
        if not self.cart:
            print("Cart is empty.")
            return
        total = 0
        for item in self.cart:
            subtotal = item.subtotal()
            print(f"{item.product.name} (x{item.quantity}) - ₹{subtotal}")
            total += subtotal
        print(f"🧾 Total: ₹{total}")

    def checkout(self):
        if not self.cart:
            print("\n🧺 Cart is empty.")
            return
        print("\n🛍️ Thank you for shopping!")
        self.view_cart()
        for item in self.cart:
            pid = item.product.product_id
            self.sales_tracker[pid] = self.sales_tracker.get(pid, 0) + item.quantity
        print("✅ Checkout complete.")
        self.cart.clear()

    def leave_feedback(self):
        if not current_user:
            print("❌ You must log in to leave feedback.")
            return
        fb = input("Enter your feedback: ")
        self.feedbacks.append((current_user, fb))
        print("✅ Thank you for your feedback!")

    def show_feedbacks(self):
        print("\n📝 User Feedbacks:")
        if not self.feedbacks:
            print("No feedback yet.")
        for user, fb in self.feedbacks:
            print(f"{user}: {fb}")

    def show_most_selling(self):
        if not self.sales_tracker:
            print("❌ No sales yet.")
            return
        print("\n🔥 Most Selling Products:")
        sorted_sales = sorted(self.sales_tracker.items(), key=lambda x: x[1], reverse=True)
        for pid, qty in sorted_sales[:3]:
            for product in self.catalog:
                if product.product_id == pid:
                    print(f"{product.name} - Sold: {qty} pcs")

# ==================== Main Program ====================
def main():
    cart = ShoppingCart()

    # ✅ Add Boys Products
    cart.add_product(Product("B001", "Boys T-shirt", 500, "Boys"))
    cart.add_product(Product("B002", "Boys Jeans", 800, "Boys"))
    cart.add_product(Product("B003", "Boys Shoes", 1200, "Boys"))
    cart.add_product(Product("B004", "Boys Jacket", 1500, "Boys"))
    cart.add_product(Product("B005", "Boys Cap", 300, "Boys"))

    # ✅ Add Men Products
    cart.add_product(Product("M001", "Men's Watch", 2500, "Men"))
    cart.add_product(Product("M002", "Men's Wallet", 1000, "Men"))
    cart.add_product(Product("M003", "Men's Shirt", 1500, "Men"))
    cart.add_product(Product("M004", "Men's Shoes", 3000, "Men"))
    cart.add_product(Product("M005", "Men's Sunglasses", 1200, "Men"))

    # ✅ Add Women Products
    cart.add_product(Product("W001", "Women's Dress", 3000, "Women"))
    cart.add_product(Product("W002", "Women's Handbag", 2000, "Women"))
    cart.add_product(Product("W003", "Women's Sandals", 1500, "Women"))
    cart.add_product(Product("W004", "Women's Scarf", 700, "Women"))
    cart.add_product(Product("W005", "Women's Earrings", 400, "Women"))

    while True:
        print("\n=== 🛒 Online Shopping Cart ===")
        print("1. Register")
        print("2. Login")
        print("3. View All Products")
        print("4. View Products by Category")
        print("5. Add Items to Cart (Multiple)")
        print("6. View Cart")
        print("7. Checkout")
        print("8. Leave Feedback")
        print("9. View Feedbacks")
        print("10. Most Selling Products")
        print("11. Remove Item from Cart")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            cart.show_products()
        elif choice == "4":
            cat = input("Enter category (Boys/Men/Women): ")
            cart.show_products(cat)
        elif choice == "5":
            if not current_user:
                print("❌ Please login first.")
                continue
            print("\n➕ Add multiple items to cart. Type 'done' to finish.")
            while True:
                pid = input("Enter Product ID (or 'done' to finish): ")
                if pid.lower() == "done":
                    break
                try:
                    qty = int(input("Enter Quantity: "))
                    cart.add_to_cart(pid, qty)
                except ValueError:
                    print("❌ Invalid quantity.")
        elif choice == "6":
            cart.view_cart()
        elif choice == "7":
            cart.checkout()
        elif choice == "8":
            cart.leave_feedback()
        elif choice == "9":
            cart.show_feedbacks()
        elif choice == "10":
            cart.show_most_selling()
        elif choice == "11":
            if not current_user:
                print("❌ Please login first.")
                continue
            if not cart.cart:
                print("🧺 Your cart is already empty.")
                continue
            pid = input("Enter Product ID to remove: ")
            cart.remove_from_cart(pid)
        elif choice == "12":
            print("👋 Thank you! Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run program
if __name__ == "__main__":
    main()
