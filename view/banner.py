from colorama import Fore
from pyfiglet import Figlet
from os import system, name
from time import sleep


f = Figlet(font='big')


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

    
def menu():
    sleep(0.05)
    print(Fore.RED + ' [' + Fore.WHITE + '#' + Fore.RED + ']' + Fore.BLUE + " Choose one of the options below\n")
    sleep(0.05)
    print(Fore.YELLOW + ' [1] Start new game')
    sleep(0.05)
    print(Fore.GREEN + ' [2] User Score')
    sleep(0.05)
    print(Fore.RED + ' [0] Exit...' + Fore.RESET)
    
    
def level():
    sleep(0.05)
    print(Fore.RED + ' [' + Fore.WHITE + '#' + Fore.RED + ']' + Fore.BLUE + " Choose your desired game level\n")
    sleep(0.05)
    print(Fore.YELLOW + ' [1] Easy')
    sleep(0.05)
    print(Fore.GREEN + ' [2] Medium')
    sleep(0.05)
    print(Fore.RED + ' [3] Hard')


def word(word, live, notin):
    sleep(0.3)
    system('cls' if name == 'nt' else 'clear')
    print(Fore.RED + f.renderText(str(word)))
    print(Fore.YELLOW + " The selected word has {} letters".format(len(word)))
    print(Fore.YELLOW + " The letters used so far " + Fore.WHITE + notin)
    print(Fore.YELLOW + " Remaining chance : {}".format('❤️' * live))


# Select user   
def select(text, title, logo):
    sleep(0.03) # 0.03s sleep
    try:
        # Print input text and turn it into number and return base
        return input(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "HANGMAN "+ Fore.GREEN + "~ " + Fore.BLUE + title + Fore.GREEN +" <<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + logo + Fore.RED +"] "+ Fore.YELLOW + text + Fore.RESET + " ")
    except:
        # In the event of incoming number
        return -1
    
 
def get_char(found, username, live, notin):
    word(found, live, notin)
    return select("Enter the character you want ", username, ':)')
 
    
# Select user   
def show(text, title, logo):
    sleep(0.03) # 0.03s sleep
    return print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "HANGMAN "+ Fore.GREEN + "~ " + Fore.BLUE + title + Fore.GREEN +" <<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + logo + Fore.RED +"] "+ Fore.YELLOW + text + Fore.RESET + " ")


def get_user_name():
    main_banner()
    return select('Enter your username ', 'USERNAME', '$')

    
# Print Good Bye :)
def bye():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "TIMER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "!" + Fore.RED +"] " + Fore.YELLOW + 'We hope you enjoy the game')


# Wrong Input
def wrong():
    print(Fore.RED + "\n ┌─[" + Fore.GREEN + ">> " + Fore.WHITE + "TIMER "+ Fore.GREEN +"<<" + Fore.RED + "]\n └──╼ [" + Fore.WHITE + "?" + Fore.RED +"] " + Fore.YELLOW + 'The input structure has not been observed !!')


def main_page(username):
    main_banner()
    menu()
    return select('', username, '#')