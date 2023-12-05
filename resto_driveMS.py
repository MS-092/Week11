from resto_classMS import FancyFood

def create_food_list():
    food_list = []
    num_items = int(input("Enter the number of items to purchase: "))
    
    while num_items < 1:
        print("Please enter a valid number (at least 1).")
        num_items = int(input("Enter the number of items to purchase: "))

    for _ in range(num_items):
        food_name = input("Enter the name of the food: ")
        amount_ordered = float(input("Enter the amount of food in pounds: "))
        
        while amount_ordered <= 0:
            print("Please enter a valid amount (greater than 0).")
            amount_ordered = float(input("Enter the amount of food in pounds: "))

        food = FancyFood(food_name, amount_ordered)
        food_list.append(food)

    return food_list

def display_food_list(food_list):
    for food in food_list:
        print(food)

def calculate_total_cost(food_list):
    total_cost = sum(food.getPrice_MS() for food in food_list)
    return total_cost

def main():
    foods = create_food_list()
    display_food_list(foods)

    total_cost = calculate_total_cost(foods)
    print(f"\nTotal Cost of all items: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
