spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    spicy_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spicy_foods;

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        heat_number = item["heat_level"] * "🌶"  
        print( f"{item['name']} ({item['cuisine']}) | Heat Level: {heat_number}" )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item['cuisine'] == cuisine:
            return item
    return None 

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level = '🌶' * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods) if spicy_foods else 0
    return round(average_heat)

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
