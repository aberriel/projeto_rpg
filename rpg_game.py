import random


game_paths = {
    1: {
        'red': 2,
        'black': 3
    },
    2: {
        'red': 3,
        'black': 4
    },
    3: {
        'red': 4,
        'black': 5  
    },
    4: {
        'red': 5,
        'black': 6,
    },
    5: {
        'red': 6,
        'black': 7,
    },
    6: {
        'black': 8
    },
    7: {
        'red': 8,
        'black': 9
    },
    8: {
        'red': 9,
        'black': random.choice([1, 2, 3, 4, 5])
    }
}

actual_step = 1
step_count = 1

while True:
    if actual_step == 9:
        print('Você ganhou, gado do bozonero!!!')
        break
    elif step_count >= 7:
        print('YOU LOOOOOOOOSE!!!!!!!!!!!!!!!!!!!!')
        break
    
    print(f'Você está na sala: {actual_step}')
    print('Escolha seu caminho:')
    possible_paths = game_paths[actual_step]
    paths = list(possible_paths.keys())
    for path_index in range(len(paths)):
        print(f'[{path_index + 1}] - Caminho {paths[path_index]}')
    response = int(input())
    
    next_step_name = list(paths)[response - 1]
    actual_step = possible_paths[next_step_name]
    step_count = step_count + 1
