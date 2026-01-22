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
        "ingredients": [
            "1 packet Maggi noodles",
            "1.5 cups water",
            "Masala packet",
            "Vegetables (optional)"
        ],
        "steps": [
            "Boil 1.5 cups of water",
            "Add Maggi noodles",
            "Cook for 2 minutes",
            "Add masala packet",
            "Serve hot"
        ],
        "tips": "Add an egg for extra protein!"
    },
    "dal-rice": {
        "name": "Simple Dal Rice",
        "category": "Main Course",
        "time": "30 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍚",
        "ingredients": [
            "1 cup rice",
            "1/2 cup toor dal",
            "Turmeric powder",
            "Salt",
            "Ghee"
        ],
        "steps": [
            "Wash rice and dal",
            "Pressure cook dal for 3 whistles",
            "Cook rice separately",
            "Mix and serve"
        ],
        "tips": "Add tempering for extra flavor."
    },
    "egg-bhurji": {
        "name": "Egg Bhurji",
        "category": "Breakfast",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍳",
        "ingredients": [
            "4 eggs",
            "1 onion chopped",
            "2 tomatoes chopped",
            "Green chilies",
            "Spices"
        ],
        "steps": [
            "Heat oil in pan",
            "Sauté onions and chilies",
            "Add tomatoes",
            "Beat eggs and pour",
            "Scramble and serve"
        ],
        "tips": "Perfect with toast!"
    },
    "aloo-paratha": {
        "name": "Aloo Paratha",
        "category": "Breakfast",
        "time": "30 minutes",
        "difficulty": "Medium",
        "servings": "4",
        "image": "🥔",
        "ingredients": [
            "Wheat flour",
            "Boiled potatoes",
            "Spices",
            "Ghee"
        ],
        "steps": [
            "Make dough",
            "Prepare potato filling",
            "Stuff and roll",
            "Cook on tawa with ghee"
        ],
        "tips": "Serve with curd and pickle!"
    },
    "poha": {
        "name": "Poha",
        "category": "Breakfast",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍚",
        "ingredients": [
            "2 cups poha",
            "Onion",
            "Peanuts",
            "Curry leaves",
            "Mustard seeds"
        ],
        "steps": [
            "Wash and drain poha",
            "Temper mustard seeds",
            "Add peanuts and curry leaves",
            "Add poha and mix",
            "Serve with lemon"
        ],
        "tips": "Add sev for crunch!"
    },
    "khichdi": {
        "name": "Moong Dal Khichdi",
        "category": "Main Course",
        "time": "25 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍲",
        "ingredients": [
            "Rice",
            "Moong dal",
            "Turmeric",
            "Ghee",
            "Cumin seeds"
        ],
        "steps": [
            "Wash rice and dal",
            "Pressure cook together",
            "Add tempering",
            "Serve with curd"
        ],
        "tips": "Perfect comfort food!"
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
