#The introduction and rueles are stated
print("""
All yes or no questions are to be answered with Y or N.
Her name is Stella. Stella has been in the coal mines for years.
She works in the deepest section of the mine; she has not seen daylight in months.
""")
#The player class, which includes all function for gameplay, is created
class Player(object):
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.orbc = 1
#The final scene was created last, but I moved it up here becaused it needed to be used inside of another function that is not defined till later on
    def final(self):
        while True:
            print("""
Stella remembers one night when she was home alone. Temperatures
were falling quickly and night was approaching. She wants to
light a lamp, the fireplace, and the stove, but she only has
one match.
""")
            p = input("""
What will she light first? (Answers should be one word)
""")
            if p != "match":
                print("Incorrect. Try again")
            if p == "match":
                print("""
The now colorless orb suddenly emits a blinding light. When
the light fades, Stella is on the surface on the shore of a lake.
Congratulations, you have completed the game!
""")
                player.xc = 10
                return
#This command was created to allow for the movement of the player from room to room
    def move(self):
        a = input("""Would you like to go through a door? """)
        if a == "N":
            return
        if a == "Y":
            b = input("""
To move right, reply R
To move left, reply L
To move forward, reply F
To move backward, reply B
""")
#Boundaries are determined by preventing the player from moving to rooms that do not exist
#If the movement does not violate a boundary, the player's coordinates are changed
        if self.xc == 0 and self.yc == 0 and b == "L":
            print("There is no door there. ")
        elif self.xc == 0 and self.yc == 0 and b == "F":
            print("There is no door there. ")
        elif self.xc == 0 and self.yc == 0 and b == "B":
            print("There is no door there. ")
        elif self.xc == 1 and self.yc == 1 and b == "F":
            print("There is no door there. ")
        elif self.xc == 1 and self.yc == 1 and b == "L":
            print("There is no door there. ")
        elif self.xc == 1 and self.yc == 1 and b == "R":
            print("There is no door there. ")
        elif self.xc == 1 and self.yc == -1 and b == "L":
            print("There is no door there. ")
        elif self.xc == 1 and self.yc == -1 and b == "R":
            print("There is no door there. ")
        elif self.xc == 1 and self.yc == -1 and b == "B":
            print("There is no door there. ")
        elif self.xc == 2 and self.yc == 0 and b == "F":
            print("There is no door there. ")
        elif self.xc == 2 and self.yc == 0 and b == "B":
            print("There is no door there. ")
        elif self.xc == 3 and self.yc == 0 and b == "R":
            print("There is no door there. ")
        elif self.xc == 3 and self.yc == 0 and b == "F":
            print("There is no door there. ")
        elif self.xc == 3 and self.yc == -1 and b == "L":
            print("There is no door there. ")
        elif self.xc == 3 and self.yc == -1 and b == "B":
            print("There is no door there. ")
        elif self.xc == 4 and self.yc == -1 and b == "R":
            print("There is no door there. ")
        elif self.xc == 4 and self.yc == -1 and b == "F":
            print("There is no door there. ")
        elif self.xc == 4 and self.yc == -1 and b == "B":
            print("There is no door there. ")
        elif b == "R":
            self.xc += 1
        elif b == "L":
            self.xc += -1
        elif b == "F":
            self.yc += 1
        elif b == "B":
            self.yc += -1
        else:
            print("Invalid Input.")
#A function for stating the location of the player was made
    def location(self):
        print(f"""
The room has a slate on the cieling that reads: {player.xc}, {player.yc}
""")
#A function for stating the description of the room was made
#If the orb matches the podium in this room, the riddle is given
#If the riddle is answered correctly, the color of the orb is changed
    def roomdescribe(self):
        if self.xc == 0 and self.yc == 0:
            print("""
The room is mostly barren.
In the corner is a mysterious yellow orb that emits a faded light.
You pick up the orb and place it in your backpack.
""")
        if self.xc == 1 and self.yc == 0:
            print("""
The room is mostly barren.
In the center is a podium pertruding two feet from the ground.
""")
        if self.xc == 1 and self.yc == 1:
            print("""
The room is mostly barren.
In the center is a podium pertruding two feet from the ground.
""")
        if self.xc == 1 and self.yc == -1:
            print("""
The room is mostly barren.
In the center is a podium pertruding two feet from the ground.
""")
        if self.xc == 2 and self.yc == 0:
            print("""
The room is mostly barren.
In the center is a podium pertruding two feet from the ground.
""")
        if self.xc == 3 and self.yc == 0:
            print("""
The room is mostly barren.
In the center is a podium pertruding two feet from the ground.
""")
        if self.xc == 3 and self.yc == -1:
            print("""
The room is mostly barren.
In the center is a podium pertruding two feet from the ground.
""")
        if self.xc == 4 and self.yc == -1:
            print("""
The room is mostly barren.
In the center is a podium pertruding two feet from the ground.
""")

    def podium(self):
        b = input("Approach the podium? ")
        if b == "N":
            return
        if b == "Y":
            print("""
You approach the podium
and the orb in your bag begins to vibrate.
You place the orb in the slot on the podium.
""")
        if b != "Y" and b != "N":
            print("Invalid Input.")
            return
        if self.xc == 1 and self.yc == 1 and self.orbc == 1:
            print("""
You place the yellow orb in the slot in the podium.

She had not seen daylight in months.
The only way she tells time is by the 12 hour digital
clock in her living quarters
""")
            d = input("""
How many times over the course of one day
does the clock display three or more of the same digits in a row?
""")
            if d == "34":
                self.orbc += 1
                print("""
The podium collapses and the orb turns to a bright
green. You place it back in your backpack
""")
            else:
                print("""
The podium makes no response, your answer is incorrect.
""")
        if self.xc == 1 and self.yc == 0 and self.orbc == 2:
            print("""
You place the green orb in the slot in the podium.

Stella remembers when her life was easy, before they lost the farm.
Stella and her brother Louis are given the chore of plowing a
rectangular ten acre plot for their father. They divide the plot
in half so they can work independently. Stella starts from one end
of the plot, while Louis starts from the other. They both work
towards the center of the plot. Stella works at 20 minutes per acre
before she plants. Louis works at 40 minutes per acre but plants
at three times Stella's speed. Their father gives them $100 to split
proportionally.

Stella remembers those memories fondly. She reaches into her backpack
and pulls out the money she made that day.
""")
            d = input("""
How many dollars is she holding?
""")
            if d == "50":
                self.orbc += 1
                print("""
The podium collapses and the orb turns to a pale blue. You place it back in your backpack
""")
            else:
                print("""
The podium makes no response, your answer is incorrect.
""")
        if self.xc == 1 and self.yc == -1 and self.orbc == 3:
            print("""
You place the blue orb in the slot in the podium.

Stella suddenly begins to feel nauseas. Her vision begins to narrow
and she cannot think clearly. She has forgotten to take her
medicine. She remembers that they had lost the farm because they
had spent all of their money on the medicine for Stella's memory
decay.

Stella recieves 10 pills from her doctor. She must take one each
day. They all have different dosages but are not labeled, so she
decides to number them now before they get mixed up.
""")
            d = input("""
What is the minimum number of pills Stella can number and still
remember the order in which to take them?
""")
            if d == "8":
                self.orbc += 1
                print("""
The podium collapses and the orb turns to a bold pink. You place it back in your backpack
""")
            else:
                print("""
The podium makes no response, your answer is incorrect.
""")
        if self.xc == 4 and self.yc == -1 and self.orbc == 4:
            print("""
You place the pink orb in the slot in the podium.

Suddenly, the pill begins to kick in and an old memory of her and
Louis floods back.

[Louis]: "You know Stella, if I took away two years from my age
and gave them to you, you would be twice my age!

[Stella]: "Why don't you just give me one more on top of that,
then I'd be three times your age!

Stella cannot remember when this memory is from.
""")
            d = input("""
How old was Stella when this happened?
""")
            if d == "6":
                self.orbc += 1
                print("""
The podium collapses and the orb turns to a blood red. You place it back in your backpack
""")
            else:
                print("""
The podium makes no response, your answer is incorrect.
""")
        if self.xc == 3 and self.yc == 0 and self.orbc == 5:
            print("""
You place the red orb in the slot in the podium.

Deep, red light fills the room she is in. She recognizes this
room as the room she was in when she first entered the mine. The
familiar odor and squeak of mice is horridly nostalgic.

A certain mouse can give birth once a month, baring 12 babies each
time. Assuming half of the mice it bares are females, they will
mature and be able to give birth on their own after two months.
""")
            d = input("""
If you were to buy a female mouse of this species, how many mice
would you have after eleven months?
""")
            if d != "1":
                print("""
The podium makes no response, your answer is incorrect.
""")
            if d == "1":
                print("""
Suddenly the room goes dark, and Stella begins to panic.
""")
                player.final()
        else:
            print("The orb makes no response.")

#A player is created
player = Player()
#A loop that allows for the cycle of these functions was created so that gameplay could technically last forever up until the game is completed.
while True:
    player.location()
    player.roomdescribe()
    player.podium()
    if player.xc == 10:
        break
    player.move()

