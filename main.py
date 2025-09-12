import random

def get_weather(location):
    conditions = ["sunny", "cloudy", "rainy", "stormy", "foggy"]
    temp = random.randint(10, 25)
    return f"Today in {location}: {temp}°C, {random.choice(conditions)}."

def main():
    print("Weathered Notes ☁️")
    print("-------------------")
    city = input("Enter your city: ")
    print(get_weather(city))
    note = input("Add a note for today: ")
    print(f"Note saved: {note}")

if __name__ == "__main__":
    main()
