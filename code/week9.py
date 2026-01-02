# Part 1: Creating Basic Classes

class Musician:
    def __init__(self, name, instrument, skill_level):
        self.name = name
        self.instrument = instrument
        self.skill_level = skill_level

    def play(self):
        return f"{self.name} plays the {self.instrument}"

    def practice(self):
        if self.skill_level < 10:
            self.skill_level += 1

    def get_info(self):
        return f"{self.name} plays {self.instrument} at skill level {self.skill_level}"

# Testing Task 1.1
print("--- Task 1.1 ---")
musician1 = Musician("Aoife", "fiddle", 7)
print(musician1.play())
print(musician1.get_info())
musician1.practice()
print(musician1.get_info())
print()


# Part 2: Encapsulation

class Session:
    def __init__(self, location, max_capacity):
        # Private attributes denoted by __
        self.__location = location
        self.__max_capacity = max_capacity
        self.__musicians = []

    def add_musician(self, musician):
        if len(self.__musicians) < self.__max_capacity:
            self.__musicians.append(musician)
        else:
            print(f"Sorry, {self.__location} is at full capacity.")

    def remove_musician(self, name):
        # Searches for musician by name attribute and removes them
        self.__musicians = [m for m in self.__musicians if m.name != name]

    def get_musician_count(self):
        return len(self.__musicians)

    def list_musicians(self):
        for m in self.__musicians:
            print(m.get_info())

    def get_location(self):
        return self.__location

# Testing Task 2.1
print("--- Task 2.1 ---")
session = Session("The Cobblestone", 5)
session.add_musician(musician1)
session.add_musician(Musician("Liam", "guitar", 6))
session.list_musicians()
print(f"Musicians in session: {session.get_musician_count()}")
print()


# Part 3: Inheritance

class LeadMusician(Musician):
    def __init__(self, name, instrument, skill_level, specialty):
        # Use super() to initialize parent attributes
        super().__init__(name, instrument, skill_level)
        self.specialty = specialty

    def play(self):
        # Overriding the play method
        return f"{self.name} leads the session with {self.specialty} on {self.instrument}"

    def start_tune(self, tune_name):
        return f"{self.name} starts playing {tune_name}"

class BeginnersMusician(Musician):
    def __init__(self, name, instrument, skill_level):
        super().__init__(name, instrument, skill_level)
        self.learning = True

    def play(self):
        # Overriding the play method
        return f"{self.name} is learning to play the {self.instrument}"

    def graduate(self):
        self.learning = False
        self.skill_level = min(10, self.skill_level + 2)

# Testing Task 3.1
print("--- Task 3.1 ---")
lead = LeadMusician("Máire", "flute", 9, "slip jigs")
beginner = BeginnersMusician("Tom", "bodhrán", 3)

print(lead.play())
print(lead.start_tune("The Butterfly"))
print(beginner.play())
beginner.graduate()
print(f"{beginner.name} skill level: {beginner.skill_level}")
print()


# Part 4: Polymorphism

def hold_session(musicians):
    print("--- Session Starting ---")
    for musician in musicians:
        # Polymorphism: each object calls its own version of play()
        print(musician.play())
    print("--- Session Ending ---")

# Testing Task 4.1
print("--- Task 4.1 ---")
musicians_list = [
    Musician("Aoife", "fiddle", 7),
    LeadMusician("Máire", "flute", 9, "slip jigs"),
    BeginnersMusician("Tom", "bodhrán", 3)
]

hold_session(musicians_list)

"""
--- ANSWERS TO QUESTIONS ---

1. What advantages does encapsulation provide in the Session class?
Encapsulation protects the data (like the musician list and capacity) from being 
modified directly and incorrectly by external code. It ensures that changes only 
happen through defined methods (like add_musician), where we can enforce rules 
(like checking the max capacity).

2. How does inheritance help avoid code duplication between Musician classes?
Inheritance allows LeadMusician and BeginnersMusician to reuse the core logic 
already written in the Musician class (like name, instrument, and practice 
mechanics). We only have to write the unique features for each subclass rather 
than rewriting the entire class from scratch.

3. Give an example of polymorphism from this lab and explain why it's useful.
The hold_session() function is the primary example. It calls .play() on every 
object in the list. It doesn't need to check if the musician is a 'Lead' or 
'Beginner'; it just knows that every Musician has a play() method. This is 
useful because we can add new types of musicians in the future without ever 
having to change the hold_session() function.

4. What other real-world scenarios could you model using OOP?
OOP is perfect for modeling systems like:
- Banking (Account parent class, with Savings and Checking subclasses).
- E-commerce (Product parent class, with Clothing and Electronics subclasses).
- RPG Games (Character parent class, with Warrior and Mage subclasses).
- Library Systems (Media parent class, with Books and DVDs subclasses).
"""