def greet():
    print("Hello Sir")


def greet_with_name(name):
    print("Hello "+name)

greet_with_name("Anup")

def greet_inDetails(name, city, nickname):
    print(f"Hi {name}, I'm gonna call you with your nickname.")
    print(f"{nickname}, is your nickname right!!")
    print(f"You're living in {city}")
    print(f"Hello {nickname} what's up")

greet_inDetails("Amlan", "Cuttack", "Papal")