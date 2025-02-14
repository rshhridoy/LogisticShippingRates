def calculate_shipping_cost():
    """Calculate the shipping cost based on weight and rate."""
    try:
        weight = float(input("Enter package weight (kg): "))
        rate = float(input("Enter shipping rate per kg: "))
        print(f"Shipping Cost: {weight * rate:.2f} USD")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculate_shipping_cost()
