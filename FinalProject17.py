print(f"Welcome to Crumbs, Stella")
print("""
.
.
.
""")
print("""Her name is Stella. Stella has been in the coal mines for years.
She works in the deepest section of the mine; she has not seen daylight in months.""")
xc = 0
yc = 0

class room(object):
    def __init__(self, xc, yc):
        self.xc = xc
        self.yc = yc

room00 = room(0, 0)
room10 = room(1, 0)
room11 = room(1, 1)
room1n1 = room(1, -1)
room20 = room(2, 0)
room30 = room(3, 0)
room3n1 = room(3, -1)
room4n1 = room(4, 1)



def move():
    a = input("Would you like to go through a door?")
    if a == yes:
        b = input(f"Would you like to go {doors.join(, or )}? ")
    if no:
        break

move()