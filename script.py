
from random import randint
from time import sleep


ENEMEY_INFO = [
               {
                   "name": "モンスター1",
                   "status":
                   {
                       "hp": 10,
                       "atk": randint(1, 3),
                       "spd": 10,
                       "ex": 30
                   }
               },
               {
                   "name": "モンスター2",
                   "status":
                   {
                       "hp": 100,
                       "atk": randint(3, 15),
                       "spd": 20,
                       "ex": 50
                    }
                },
               {
                   "name": "モンスター3",
                   "status":
                   {
                       "hp": 150,
                       "atk": randint(15, 75),
                       "spd": 30,
                       "ex": 100
                    }
                }
               ]

def set_player():
    player_hp = randint(50, 100)
    player_atk = randint(20, 50)
    player_spd = randint(10, 30)
    player_name = input('あなたのモンスターの名前は？：')
    player_param = player_hp, player_atk, player_spd, player_name
    return player_param

def show_player(param):
    hp, atk, spd, name = param
    print("NAME: {0}".format(name))
    print("HP: {0}".format(hp))
    print("ATK: {0}".format(atk))
    print("SPD: {0}".format(spd))

def set_enemy():
    ene_index = randint(0, len(ENEMEY_INFO) - 1)
    enemy_info = ENEMEY_INFO[ene_index]
    ene_name = enemy_info["name"]
    ene_hp = enemy_info["status"]["hp"]
    ene_atk = enemy_info["status"]["atk"]
    ene_spd = enemy_info["status"]["spd"]
    ene_ex = enemy_info["status"]["ex"]
    enemy_param = ene_name, ene_hp, ene_atk, ene_spd, ene_ex
    return enemy_param

def calc_dmg(atk,from_who, to_who):
    total_atk = atk
    print("{0}は{1}に{2}のダメージを与えた!".format(from_who, to_who, total_atk))
    return total_atk

def judge(player_hp, enemy_hp):
    if player_hp < 0:
        ply_win_flag = False
    elif enemy_hp < 0:
        ply_win_flag = True
    return ply_win_flag