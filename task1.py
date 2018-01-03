import ast

games1 = open("task1.txt", "r")
games = games1.read()
games = ast.literal_eval(games)
games1.close()

def get_key(games, val):
    for key, value in games.items():
        if value == val:
            print(key)


choice = None
while choice != "0":
    print("""
    База данных игр
    0 - Выйти
    1 - Вывести все игры
    2 - Добавить игру
    3 - Вывести все игры указанного года
    """
          )
    choice = input("Что вы хотите сделать?")
    print()
    if choice == "0":
        print("Пока-пока!")
    elif choice == "1":
        print(games)
    elif choice == "2":
        gameadd = input("Напишите название игры: ")
        if gameadd not in games:
            yearadd = input("Напишите год ее создания: ")
            games[gameadd] = yearadd
            games1 = open("task1.txt", "w")
            games1.write(str(games))
            games1.close()
            print("Игра ", gameadd, " добавлена в базу данных!")
        else:
            print("Такая игра уже есть!")
    elif choice == "3":
        year = input("Игры какого года вывести? ")
        get_key(games, year)








