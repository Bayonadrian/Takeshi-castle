import time
from random import Random
from CastleGame.game.doors import door

class games(Random):

    def add_door(self):

        result = super().randint(0, 40000)

        try:

            print(f'You have to give me two numbers to get {result} adding them - 100 GOLD')
            print('\n')
            time.sleep(1)

            f = input('Give me the first number: ')
            print('\n')
            s = input('Give me the second number: ')
            print('\n')

            adding = int(f) + int(s)

            if adding == result:

                return 100

            else:

                return 0

        except:

            print('You made a mistake')

            return 0

    def decrease_door(self):

        result = super().randint(0, 40000)

        try:

            print(f'You have to give me two numbers to get {result} decreasing them - 150 GOLD')
            print('\n')
            time.sleep(1)

            f = input('Give me the first number: ')
            print('\n')
            s = input('Give me the second number: ')
            print('\n')

            decreasing = int(f) + int(s)

            if decreasing == result:

                return 100

            else:

                return 0

        except:

            print('You made a mistake')
            print('\n')
            time.sleep(1)

            return 0

    def reading(self):

        i = input('Which is the correct letter to read a file? ').lower()

        if 'r' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def slicing(self):

        i = input('How can you slice a text from the third index to the last one? ').lower()

        if '[3:]' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def writing(self):

        i = input('Which is the correct letter to write a file? ').lower()

        if 'w' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def formating(self):

        i = input('How can you format a text without using fstring? ').lower()

        if '%' in i or 'format' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def pandas_d(self):

        i = input('What is the maximum quantity of dimensions pandas can work with? ').lower()

        if '2' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def b_in(self):

        i = input('Is random an external function? ').lower()

        if 'n' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def npy(self):

        i = input('What is the most popular python library to work with linear algebra? ').lower()

        if 'numpy' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def stats(self):

        i = input('What is the build-in package to work with statistics? ').lower()

        if 'statistics' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def ap(self):

        i = input('What class is append belong to? ').lower()

        if 'list' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def op(self):

        i = input('What is the best function to open a file? ').lower()

        if 'open' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def inheritance(self):

        i = input('How is the inheritance work sigle or multiple? ').lower()

        if 'multiple' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def sup(self):

        i = input('What is the correct statement to inherit a method? ').lower()

        if 'super' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def compiler(self):

        i = input('Is python compiled or interpreted? ').lower()

        if 'interpreted' in i:

            print('Great!!')

            return 100

        else:

            print('You made a mistake')
            return 0

    def get_doors(self):
        
        add_door1 = door('Adding', self.add_door)
        add_door2 = door('Decreasing', self.decrease_door)
        add_door3 = door('Reading', self.reading)
        add_door4 = door('Slicing', self.slicing)
        add_door5 = door('Writing', self.writing)
        add_door6 = door('Formating', self.formating)
        add_door7 = door('Pandas dimensions', self.pandas_d)
        add_door8 = door('Build-in', self.b_in)
        add_door9 = door('NY', self.npy)
        add_door10 = door('Stats', self.stats)
        add_door11 = door('Append', self.ap)
        add_door12 = door('OP', self.op)
        add_door13 = door('Inheritance', self.inheritance)
        add_door14 = door('Sup', self.sup)
        add_door15 = door('Compiler', self.compiler)

        games = [add_door1, 
            add_door2, 
            add_door3, 
            add_door4, 
            add_door5, 
            add_door6, 
            add_door7, 
            add_door8, 
            add_door9, 
            add_door10,
            add_door11,
            add_door12,
            add_door13,
            add_door14,
            add_door15]

        return games