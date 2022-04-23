# 更新日志：保存用户的信息给minecraft_home.py

import os

Launcher = True
Game_start = False
username = ''
skin_name = ''
edition_name = ''
mod_name = ''
user_info = {}

def game_start_return_info():
    Game_start = True
    user_info['un'] = username
    user_info['sn'] = skin_name
    user_info['en'] = edition_name
    user_info['mn'] = mod_name
    return user_info

while Launcher:
    print(input('start\tskin\tusername\tchoose your edition\tset-up your edition'))
    if (input() == 'start'):
        if (username != '' and skin_name != ''):
            os.popen('D:/zcyh/编程文件夹/VSC测试/脑洞大开哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈/Minecraft/.minecraft/toaruZhang-plus/home/minecraft_home.py')
            game_start_return_info()
            break
        elif (username == ''):
            print("You wasn't tell us your username.")
        elif (skin_name == ''):
            print("You wasn't tell us your skin-name.")
        elif (edition_name == ''):
            print("You wansn't tell us your edition-name.")
        else:
            input('Your Launcher Has Other Question. Please Create An Issues On https://github.com/mfuns-zhangtongxue/toaruZhang-Minecraft .')
    elif (input() == 'skin'):
        print(input('Please input the name of your skin.'))
        skin_name = input()
    elif (input() == 'username'):
        print(input('Please input your username.'))
        username = input()
    elif (input() == 'choose your edition'):
        print(input("Input your edition name."))
        if (input() == '1.0.0'):
            print('Okay.')
    elif (input() == 'skin'):
        print(input("add mod"))
        if (input() == 'add mod'):
            print(input('input your mod name.'))
            if (input() == 'Tinkers Construct'):
                mod_name = input()
            else:
                print('Please enter the officially designated mods.')
    else:
        continue