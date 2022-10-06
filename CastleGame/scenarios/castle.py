import time
from game.game import games
from random import Random

class castle(games, Random):

    def __init__(self, doors: int) -> None:
        
        self.doors = int(doors)
        self.gold = 0

    def create(self):

        ls = super().get_doors()

        return super().sample(ls, self.doors)

    def choosing_doors(self, gold, ls):

        print('You have this doors...')
        print('\n')
        time.sleep(1)

        num = 0

        for d in ls:

            print(f'{d.name} with a number {num}')
            print('\n')
            time.sleep(1)

            num += 1

        n = int(input('Please give me the number of your room: '))
        print('\n')

        item = ls.pop(n)

        gold += item.meth()

        return gold, ls
        


