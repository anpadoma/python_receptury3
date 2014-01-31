from functools import total_ordering
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width

@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}: {} stóp kwadratowych {}'.format(self.name, 
                                              self.living_space_footage, 
                                              self.style)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage 



# Tworzenie kilku domów i dodawanie do nich pomieszczeń
h1 = House('h1', 'Na wzgórzu')
h1.add_room(Room('Główna sypialnia', 14, 21))
h1.add_room(Room('Salon', 18, 20))
h1.add_room(Room('Kuchnia', 12, 16))
h1.add_room(Room('Gabinet', 12, 12))

h2 = House('h2', 'Ranczo')
h2.add_room(Room('Główna sypialnia', 14, 21))
h2.add_room(Room('Salon', 18, 20))
h2.add_room(Room('Kuchnia', 12, 16))

h3 = House('h3', 'Bliźniak')
h3.add_room(Room('Główna sypialnia', 14, 21))
h3.add_room(Room('Salon', 18, 20))
h3.add_room(Room('Gabinet', 12, 16))
h3.add_room(Room('Kuchnia', 15, 17))
houses = [h1, h2, h3]

print("Czy h1 jest większy od h2?", h1 > h2) # Wyświetla True
print("Czy h2 jest mniejszy od h3?", h2 < h3) # Wyświetla True
print("Czy h2 jest większy lub równy względem h1?", h2 >= h1) # Wyświetla False
print("Który dom jest największy?", max(houses)) # Wyświetla 'h3: 1101 stóp kwadratowych Bliźniak'
print("Który dom jest najmniejszy?", min(houses)) # Wyświetla 'h2: 846 stóp kwadratowych Ranczo'
