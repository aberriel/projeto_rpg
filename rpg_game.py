import random


player_name = input ('Olá Jogador, diga seu nome para darmos inicio a jornada! \n Digite seu Nickname:')

print (f"   \n  Muito bem {player_name}! Você será nosso líder nessa aventura!\
        \n  Somos a guilda 'Zero a esquerda ' e estamos prestes a começar mais uma missão\
        \n  Nós temos as seguintes informações sobre essa dungeon:\
        \n 1 - Ela é um labirinto formado por conjunto de salões interligados!\
        \n 2 - Que em um dos salões existe um loot lendário\
        \n 3 - Existe uma armadilha que mata qualquer um que vasculhar mais de 7 salões durante a busca")


game_paths = {
    1: {
        'Escada de sangue': 2,
        'Corredor apertado': 3
    },
    2: {
        'Passagem estreita': 3,
        'Corredor de pedras afiadas': 4
    },
    3: {
        'passagem com pêndulos cortantes': 4,
        'Porta da esquerda': 5  
    },
    4: {
        'Porta principal': 5,
        'Túnel flamejante': 6,
    },
    5: {
        'Portão infernal': 6,
        'Buraco na parede': 7,
    },
    6: {
        'Salão principal': 8
    },
    7: {
        'Buraco no chão': 8,
        'Caminho do tapete Azul': 9
    },
    8: {
        'Caminho do tapete Roxo': 9,
        'Porta brilhante': random.choice([1, 2, 3, 4, 5])
    }
}

room_joke = {
    1: 'Bem vindo!',
    2: 'Se sujou de sangue atoa, não tem nada aqui :(',
    3: 'Se estreitou demais por nada, somente caixas vazias aqui',
    4: 'Muitos cortes para pouca recompensa, hora de se curar',
    5: 'Caminho entediante em resultado entediante, nada aqui',
    6: '3 integrantes da guilda morreram queimados na última passagem',
    7: 'Maneiro encontramos alguns suprimentos e pão de queijo aqui... Vai um cafézinho?',
    8: 'Cuidado, nem tudo que reluz é ouro'


}

while True:
    actual_step = 1
    step_count = 0


    while True:
        if actual_step == 9:
            print('Encontramos o Loot Lendário!!! :D ')
            break
        elif step_count >= 7:
            print('Uma pedra gigante esmagou sua guilda :(')
            break
        
        print(f'Você está na salão: {actual_step}')
        print(room_joke[actual_step])
        print('Escolha seu caminho:')
        possible_paths = game_paths[actual_step]
        paths = list(possible_paths.keys())
        for path_index in range(len(paths)):
            print(f'[{path_index + 1}] - Ir por {paths[path_index]}')
        response = int(input())
        
        next_step_name = list(paths)[response - 1]
        actual_step = possible_paths[next_step_name]
        step_count = step_count + 1
        
    new_game = int(input('Você deseja iniciar uma nova aventura? \n [1] Pra sim \n [2] Pra não \n '))
    if new_game == 2:
        break
    else:
        print('Você é o bixão mesmo em doido!!')

        
print('Obrigado pela sua jogatina!!!')
print('Créditos:')
print('Anselmo Lira !')
print('Lucas Gianizelli !')
print('Gustavo Batista !')
print('Fábio Giannini !')
print('Isaac Gouveia !')

                                                
    