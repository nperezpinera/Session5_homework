print("You have become trapped in the Crete labyrinth.")
print("")
print("Find the exit by choosing the correct compass direction, or the minotaur will eat your limbs.")
print("")
print("If you lose all your limbs you will lose.")
print("")
nummove = 0
counter = 0
lives = 5
path = ["S","S","W","N","E","S"]
while True:
        while counter<6:
            if(path[counter]==input("Enter a direction: ")):
                counter+=1
                nummove+=1
            else:
                print("The minotaur caught you")
                if (lives == 5):
                    print("The minotaur ate your right arm! You run away and find yourself back where you started.")
                    lives -= 1
                    counter = 0
                    continue
                elif (lives == 4):
                    print("The minotaur ate your left arm! You run away and find yourself back where you started.")
                    lives -= 1
                    counter = 0
                    continue
                elif (lives == 3):
                    print("The minotaur ate your right leg! You run away and find yourself back where you started.")
                    lives -= 1
                    continue
                elif (lives == 2):
                    print("The minotaur ate your left leg! You run away and find yourself back where you started.")
                    lives -= 1
                    counter = 0
                    continue
                elif (lives == 1):
                    print("The minotaur ate you whole! You lose.")
                    break
        if(lives>0):
            print("You escaped with ", lives-1, " limbs!")
            if(lives==1):
                print("You are now just a human torso.")
            break
        else:
            break