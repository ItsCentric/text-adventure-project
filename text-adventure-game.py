import time
import random

playerName = input("What is your name, brave adventurer?")
print("This begins the adventure of the infamous adventurer known as " + str(playerName) + "...")
inventory = []

def Victory():
    print("After killing the adventurer, you have decided you've had enough of this silly little adventure and decide to go back home.")
    exit(0)

def youLose(death):
    print(death)
    exit(0)

def trail():
    print("You skip by the house and head down the trail.")
    time.sleep(3)
    print("The trail comes to a dead end. As you begin to turn back, a noise comes from behind you in the nearby shrubbery.")
    time.sleep(3)
    print("What do you want to do? (sound, flee)")
    trailChoice = input(">")

    if trailChoice == "sound":
        check_out_sound()
    
    elif trailChoice == "flee":
        flee_from_dead_end()
    
    else:
        print("Please choose a valid choice.")

def house():
    print("You entered the house...")
    time.sleep(2)
    print("After exploring around the house for a while, you come across a chest.")
    print("What would you like to do? (chest, exit)")
    chestChoice = input(">")

    if chestChoice == "chest":
        print("You cautiously opened the chest.")
        time.sleep(2)
        print("In the chest you found the one piece!")
        time.sleep(3)
        print("You head back home to your gang of pirates, and finally conclude your 1000 episode anime.")

    elif chestChoice == "exit":
        print("You decide to head back outside the house and go down the trail.")
        time.sleep(3)
        trail()

    else:
        print("Please choose a valid choice.")

def rightPath():
    print("You take the right path...")
    time.sleep(3)
    print("A little ways down the trail you come across a house... ")
    time.sleep(3)
    house_or_trail = input("Enter the house or continue down the trail? (house, trail)")

    if house_or_trail == "house":
        house()
    
    elif house_or_trail == "trail":
        trail()
    
    else:
        print("Please choose a valid choice.")

def check_out_sound():
    print("You make your way over to the source of the noise...")
    time.sleep(3)
    print("It was an armed aggressive adventurer!")
    playerHP = 100
    Enemy = True
    enemyHP = 80

    while playerHP > 0 and enemyHP > 0:
        fightChoice = input("What would you like to do? (attack, guard)")
        time.sleep(2)
        guardStrength = 0
        if fightChoice == "attack":
            attackPower = random.randint(1, 11)
            print("You bare your fist and threw a punch, it did {damage} HP!".format(damage=attackPower))
            enemyHP = enemyHP - attackPower
            if enemyHP < 0:
                enemyHP = 0
            print("The opposing adventurer is now at " + str(enemyHP) + "health!")

            if enemyHP <= 0:
                Enemy = False
                print("You have successfully killed the opposing Adventurer!")
                Victory()

        elif fightChoice == "guard":
            guardStrength = random.randint(1, 6)
            print("You take your guard and brace for the incoming attack.")
        
        else:
            print("Please choose a valid option.")

        if Enemy:
            time.sleep(2)
            enemyAttack = random.randint(1, 11)
            if guardStrength > 0:
                enemyAttack = enemyAttack - guardStrength
            if enemyAttack < 0:
                enemyAttack = 0
            playerHP = playerHP - enemyAttack
            print("The opposing adventurer readied his blade and strikes. He hit you for {enemyDamage} damage!".format(enemyDamage=enemyAttack))
            time.sleep(2)
            print("You are now at {playerHealth} health.".format(playerHealth=playerHP))

            if playerHP <= 0:
                youLose("The enemy adventurer has bested you.")

def flee_from_dead_end():
    youLose("You attempt to flee, but the noise was actually an aggressive adventurer ready to pounce with a bow and arrow. He shot you down as you ran.")

def leftPath():
    print("You take the left path...")
    time.sleep(3)
    print("At the end of the trail you approach a dead end and hear the sound of rustling in the bushes near you...")
    time.sleep(3)
    dead_end = input("What will you do? (flee, check out the sound)")

    if dead_end == "flee":
        flee_from_dead_end()
    
    elif dead_end == "check out the sound":
        check_out_sound()
    
    else:
        print("Please choose a valid choice.")

def startAdventure():
    print("You start down the trail...")
    time.sleep(3)
    print("You come across a fork in the trail, the two paths lead either right or left.")
    time.sleep(3)
    pathChoice = input("Which path will you choose?")

    if pathChoice == "right":
        rightPath()
    
    elif pathChoice == "left":
        leftPath()

    else:
        youLose("Are you stupid? I said TWO paths, no more than that! You know what? I don't even think you deserve to play anymore. Goodbye!")

startAdventure()