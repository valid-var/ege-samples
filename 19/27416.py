
MAX_TURNS = 5


def steps(n: tuple):
    x, y = n
    return (x + 1, y), (x * 2, y), (x, y + 1), (x, y * 2)

"""
! ВНИМАНИЕ !
Не работает для первой задачи, так как там петя НЕ следует выигрышной стратегии.
"""
def f(n: tuple, turn: int = 0):
    if sum(n) >= 77:
        return "W"
    if turn >= MAX_TURNS:
        return "MAX_TURNS"
    turn += 1
    results = [f(x, turn) for x in steps(n)]
    if any(x == 'W' for x in results):
        return "P1" # Игрок с текущей комбинацией обязательно выиграет первым ходом
    if all(x == "P1" for x in results):
        """
        Используется all, т.к. если есть хотя бы один вариант не дает противнику выиграть - он должен использоваться 
        (следование выигрышной стратегии), а если все ходы ведут к выигрышу другого игрока, 
        то текущий игрок точно проиграет
        """
        return "B1" # Игрок с текущей комбинацией обязательно проиграет
    if any(x == "B1" for x in results):
        """
        Используется amy т.к. если хотя бы один из ходов дает возможность поставить противника в проигрышное положение - 
        он будет использоваться (следование выигрышной стратегии)
        """
        return "P2" # Игрок с текущей комбинацией обязательно выиграет вторым ходом
    if all(x == "P1" or x == 'P2' for x in results):
        return "B1/2" # Игрок с текущей комбинацией обязательно проиграет, при этом второй игрок выиграет 1 или 2 ходом


for s in range(15, 70):
    n = (7, s)
    if f(n) == 'P2':
        print(s)
