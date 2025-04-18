class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} just ate. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy: {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played around. Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play. Let them sleep!")

   # We thought we should spice up the game a bit and add an auto-feed feature.
    # This will be triggered when the hunger reaches 10.
    def check_auto_feed(self):
        if self.hunger == 10:
            print(f"{self.name} reached max hunger! Auto-feeding... 🍽️")
            self.eat()
            self.happiness = min(10, self.happiness + 1)  # Happiness boosts from eating
            self.energy = max(0, self.energy - 1)  # Energy lowers after eating
            print(f"{self.name} is full and happier, but a lil tired now. Energy: {self.energy}")


    def get_status(self):        
        print(f"\n Status of {self.name} ")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10\n")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick} ")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s Tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn’t learned any tricks yet.")
