# Daily Water Intake Tracker
def check_hydration(intake):
    recommended = 2.0 
    if intake < 0:
        return "Invalid input! Water intake cannot be negative."
    elif intake == 0:
        return "You haven't consumed any water today. Please drink water!"
    elif intake < recommended:
        return "Under-hydrated\nYou need to drink more water."
    elif intake == recommended:
        return "Adequately Hydrated\nGood job! You are meeting your daily water requirement."
    elif intake <= 5:
        return "Over-hydrated\nYou may be drinking more than required. Maintain balance."
    else:
        return "Unrealistic input! Please enter a value between 0 and 5 liters."

try:
    water_intake = float(input("Enter water consumed today (in liters): "))
    result = check_hydration(water_intake)
    print("\nHydration Status:")
    print(result)

except ValueError:
    print("Invalid input! Please enter a numeric value.")