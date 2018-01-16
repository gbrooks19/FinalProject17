print(f"Welcome to Crumbs. Yes or no questions should be answered with a Y or N.")
print("""
.
.
.
""")
print("""Her name is Stella. Stella has been in the coal mines for years.
She works in the deepest section of the mine; she has not seen daylight in months.
Her only source of light is the yellow orb that she was given by her father.
It is called a crumb.
""")

class Player(object):
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.crumbc = 1


    def move(self):
        a = input("""Would you like to go through a door? """)
        if a == "N":
            return
        if a == "Y":
            b = input(f"""
To move right, reply R
To move left, reply L
To move forward, reply F
To move backward, reply B
""")
        if self.xc == 0 and self.yc == 0 and b == "L" or "F" or "B":
            print("There is no door there. ")
        if self.xc == 1 and self.yc == 1 and b == "B":
            print("There is no door there. ")
        if self.xc == 1 and self.yc == -1 and b == "F":
            print("There is no door there. ")
        if self.xc == 2 and self.yc == 0 and b == "F" or "B":
            print("There is no door there. ")
        if self.xc == 3 and self.yc == 0 and b == "R" or "F":
            print("There is no door there. ")
        if self.xc == 3 and self.yc == -1 and b == "L" or "B":
            print("There is no door there. ")
        if self.xc == 4 and self.yc == -1 and b == "R" or "F" or "B":
            print("There is no door there. ")
        elif b == "R":
            self.xc += 1
        elif b == "L":
            self.xc += -1
        elif b == "F":
            self.yc += 1
        elif b == "B":
            self.yc += -1

    def location(self):
        print(f"The room has a slate on the cieling that reads: {player.xc}, {player.yc}")

    def roomdescribe(self):
        if self.xc == 0 and self.yc == 0:
            print("""
            The room is mostly barren.
            In the corner is a mysterious yellow orb that emits a faded light.""")
        if self.xc == 1 and self.yc == 0:
            print("""
            The room is mostly barren.
            In the center is a podium GREEN pertruding two feet from the ground.""")
        if self.xc == 1 and self.yc == 1:
            print("""
            The room is mostly barren.
            In the center is a podium YELLOW pertruding two feet from the ground.""")
        if self.xc == 1 and self.yc == -1:
            print("""
            The room is mostly barren.
            In the center is a podium BLUE pertruding two feet from the ground.
            """)
        if self.xc == 2 and self.yc == 0:
            print("""
            The room is mostly barren.
            In the center is a podium FAKE pertruding two feet from the ground.
            """)
        if self.xc == 3 and self.yc == 0:
            print("""
            The room is mostly barren.
            In the center is a podium RED pertruding two feet from the ground.
            """)
        if self.xc == 3 and self.yc == -1:
            print("""
            The room is mostly barren.
            """)
        if self.xc == 4 and self.yc == -1:
            print("""
            The room is mostly barren.
            In the center is a podium PINK pertruding two feet from the ground.
            """)

    def podium(self):
        if self.xc == 3 and self.yc == -1:
                print("There is no podium in this room")
        if self.xc == 0 and self.yc == 0:
                print("There is no podium in this room")
        else:
            b = input("Approach the podium?")
            if b == "N":
                return
            if b == "Y":
                print("""
You approach the podium
and the crumb in your bag begins to vibrate.
You place the crumb in the slot on the podium.""")
            if self.xc == 1 and self.yc == 1 and self.crumbc == 1:
                RIDDLE AND REWARD
            if self.xc == 1 and self.yc == 0 and self.crumbc == 2:
                RR
            if self.xc == 1 and self.yc == -1 and self.crumbc == 3:
                RR
            if self.xc == 4 and self.yc == -1 and self.crumbc == 4:
                RR
            if self.xc == 3 and self.yc == 0 and self.crumbc == 5:
                END

player = Player()
