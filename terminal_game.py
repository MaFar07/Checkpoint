## Terminal Adventure Game
#Create a terminal_game.py that walks the player through a captivating mini-game adventure! In each step of the adventure, 
#the player should be presented with 2 or more options on where to go next.Be as creative as you want with this, but make sure your code runs!
#Some ideas include:
#A space-based adventure of a crew of curious individuals exploring an unknown galaxy.
#A “Day in the Life” story that walks you through choices the main character makes based on conditions like the time of day, the actions that the player take, etc.
#A classic mini-RPG (role-playing game) with hp health points, character moves like attack/block/heal, and NPCs (non-player characters) 
#that attacks based on a random number generator.

import random

# Función principal del juego
def mini_rpg():
    print('Hello, welcome to the fight world,\n'
          'Are you ready to begin?')
    
    answer = input('Y/N: ').lower()
    if answer == 'y':
        print('You selected yes, let\'s continue')
    elif answer == 'n':
        print('Coward')
        return
    else:
        print('Invalid letter')
        return

    player_moves = ['attack', 'block', 'heal']
    npc_moves = ['attack', 'double_punch', 'kick', 'jump', 'cut']
    
    player_hp = 100
    npc_hp = 100

    for _ in range(10):  
        player_move = random.choice(player_moves)
        npc_move = random.choice(npc_moves)
        
        print(f'\nRound {_+1}:')
        print(f'Player move: {player_move}')
        print(f'NPC move: {npc_move}')
        
        if player_move == 'attack':
            npc_hp -= 10
            print('Player attacks! NPC loses 10 hp.')
        elif player_move == 'block':
            player_hp += 5
            print('Player blocks! Gains 5 hp.')
        elif player_move == 'heal':
            player_hp += 15
            print('Player heals! Gains 15 hp.')
        
        if npc_move == 'attack':
            player_hp -= 5
            print('NPC attacks! Player loses 5 hp.')
        elif npc_move == 'double_punch':
            player_hp -= 10
            print('NPC double punches! Player loses 10 hp.')
        elif npc_move == 'kick':
            player_hp -= 2
            print('NPC kicks! Player loses 2 hp.')
        elif npc_move == 'jump':
            npc_hp += 5
            print('NPC jumps! Gains 5 hp.')
        elif npc_move == 'cut':
            player_hp -= 25
            print('NPC cuts! Player loses 25 hp.')

        
        print(f'Current player hp: {player_hp}')
        print(f'Current NPC hp: {npc_hp}')

        
        if player_hp <= 0:
            print('Player has been defeated!')
            return
        elif npc_hp <= 0:
            print('NPC has been defeated!')
            return
    
    
    if player_hp > npc_hp:
        print('Player wins!')
    elif npc_hp > player_hp:
        print('NPC wins!')
    else:
        print('It\'s a draw!')

mini_rpg()
