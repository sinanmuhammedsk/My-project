import tkinter as tk
from tkinter import ttk, messagebox
import random

# Sample meal data
meals = {
    "Breakfast": ["Pancakes", "Omelette", "Smoothie", "Toast with Avocado"],
    "Lunch": ["Grilled Chicken Salad", "Pasta", "Veggie Stir-fry", "Burger"],
    "Dinner": ["Steak", "Soup with Bread", "Sushi", "Vegetarian Curry"],
    "Snacks": ["Fruit Salad", "Yogurt", "Nuts", "Cookies"]
}

# Function to get random meal
def suggest_meal(meal_type):
    if meal_type in meals:
        meal = random.choice(meals[meal_type])
        messagebox.showinfo(f"{meal_type} Suggestion", f"We suggest: {meal}")
    else:
        messagebox.showwarning("Error", "Meal type not found!")

# GUI setup
root = tk.Tk()
root.title("Smart Meal Planner")
root.geometry("600x400")
root.configure(bg="#f0f8ff")  # Alice Blue background

# Title
title = tk.Label(root, text="Smart Meal Planner", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

# Subtitle with your name and roll number
subtitle = tk.Label(
    root, 
    text="Designed by: Sinan Muhammed\nRoll No: 34", 
    font=("Arial", 12), 
    bg="#f0f8ff", 
    fg="#666"
)
subtitle.pack(pady=5)

# Dropdown for meal type
meal_type_label = tk.Label(root, text="Select Meal Type:", font=("Arial", 14), bg="#f0f8ff", fg="#333")
meal_type_label.pack(pady=10)

meal_type = tk.StringVar()
meal_type.set("Breakfast")  # Default value
meal_dropdown = ttk.Combobox(root, textvariable=meal_type, font=("Arial", 12), state="readonly")
meal_dropdown['values'] = list(meals.keys())
meal_dropdown.pack(pady=5)

# Suggest button
suggest_button = tk.Button(
    root, 
    text="Suggest Meal", 
    font=("Arial", 14), 
    bg="#4caf50", 
    fg="white", 
    activebackground="#45a049", 
    command=lambda: suggest_meal(meal_type.get())
)
suggest_button.pack(pady=20)

# Exit button
exit_button = tk.Button(
    root, 
    text="Exit", 
    font=("Arial", 14), 
    bg="#f44336", 
    fg="white", 
    activebackground="#e53935", 
    command=root.destroy
)
exit_button.pack(pady=10)

# Footer
footer = tk.Label(
    root, 
    text="Healthy meals, happy life!", 
    font=("Arial", 10, "italic"), 
    bg="#f0f8ff", 
    fg="#777"
)
footer.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
import random

# Sample meal data
meals = {
    "Breakfast": ["Pancakes", "Omelette", "Smoothie", "Toast with Avocado"],
    "Lunch": ["Grilled Chicken Salad", "Pasta", "Veggie Stir-fry", "Burger"],
    "Dinner": ["Steak", "Soup with Bread", "Sushi", "Vegetarian Curry"],
    "Snacks": ["Fruit Salad", "Yogurt", "Nuts", "Cookies"]
}

# Function to get random meal
def suggest_meal(meal_type):
    if meal_type in meals:
        meal = random.choice(meals[meal_type])
        messagebox.showinfo(f"{meal_type} Suggestion", f"We suggest: {meal}")
    else:
        messagebox.showwarning("Error", "Meal type not found!")

# GUI setup
root = tk.Tk()
root.title("Smart Meal Planner")
root.geometry("600x400")
root.configure(bg="#f0f8ff")  # Alice Blue background

# Title
title = tk.Label(root, text="Smart Meal Planner", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

# Subtitle with your name and roll number
subtitle = tk.Label(
    root, 
    text="Designed by: Sinan Muhammed\nRoll No: 34", 
    font=("Arial", 12), 
    bg="#f0f8ff", 
    fg="#666"
)
subtitle.pack(pady=5)

# Dropdown for meal type
meal_type_label = tk.Label(root, text="Select Meal Type:", font=("Arial", 14), bg="#f0f8ff", fg="#333")
meal_type_label.pack(pady=10)

meal_type = tk.StringVar()
meal_type.set("Breakfast")  # Default value
meal_dropdown = ttk.Combobox(root, textvariable=meal_type, font=("Arial", 12), state="readonly")
meal_dropdown['values'] = list(meals.keys())
meal_dropdown.pack(pady=5)

# Suggest button
suggest_button = tk.Button(
    root, 
    text="Suggest Meal", 
    font=("Arial", 14), 
    bg="#4caf50", 
    fg="white", 
    activebackground="#45a049", 
    command=lambda: suggest_meal(meal_type.get())
)
suggest_button.pack(pady=20)

# Exit button
exit_button = tk.Button(
    root, 
    text="Exit", 
    font=("Arial", 14), 
    bg="#f44336", 
    fg="white", 
    activebackground="#e53935", 
    command=root.destroy
)
exit_button.pack(pady=10)

# Footer
footer = tk.Label(
    root, 
    text="Healthy meals, happy life!", 
    font=("Arial", 10, "italic"), 
    bg="#f0f8ff", 
    fg="#777"
)
footer.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
