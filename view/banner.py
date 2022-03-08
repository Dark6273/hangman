# Import needed library
from colorama import Fore
from pyfiglet import Figlet
from os import system, name
from time import sleep


f = Figlet(font='big')


# Main logo
def main_banner():
    system('cls' if name == 'nt' else 'clear')
    print(Fore.CYAN + """
          
 /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$      /$$  /$$$$$$  /$$   /$$
| $$  | $$ /$$__  $$| $$$ | $$ /$$__  $$| $$$    /$$$ /$$__  $$| $$$ | $$
| $$  | $$| $$  \ $$| $$$$| $$| $$  \__/| $$$$  /$$$$| $$  \ $$| $$$$| $$
| $$$$$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$| $$ $$/$$ $$| $$$$$$$$| $$ $$ $$
| $$__  $$| $$__  $$| $$  $$$$| $$|_  $$| $$  $$$| $$| $$__  $$| $$  $$$$
| $$  | $$| $$  | $$| $$\  $$$| $$  \ $$| $$\  $ | $$| $$  | $$| $$\  $$$
| $$  | $$| $$  | $$| $$ \  $$|  $$$$$$/| $$ \/  | $$| $$  | $$| $$ \  $$
|__/  |__/|__/  |__/|__/  \__/ \______/ |__/     |__/|__/  |__/|__/  \__/
        
          """)

    
# Print menu
def menu():
    sleep(0.05)
    print(Fore.RED + ' [' + Fore.WHITE + '#' + Fore.RED + ']' + Fore.BLUE + " Choose one of the options below\n")
    sleep(0.05)
    print(Fore.YELLOW + ' [1] Start new game')
    sleep(0.05)
    print(Fore.GREEN + ' [2] User Score')
    sleep(0.05)
    print(Fore.RED + ' [0] Exit...' + Fore.RESET)
    

# Print menu level
def level():
    sleep(0.05)
    print(Fore.RED + ' [' + Fore.WHITE + '#' + Fore.RED + ']' + Fore.BLUE + " Choose your desired game level\n")
    sleep(0.05)
    print(Fore.YELLOW + ' [1] Easy')
    sleep(0.05)
    print(Fore.GREEN + ' [2] Medium')
    sleep(0.05)
    print(Fore.RED + ' [3] Hard')


# Print Word and Input for get charcater
def word(word, live, notin): 
    sleep(0.3) # sleep 0.3 s
    system('cls' if name == 'nt' else 'clear') # Clear screen
    print(Fore.RED + f.renderText(str(word))) # Print character founded user
    print(Fore.YELLOW + " The selected word has {} letters".format(len(word))) # Len word
    print(Fore.YELLOW + " The letters used so far " + Fore.WHITE + notin) # Used character
    print(Fore.YELLOW + " Remaining chance : {}".format('❤️' * live)) # Count of live


# Select user   
def select(text, title, logo):
    sleep(0.03) # 0.03s sleep
    try:
        # Print input text and turn it into number and return base
        return input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "HANGMAN "+ Fore.GREEN + "~ " + Fore.BLUE + title + Fore.GREEN +" <<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + logo + Fore.RED +"] "+ Fore.YELLOW + text + Fore.RESET + " ")
    except:
        # In the event of incoming number
        return -1
    
 
 # Show box for get character and word
def get_char(found, username, live, notin):
    word(found, live, notin) # Print word
    return select("Enter the character you want ", username, ':)') # Input get charcter
 
    
# Select user   
def show(text, title, logo):
    sleep(0.03) # 0.03s sleep
    return print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "HANGMAN "+ Fore.GREEN + "~ " + Fore.BLUE + title + Fore.GREEN +" <<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + logo + Fore.RED +"] "+ Fore.YELLOW + text + Fore.RESET + " ")


# Show page for get username
def get_user_name():
    main_banner() # Main banner
    return select('Enter your username ', 'USERNAME', '$') # Get username from user

    
# Print Good Bye :)
def bye():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "TIMER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "!" + Fore.RED +"] " + Fore.YELLOW + 'We hope you enjoy the game')


# Wrong Input
def wrong():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "TIMER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'The input structure has not been observed !!')


# Print Main Menu 
def main_page(username):
    main_banner() # Main banner
    menu() # Print menu
    return select('', username, '#') # Get input from user