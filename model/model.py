# Import needed library
import view.banner as banner
from sys import exit
from time import sleep
from random import choice

# Define variable
USERNAME = ''
WORD = ''
FOUND = ''
LIVE = 6
NOTIN = ''


# Get username and check in score file
def get_user_name():
    global USERNAME
    USERNAME = banner.get_user_name() # Get username
    
    with open('data/score') as f: # Read data from score file
        users = f.readlines()
    users = [user.strip() for user in users] # Remove \n
    users = [user.split(',')[0] for user in users] # split as , 
    
    if USERNAME not in users: # If the user did not exist
        file = open('data/score', 'a+') # Open file as a+
        file.write(USERNAME+',0,0\n') # Write a new user
        file.close() # Close file
        banner.show('The user successfully added', USERNAME, '@') # Show banner add user
        sleep(1) # Sleep 1s 


# Reset global variables
def reset():
    global WORD, FOUND, LIVE
    WORD = ''
    FOUND = ''
    LIVE = 6


# Write new data in score fine
def write(users):
    file = open('data/score', 'w') # Open file as w
    for user in users:
        text = user[0] + ',' + str(user[1]) + ',' + str(user[2]) + '\n'
        file.write(text) # Wrinte in File
    reset() # Call reser function
    

# Update score user
def win():
    user = ['', '', '']
    with open('data/score') as f:
        users = f.readlines()
    users = [user.strip().split(',') for user in users]
    for i in users:
        if i[0] == USERNAME:
            user = i
            temp = i
    user[1] = int(user[1]) + 1
    users[users.index(temp)] = user
    write(users)


# Update score user
def lose():
    user = ['', '', '']
    with open('data/score') as f:
        users = f.readlines()
    users = [user.strip().split(',') for user in users]
    for i in users:
        if i[0] == USERNAME:
            user = i
            temp = i
    user[2] = int(user[2]) + 1
    users[users.index(temp)] = user
    write(users)


# Check character if exist in word or not exist
def get_char(char):
    global FOUND, LIVE, NOTIN
    
    while LIVE > 0 and WORD != FOUND:
        if char in WORD: # If exist in word 
            count = 0
            ls = list(FOUND)
            text = ''
            for i in WORD:
                if i == char:
                    ls[count] = char
                count += 1
            for i in ls:
                text += i
            FOUND = text
        else: # If not exist
            LIVE -= 1
            
        if len(NOTIN) > 0:
            NOTIN += '-' + char
        else:
            NOTIN += char
        if LIVE > 0 and WORD != FOUND:
            get_char(banner.get_char(FOUND, USERNAME, LIVE, NOTIN))
    
    if LIVE > 0: # If win user
        banner.word(WORD, LIVE, NOTIN) # Show word banner
        banner.show('good job. you win', USERNAME, ':)') # Print win text
        sleep(1) # Sleep 1s
        win() # Call win function
        main() # Call main function
    else:  # If lose user
        banner.word(WORD, LIVE, NOTIN) # Show word banner
        banner.show('Unfortunately you lost', USERNAME, ':(') # Print lose text
        sleep(1) # Sleep 1s
        lose() # Call lose function
        main() # Call main funciton
        

# Start game and Choice word
def start_game():
    global WORD,FOUND
    with open('data/words') as f: # Read words in file words
        words = f.readlines()
    words = [w.strip() for w in words] # Remove \n
    try: # Try get int level
        banner.level()
        level = int(banner.select('', USERNAME, '?'))
    except:
        level = -1
        
    if level == 1: # len word < 5
        word = choice(words)
        while len(word) > 5:
            word = choice(words)
    elif level == 2: # len word < 10
        word = choice(words)
        while len(word) > 10:
            word = choice(words)
    elif level == 3: # len word > 10
        word = choice(words)
        while len(word) < 5:
            word = choice(words)
    else: # Wrong input
        wrong()
    
    WORD = word
    for i in word:
        FOUND += '-'
    
    banner.show('The game has been successfully created', USERNAME, '!')# Start game and
    sleep(1) # Sleep 1s
    get_char(banner.get_char(FOUND, USERNAME, LIVE, NOTIN)) # Call function from banner file


# Get score data
def score():
    with open('data/score') as f: # Open file score and read lines
        users = f.readlines()
    users = [user.strip() for user in users] # Remove \n
    users = [user.split(',') for user in users] # Split ,
    
    for user in users: # Find user
        if USERNAME == user[0]:
            users = user
            pass
        
    banner.show('The user has >> {} wins << and >> {} lost <<'.format(users[1], users[2]), USERNAME, '#') # Call score banner
    sleep(3) # Sleep 3s
    main() # Call main function


# bye function for exit game
def bye():
    banner.bye() # Show bye banner
    sleep(1) # Sleep 1s
    exit() # Exit from app


# Wrong banner if user select false option
def wrong():
    banner.wrong() # Call wrong banner
    sleep(0.7) # Sleep 0.7s
    main() # Call main
    

# Main function
def main():
    try: # Try get int from user
        select = int(banner.main_page(USERNAME))
    except:
        select = -1
    
    if select == 1: # user select 1 start game
        start_game()
    elif select == 2: # user select 2 show score
        score()
    elif select == 0: # user select 0 exit app
        bye()
    else: # user false select
        wrong()