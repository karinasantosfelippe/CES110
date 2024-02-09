'''
Author: Karina Santos Felippe
Version: 1.8

Exceeding requirements: 
- For any choice the user write wrong a function will be called to count how many wrong answers was given and print a invalid response message. If the user input 2 or more wrong answers a warning message will be printed.
- Also, there is a choice in the second level which provide a possibility to restart the game.

'''

print("\nYou are now playing an Adventure Game!")
response = ""
wrong_count = 0

def wrong_choice(count):
    count += 1
    print("\nInvalid response! Please try again.")
    return count

while True:
    response = input("\nDo you need an explanation about how to play this game? (YES or NO) ").lower()

    if response == 'yes':
        print("\nThe system will tell you a story and provide a decision to move on. You need to write a valid answer (the ALL CAPS choices in the sentence) to progress, and the story will change according your decision.\n")
    elif response != 'no':
        wrong_count = wrong_choice(wrong_count)
        if wrong_count >= 2:
            print("You need to write a valid answer (the ALL CAPS choices in the sentence) to progress.")
        continue
    
    response = input("Do you want to PLAY or QUIT? ").lower()
    # LEVEL 1 - Steps for PLAY choice
    if response == 'play':
        print("\nYou are now in Amazonia, Brazil.\nIt's a sunny and warm day, through the window you feel a strong wind coming.")

        response = input("Do you CLOSE the window or go OUTSIDE to see what's going on? ").lower()
        # LEVEL 2 - Steps for OUTSIDE choice 
        if response == 'outside':
            print("\nOutside you see a man who seems to be a local resident.")
            response = input("You go TALK to him about what is going on, you just IGNORE the man and keep moving into the forest, or you go BACK inside because you are scared? ").lower()

            # LEVEL 3 - Steps for TALK choice
            if response == 'talk':
                print("\nHe explain to you there is a child tale about a boy called Saci-Perere - a single-legged dark-skinned boy who wears a red hood and transports himself on a mini hurricane.")
                print('"You don`t need to worry! If you take care of nature he will be very kind!" - said the man.\n\nThe End!')
                break
            # LEVEL 3 - Steps for IGNORE choice
            elif response == 'ignore':
                print("\nYou keep walking and find a child (single-legged dark-skinned boy wearing a red hat) looking to you. He seems to be kind and gently ask:")
                print('- "This is my home, please be careful!"\n\nThe End!')
                break
            # LEVEL 3 - Steps for BACK choice
            elif response == 'back':
                print("\nA feel minutes later, the wind stop, and you don't need to be afraid because you are safe!")
                print("\nThe End!")
                break
            # LEVEL 3 - If user write a wrong choice
            else:
                wrong_count = wrong_choice(wrong_count)
                continue
        # LEVEL 2 - Steps for CLOSE choice
        elif response == 'close':
            print("\nA feel minutes later, the wind stop and you don`t know what happened.")
            response = input("\nAren't you curious about what started the strong wind? (Tap YES if you want to restart the game to discover what happened): ").lower()
            if response == 'yes':
                continue
            print("\nThe End!")
            break
        # LEVEL 2 - If user write a wrong choice
        else:
            wrong_count = wrong_choice(wrong_count)
            continue

    # LEVEL 1 - Step for QUIT choice
    elif response == 'quit':
        print("\nOk! See you next time!")
        break
    # LEVEL 1 - If user write a wrong choice
    else:
        wrong_count = wrong_choice(wrong_count)
        continue