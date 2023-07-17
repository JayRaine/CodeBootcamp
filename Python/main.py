from room import *
from character import *

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom = Room("ballroom")
ballroom.set_description("A large room made for fancy dancing.")
dining_hall = Room("dining hall")
dining_hall.set_description("A long table sits in the center of the room.")
dead = False

kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_convesation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tom = Enemy("Tom", "The talking tomato")
tom.set_convesation("Yup this is a bit weird but bare with it")
tom.set_weakness("pasta")
kitchen.set_character(tom)

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_convesation("Why hello there")
ballroom.set_character(catrina)

current_room = kitchen

while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant,Enemy):
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with)== True:
                print("Hooray, you won the fight!")
            else:
                print("Oh dear, toy lost the fight.")
                print("That is the end of the ganme")
                dead = True
        else:
            print("There is no one here to fight with")

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant,Enemy):
                print("I wouldn't do that is I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one to hug :(")
            
