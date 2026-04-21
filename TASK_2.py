# Smart Traffic Signal Timer Advisor

def traffic_advisor(vehicle_count):
    if vehicle_count < 0 or vehicle_count > 100:
        return "Invalid input! Please enter a value between 0 and 100."
    if vehicle_count <= 20:
        density = "Low"
        green_time = 20
        advice = "Traffic is light. Proceed smoothly."   
    elif vehicle_count <= 50:
        density = "Medium"
        green_time = 45
        advice = "Maintain steady speed and follow lane discipline."
    else:
        density = "High"
        green_time = 70
        advice = "Heavy traffic ahead. Be patient and avoid sudden moves."
    result = f"""
Traffic Analysis:
Traffic Density: {density}
Suggested Green Signal Time: {green_time} seconds
Advice: {advice}
"""
    return result

try:
    vehicles = int(input("Enter number of vehicles waiting: "))
    output = traffic_advisor(vehicles)
    print(output)

except ValueError:
    print("Invalid input! Please enter a numeric value.")	
