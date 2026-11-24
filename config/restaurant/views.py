from django.shortcuts import render


MENU_ITEMS = [
    {
        "name": "Garden Harvest Salad",
        "description": "Greens, tomato, cucumber, lemon dressing",
        "price": "240",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=700&q=80",
    },
    {
        "name": "Chicken Burger",
        "description": "Crispy chicken patty with lettuce, cheese, and special sauce",
        "price": "250",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd"
    },
    {
        "name": "Roasted Tomato Soup",
        "description": "Tomatoes, basil, toasted bread",
        "price": "190",
        "image": "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=700&q=80",
    },
    {
        "name": "Garlic Herb Toast",
        "description": "Warm toast with garlic and herbs",
        "price": "160",
        "image": "https://images.unsplash.com/photo-1525351484163-7529414344d8?auto=format&fit=crop&w=700&q=80",
    },
    {
        "name": "Creamy Mushroom Pasta",
        "description": "Mushrooms, parmesan, creamy sauce",
        "price": "380",
        "image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=700&q=80",
    },
    {
        "name": "Margherita Pizza",
        "description": "Tomato, mozzarella, fresh basil",
        "price": "350",
        "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=700&q=80",
    },
    {
        "name": "Paneer Butter Masala",
        "description": "Paneer in a spiced tomato gravy",
        "price": "320",
        "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=700&q=80",
    },
    
    {
        "name": "Grilled Garden Sandwich",
        "description": "Grilled vegetables, cheese, herbs",
        "price": "230",
        "image": "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=700&q=80",
    },
    {
        "name": "Ember Veg Burger",
        "description": "House patty, lettuce, tomato, herb mayo",
        "price": "310",
        "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=700&q=80",
    },
    {
        "name": "Chickpea Coconut Curry",
        "description": "Chickpeas simmered in coconut milk",
        "price": "280",
        "image": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=700&q=80",
    },
    {
        "name": "Chocolate Cake",
        "description": "Chocolate sponge with cocoa ganache",
        "price": "180",
        "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=700&q=80",
    },
    {
        "name": "Caramel Pudding",
        "description": "Baked custard with caramel",
        "price": "150",
        "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=700&q=80",
    },
]
STAFF = [
    {"name": "JENIFER", "role": "Restaurant Manager"},
    {"name": "Priya Menon", "role": "Head Chef"},
    
]






def home(request):
    return render(request, "restaurant/home.html", {
        "menu_items": MENU_ITEMS,
        "staff": STAFF,
    })