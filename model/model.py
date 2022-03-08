import view.banner as banner
from sys import exit
from time import sleep
from random import choice


USERNAME = ''
WORD = ''
FOUND = ''
LIVE = 6


def get_user_name():
    global USERNAME
    USERNAME = banner.get_user_name()
    
    with open('data/score') as f:
        users = f.readlines()
    users = [user.strip() for user in users]
    users = [user.split(',')[0] for user in users]
    
    if USERNAME not in users:
        file = open('data/score', 'a+')
        file.write(USERNAME+',0,0\n')
        file.close()
        banner.show('The user successfully added', USERNAME, '@')
        sleep(1.5)


def reset():
    global WORD, FOUND, LIVE
    WORD = ''
    FOUND = ''
    LIVE = 6


def write(users):
    file = open('data/score', 'w')
    for user in users:
        text = user[0] + ',' + str(user[1]) + ',' + str(user[2]) + '\n'
        file.write(text)
    reset()
    

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


def get_char(char):
    global FOUND,LIVE
    while LIVE > 0 and WORD != FOUND:
        print(WORD)
        if char in WORD:
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
        else:
            LIVE -= 1
        print(FOUND)
        if LIVE > 0 and WORD != FOUND:
            get_char(banner.get_char(FOUND, USERNAME, LIVE))
    
    if LIVE > 0:
        banner.word(WORD, LIVE)
        banner.show('good job. you win', USERNAME, ':)')
        sleep(1)
        win()
        main()
    else:
        banner.word(WORD, LIVE)
        banner.show('Unfortunately you lost', USERNAME, ':(')
        sleep(1)
        lose()
        main()
        

def start_game():
    global WORD,FOUND
    with open('data/words') as f:
        words = f.readlines()
    words = [w.strip() for w in words]
    try:
        banner.level()
        level = int(banner.select('', USERNAME, '?'))
    except:
        level = -1
        
    if level == 1:
        word = choice(words)
        while len(word) > 5:
            word = choice(words)
    elif level == 2:
        word = choice(words)
        while len(word) > 10:
            word = choice(words)
    elif level == 3:
        word = choice(words)
        while len(word) < 5:
            word = choice(words)
    else:
        wrong()
    
    WORD = word
    for i in word:
        FOUND += '-'
    
    banner.show('The game has been successfully created', USERNAME, '!')    
    sleep(1)
    get_char(banner.get_char(FOUND, USERNAME, LIVE))


def score():
    with open('data/score') as f:
        users = f.readlines()
    users = [user.strip() for user in users]
    users = [user.split(',') for user in users]
    
    for user in users:
        if USERNAME == user[0]:
            users = user
            pass
        
    banner.show('The user has >> {} wins << and >> {} lost <<'.format(users[1], users[2]), USERNAME, '#')
    sleep(3)
    main()


def bye():
    banner.bye()
    sleep(1)
    exit()


def wrong():
    banner.wrong()
    sleep(0.7)
    main()
    

def main():
    try:
        select = int(banner.main_page(USERNAME))
    except:
        select = -1
    
    if select == 1:
        start_game()
    elif select == 2:
        score()
    elif select == 0:
        bye()
    else:
        wrong()