from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Indian recipes database for bachelors
recipes = {
    "maggi": {
        "name": "Quick Maggi Noodles",
        "category": "Quick Meals",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍜",
        "ingredients": ["1 packet Maggi noodles", "1.5 cups water", "Masala packet", "Vegetables (optional)"],
        "steps": ["Boil water", "Add noodles", "Cook", "Add masala", "Serve hot"],
        "tips": "Add an egg for extra protein!"
    },

    "dal-rice": {
        "name": "Simple Dal Rice",
        "category": "Main Course",
        "time": "30 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍚",
        "ingredients": ["Rice", "Toor dal", "Turmeric", "Salt", "Ghee"],
        "steps": ["Cook dal", "Cook rice", "Mix and serve"],
        "tips": "Add tempering for extra flavor."
    },

    "egg-bhurji": {
        "name": "Egg Bhurji",
        "category": "Breakfast",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍳",
        "ingredients": ["Eggs", "Onion", "Tomato", "Green chilies", "Spices"],
        "steps": ["Heat oil", "Sauté onion", "Add tomato", "Add eggs", "Scramble"],
        "tips": "Perfect with toast!"
    },

    "aloo-paratha": {
        "name": "Aloo Paratha",
        "category": "Breakfast",
        "time": "30 minutes",
        "difficulty": "Medium",
        "servings": "4",
        "image": "🥔",
        "ingredients": ["Wheat flour", "Boiled potatoes", "Spices", "Ghee"],
        "steps": ["Prepare dough", "Make filling", "Stuff", "Cook on tawa"],
        "tips": "Serve with curd and pickle!"
    },

    "poha": {
        "name": "Poha",
        "category": "Breakfast",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍚",
        "ingredients": ["Poha", "Onion", "Peanuts", "Curry leaves", "Mustard seeds"],
        "steps": ["Wash poha", "Temper spices", "Add poha", "Mix & serve"],
        "tips": "Add sev for crunch!"
    },

    "khichdi": {
        "name": "Moong Dal Khichdi",
        "category": "Main Course",
        "time": "25 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍲",
        "ingredients": ["Rice", "Moong dal", "Turmeric", "Ghee"],
        "steps": ["Wash", "Pressure cook", "Add ghee"],
        "tips": "Perfect comfort food!"
    },

    "bread-omelette": {
        "name": "Bread Omelette",
        "category": "Breakfast",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥪",
        "ingredients": ["Bread", "Eggs", "Onion", "Spices"],
        "steps": ["Beat eggs", "Cook omelette", "Serve with bread"],
        "tips": "Add cheese for extra taste!"
    },

    "egg-fried-rice": {
        "name": "Egg Fried Rice",
        "category": "Quick Meals",
        "time": "20 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍳",
        "ingredients": ["Cooked rice", "Eggs", "Soy sauce", "Onion", "Oil"],
        "steps": ["Scramble eggs", "Add onion", "Add rice & sauce", "Mix well"],
        "tips": "Best with leftover rice."
    },

    "vegetable-sandwich": {
        "name": "Vegetable Sandwich",
        "category": "Snacks",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥪",
        "ingredients": ["Bread", "Butter", "Cucumber", "Tomato", "Salt"],
        "steps": ["Butter bread", "Add veggies", "Season", "Serve"],
        "tips": "Toast for extra crunch."
    },

    "paneer-bhurji": {
        "name": "Paneer Bhurji",
        "category": "Main Course",
        "time": "20 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🧀",
        "ingredients": ["Paneer", "Onion", "Tomato", "Spices"],
        "steps": ["Sauté onion", "Add tomato", "Add paneer", "Cook"],
        "tips": "Great with roti or bread."
    },

    "cheese-toast": {
        "name": "Cheese Toast",
        "category": "Snacks",
        "time": "8 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🧀",
        "ingredients": ["Bread", "Cheese", "Butter"],
        "steps": ["Butter bread", "Add cheese", "Toast"],
        "tips": "Add chili flakes!"
    },

    "masala-toast": {
        "name": "Masala Toast",
        "category": "Snacks",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍞",
        "ingredients": ["Bread", "Onion", "Tomato", "Spices", "Butter"],
        "steps": ["Mix veggies", "Spread on bread", "Toast"],
        "tips": "Street-style vibes."
    },

    "instant-oats": {
        "name": "Masala Oats",
        "category": "Healthy",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥣",
        "ingredients": ["Oats", "Water", "Masala"],
        "steps": ["Boil water", "Add oats", "Add masala", "Cook"],
        "tips": "Add veggies for health."
    },

    "noodles": {
        "name": "Veg Hakka Noodles",
        "category": "Quick Meals",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍜",
        "ingredients": ["Noodles", "Veggies", "Soy sauce"],
        "steps": ["Boil noodles", "Stir fry veggies", "Add noodles"],
        "tips": "High flame cooking!"
    },

    "egg-curry": {
        "name": "Simple Egg Curry",
        "category": "Main Course",
        "time": "25 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍛",
        "ingredients": ["Eggs", "Onion", "Tomato", "Spices"],
        "steps": ["Boil eggs", "Make gravy", "Add eggs"],
        "tips": "Best with rice."
    },

    "lemon-rice": {
        "name": "Lemon Rice",
        "category": "Quick Meals",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍋",
        "ingredients": ["Rice", "Lemon", "Mustard seeds"],
        "steps": ["Cook rice", "Add tempering", "Add lemon"],
        "tips": "Refreshing & light."
    },

    "curd-rice": {
        "name": "Curd Rice",
        "category": "Main Course",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🥣",
        "ingredients": ["Rice", "Curd", "Salt"],
        "steps": ["Mix rice & curd", "Add salt"],
        "tips": "Comfort food!"
    },

    "upma": {
        "name": "Upma",
        "category": "Breakfast",
        "time": "20 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍲",
        "ingredients": ["Rava", "Water", "Spices"],
        "steps": ["Roast rava", "Add water", "Cook"],
        "tips": "Add veggies."
    },

    "corn-chat": {
        "name": "Masala Corn",
        "category": "Snacks",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🌽",
        "ingredients": ["Corn", "Butter", "Spices"],
        "steps": ["Boil corn", "Add butter & spices"],
        "tips": "Movie-time snack."
    },

    "egg-maggi": {
        "name": "Egg Maggi",
        "category": "Quick Meals",
        "time": "8 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍜",
        "ingredients": ["Maggi", "Egg", "Masala"],
        "steps": ["Boil maggi", "Add egg", "Cook"],
        "tips": "Bachelor luxury upgrade."
    }
}


@app.route('/')
def index():
    categories = {}
    for key, recipe in recipes.items():
        cat = recipe['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append({**recipe, 'id': key})
    return render_template('index.html', categories=categories, recipes=recipes)

@app.route('/api/recipes')
def get_recipes():
    return jsonify(recipes)

@app.route('/api/random')
def random_recipe():
    recipe_key = random.choice(list(recipes.keys()))
    return jsonify({recipe_key: recipes[recipe_key]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
