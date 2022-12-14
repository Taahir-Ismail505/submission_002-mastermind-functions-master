import random


# TODO: Decompose into functions
correct = False
turns = 0
code = [0,0,0,0]
answer= ""
###############################################################################

'''
when you use global always put it at the top first 
for def combo ..its a function generating a code 
'''
def code_combo():
    global code
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    #print(code)  
###############################################################################
'''
takes the user input and stores it in a variable
'''
def Userinput():
    global answer
    answer= ""
    answer = input("Input 4 digit code: ")

'''
takes the combo and user input and does the comparing and changes the values of correct and turns
'''
def str_comp():
    global correct
    correct = False
    global turns
    turns = 0
    while not correct and turns < 12:
        Userinput()
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            continue
        correct_digits_and_position = 0
        correct_digits_only = 0
        for i in range(len(answer)):
            if code[i] == int(answer[i]):
                correct_digits_and_position += 1
            elif int(answer[i]) in code:
                correct_digits_only += 1

        print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
        print('Number of correct digits not in correct place: '+str(correct_digits_only))
        turns += 1

        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))

    print('The code was: '+str(code))
###############################################################################
#runs all functions in order 

def run_game():
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    code_combo()
    str_comp()

if __name__ == "__main__":
    run_game()