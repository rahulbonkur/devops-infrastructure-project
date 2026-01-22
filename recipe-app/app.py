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
    "bread-omelette": {
        "name": "Bread Omelette",
        "category": "Breakfast",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥪",
        "ingredients": ["Bread", "Eggs", "Onion", "Spices", "Oil"],
        "steps": ["Beat eggs", "Add onion & spices", "Cook omelette", "Serve with bread"],
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
        "steps": ["Scramble eggs", "Add veggies", "Add rice & sauce", "Mix well"],
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
        "steps": ["Sauté onion", "Add tomatoes & spices", "Add paneer", "Cook well"],
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

    "peanut-butter-sandwich": {
        "name": "Peanut Butter Sandwich",
        "category": "Snacks",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥜",
        "ingredients": ["Bread", "Peanut butter"],
        "steps": ["Spread butter", "Serve"],
        "tips": "Add banana slices."
    },

    "boiled-eggs": {
        "name": "Boiled Eggs",
        "category": "Healthy",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🥚",
        "ingredients": ["Eggs", "Water"],
        "steps": ["Boil eggs", "Peel & eat"],
        "tips": "Sprinkle salt & pepper."
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
    }
    "tomato-rice": {
        "name": "Tomato Rice",
        "category": "Quick Meals",
        "time": "20 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍅",
        "ingredients": ["Rice", "Tomato", "Onion", "Spices"],
        "steps": ["Cook rice", "Prepare tomato masala", "Mix together"],
        "tips": "Add peanuts for crunch."
    },

    "jeera-rice": {
        "name": "Jeera Rice",
        "category": "Quick Meals",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🌾",
        "ingredients": ["Rice", "Cumin seeds", "Ghee"],
        "steps": ["Cook rice", "Temper cumin", "Mix"],
        "tips": "Pairs well with dal."
    },

    "veg-pulao": {
        "name": "Veg Pulao",
        "category": "Main Course",
        "time": "25 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍛",
        "ingredients": ["Rice", "Mixed veggies", "Whole spices"],
        "steps": ["Sauté spices", "Add veggies & rice", "Cook"],
        "tips": "One-pot meal."
    },

    "chicken-instant": {
        "name": "Instant Chicken Fry",
        "category": "Main Course",
        "time": "25 minutes",
        "difficulty": "Medium",
        "servings": "2",
        "image": "🍗",
        "ingredients": ["Chicken", "Onion", "Spices"],
        "steps": ["Marinate chicken", "Cook on pan", "Fry till done"],
        "tips": "Cook covered for softness."
    },

    "bread-upma": {
        "name": "Bread Upma",
        "category": "Breakfast",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍞",
        "ingredients": ["Bread", "Onion", "Spices"],
        "steps": ["Toast bread", "Prepare masala", "Mix together"],
        "tips": "Use leftover bread."
    },

    "cheese-pasta": {
        "name": "Cheese Pasta",
        "category": "Quick Meals",
        "time": "20 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🧀",
        "ingredients": ["Pasta", "Cheese", "Milk"],
        "steps": ["Boil pasta", "Prepare sauce", "Mix"],
        "tips": "Add chili flakes."
    },

    "garlic-bread": {
        "name": "Garlic Bread",
        "category": "Snacks",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🧄",
        "ingredients": ["Bread", "Butter", "Garlic"],
        "steps": ["Mix garlic butter", "Spread & toast"],
        "tips": "Add cheese if available."
    },

    "egg-toast": {
        "name": "Egg Toast",
        "category": "Breakfast",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍳",
        "ingredients": ["Bread", "Eggs", "Salt"],
        "steps": ["Beat egg", "Dip bread", "Toast"],
        "tips": "Street-style snack."
    },

    "banana-smoothie": {
        "name": "Banana Smoothie",
        "category": "Healthy",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍌",
        "ingredients": ["Banana", "Milk", "Sugar"],
        "steps": ["Blend all ingredients"],
        "tips": "Add peanut butter."
    },

    "protein-oats": {
        "name": "Protein Oats",
        "category": "Healthy",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "💪",
        "ingredients": ["Oats", "Milk", "Peanut butter"],
        "steps": ["Cook oats", "Add peanut butter"],
        "tips": "Gym-friendly meal."
    },

    "sprouts-salad": {
        "name": "Sprouts Salad",
        "category": "Healthy",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥗",
        "ingredients": ["Sprouts", "Onion", "Lemon"],
        "steps": ["Mix all ingredients"],
        "tips": "High protein."
    },

    "mayo-sandwich": {
        "name": "Mayonnaise Sandwich",
        "category": "Snacks",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥪",
        "ingredients": ["Bread", "Mayonnaise"],
        "steps": ["Spread mayo", "Serve"],
        "tips": "Add veggies."
    },

    "chana-masala": {
        "name": "Quick Chana Masala",
        "category": "Main Course",
        "time": "20 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🫘",
        "ingredients": ["Boiled chana", "Onion", "Spices"],
        "steps": ["Prepare masala", "Add chana", "Cook"],
        "tips": "Serve with rice or roti."
    },

    "veg-maggy": {
        "name": "Veg Masala Maggi",
        "category": "Quick Meals",
        "time": "7 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍜",
        "ingredients": ["Maggi", "Veggies", "Masala"],
        "steps": ["Boil water", "Add veggies & maggi", "Cook"],
        "tips": "Bachelor classic."
    },

    "milkshake": {
        "name": "Chocolate Milkshake",
        "category": "Snacks",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥤",
        "ingredients": ["Milk", "Chocolate syrup"],
        "steps": ["Blend ingredients"],
        "tips": "Instant energy."
    }
    "veg-omelette": {
        "name": "Veg Omelette",
        "category": "Breakfast",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍳",
        "ingredients": ["Eggs", "Onion", "Capsicum", "Salt"],
        "steps": ["Beat eggs", "Add veggies", "Cook on pan"],
        "tips": "Add cheese if you’re feeling rich."
    },

    "rice-omelette": {
        "name": "Rice Omelette",
        "category": "Quick Meals",
        "time": "12 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍚",
        "ingredients": ["Cooked rice", "Eggs", "Spices"],
        "steps": ["Mix rice & eggs", "Cook like omelette"],
        "tips": "Best leftover rice hack."
    },

    "onion-pakoda": {
        "name": "Onion Pakoda",
        "category": "Snacks",
        "time": "20 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🧅",
        "ingredients": ["Onion", "Besan", "Spices"],
        "steps": ["Mix batter", "Deep fry"],
        "tips": "Rainy day classic."
    },

    "bread-pizza": {
        "name": "Bread Pizza",
        "category": "Snacks",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍕",
        "ingredients": ["Bread", "Sauce", "Cheese", "Veggies"],
        "steps": ["Add toppings", "Toast"],
        "tips": "Oven not required."
    },

    "veg-fried-rice": {
        "name": "Veg Fried Rice",
        "category": "Quick Meals",
        "time": "20 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍚",
        "ingredients": ["Rice", "Veggies", "Soy sauce"],
        "steps": ["Stir fry veggies", "Add rice"],
        "tips": "High flame = restaurant style."
    },

    "curd-sandwich": {
        "name": "Curd Sandwich",
        "category": "Snacks",
        "time": "8 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥪",
        "ingredients": ["Bread", "Curd", "Salt"],
        "steps": ["Mix curd", "Spread on bread"],
        "tips": "Light & cooling."
    },

    "paneer-sandwich": {
        "name": "Paneer Sandwich",
        "category": "Snacks",
        "time": "12 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🧀",
        "ingredients": ["Bread", "Paneer", "Spices"],
        "steps": ["Mash paneer", "Stuff bread"],
        "tips": "High protein snack."
    },

    "egg-roll": {
        "name": "Egg Roll",
        "category": "Snacks",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🌯",
        "ingredients": ["Roti", "Egg", "Onion"],
        "steps": ["Cook egg on roti", "Roll & serve"],
        "tips": "Street food vibes."
    },

    "chicken-sandwich": {
        "name": "Chicken Sandwich",
        "category": "Quick Meals",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍗",
        "ingredients": ["Cooked chicken", "Bread", "Mayo"],
        "steps": ["Mix chicken", "Stuff bread"],
        "tips": "Use leftover chicken."
    },

    "butter-rice": {
        "name": "Butter Rice",
        "category": "Quick Meals",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🧈",
        "ingredients": ["Rice", "Butter", "Salt"],
        "steps": ["Mix butter into rice"],
        "tips": "Lazy day meal."
    },

    "egg-salad": {
        "name": "Egg Salad",
        "category": "Healthy",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥗",
        "ingredients": ["Boiled eggs", "Onion", "Pepper"],
        "steps": ["Chop eggs", "Mix ingredients"],
        "tips": "Gym-friendly."
    },

    "veg-noodles": {
        "name": "Veg Instant Noodles",
        "category": "Quick Meals",
        "time": "7 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍜",
        "ingredients": ["Instant noodles", "Veggies"],
        "steps": ["Boil & cook"],
        "tips": "Add egg for upgrade."
    },

    "chocolate-toast": {
        "name": "Chocolate Toast",
        "category": "Snacks",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍫",
        "ingredients": ["Bread", "Chocolate spread"],
        "steps": ["Spread & toast"],
        "tips": "Midnight cravings solved."
    },

    "fruit-salad": {
        "name": "Fruit Salad",
        "category": "Healthy",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍎",
        "ingredients": ["Mixed fruits"],
        "steps": ["Chop & mix"],
        "tips": "Add honey."
    },

    "dal-toast": {
        "name": "Dal Toast",
        "category": "Quick Meals",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍞",
        "ingredients": ["Bread", "Leftover dal"],
        "steps": ["Spread dal", "Toast bread"],
        "tips": "Zero waste king move."
    }
    "ghee-toast": {
        "name": "Ghee Toast",
        "category": "Breakfast",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🧈",
        "ingredients": ["Bread", "Ghee"],
        "steps": ["Spread ghee", "Toast bread"],
        "tips": "Add sugar or salt as per mood."
    },

    "masala-rice": {
        "name": "Masala Rice",
        "category": "Quick Meals",
        "time": "12 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍛",
        "ingredients": ["Cooked rice", "Masala", "Oil"],
        "steps": ["Heat oil", "Add masala", "Mix rice"],
        "tips": "Best use of leftover rice."
    },

    "egg-bread-fry": {
        "name": "Egg Bread Fry",
        "category": "Breakfast",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍳",
        "ingredients": ["Bread", "Eggs", "Salt"],
        "steps": ["Dip bread in egg", "Fry"],
        "tips": "Crispy outside, soft inside."
    },

    "paneer-fry": {
        "name": "Quick Paneer Fry",
        "category": "Main Course",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🧀",
        "ingredients": ["Paneer", "Spices", "Oil"],
        "steps": ["Heat oil", "Add paneer & spices", "Fry"],
        "tips": "Good protein hit."
    },

    "chicken-omelette": {
        "name": "Chicken Omelette",
        "category": "Breakfast",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍗",
        "ingredients": ["Eggs", "Cooked chicken", "Spices"],
        "steps": ["Beat eggs", "Add chicken", "Cook"],
        "tips": "Gym bros approve."
    },

    "salted-popcorn": {
        "name": "Salted Popcorn",
        "category": "Snacks",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🍿",
        "ingredients": ["Popcorn kernels", "Salt"],
        "steps": ["Pop corn", "Add salt"],
        "tips": "Netflix essential."
    },

    "masala-popcorn": {
        "name": "Masala Popcorn",
        "category": "Snacks",
        "time": "6 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🌶️",
        "ingredients": ["Popcorn", "Chaat masala"],
        "steps": ["Pop corn", "Add masala"],
        "tips": "Street-style kick."
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
    },

    "veg-stir-fry": {
        "name": "Veg Stir Fry",
        "category": "Healthy",
        "time": "12 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🥦",
        "ingredients": ["Mixed veggies", "Oil", "Salt"],
        "steps": ["Heat oil", "Stir fry veggies"],
        "tips": "Low oil, high health."
    },

    "egg-butter-toast": {
        "name": "Egg Butter Toast",
        "category": "Breakfast",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍞",
        "ingredients": ["Bread", "Egg", "Butter"],
        "steps": ["Fry egg", "Serve on buttered toast"],
        "tips": "Fast & filling."
    },

    "curd-veggies": {
        "name": "Curd Veggies Bowl",
        "category": "Healthy",
        "time": "8 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥣",
        "ingredients": ["Curd", "Veggies", "Salt"],
        "steps": ["Mix everything"],
        "tips": "Cooling meal."
    },

    "rice-milk": {
        "name": "Rice with Milk",
        "category": "Quick Meals",
        "time": "5 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🥛",
        "ingredients": ["Cooked rice", "Milk", "Sugar"],
        "steps": ["Mix all ingredients"],
        "tips": "Old-school comfort."
    },

    "banana-toast": {
        "name": "Banana Toast",
        "category": "Breakfast",
        "time": "6 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍌",
        "ingredients": ["Bread", "Banana"],
        "steps": ["Slice banana", "Add on toast"],
        "tips": "Add honey if available."
    },

    "plain-pasta": {
        "name": "Plain Butter Pasta",
        "category": "Quick Meals",
        "time": "15 minutes",
        "difficulty": "Easy",
        "servings": "1",
        "image": "🍝",
        "ingredients": ["Pasta", "Butter", "Salt"],
        "steps": ["Boil pasta", "Add butter"],
        "tips": "Emergency hunger fix."
    },

    "boiled-veggies": {
        "name": "Boiled Veggies",
        "category": "Healthy",
        "time": "10 minutes",
        "difficulty": "Easy",
        "servings": "2",
        "image": "🥕",
        "ingredients": ["Veggies", "Salt"],
        "steps": ["Boil veggies", "Add salt"],
        "tips": "Diet mode ON."
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
