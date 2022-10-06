import time
import click
from click_help_colors import HelpColorsGroup
from rich.console import Console
from halo import Halo
from CastleGame.scenarios import start, castle
from CastleGame.game.persecutor import persecutor
from CastleGame.game.game import games


@click.group(cls= HelpColorsGroup, help_headers_color= "black", help_options_color= "blue")
def main():

    '''Welcome to Takeshi's Castle there are your options'''

    pass

@main.command()
def instructions():

    '''There are the instructions of the game'''

    click.secho(start.start('Takeshi\'s Castle').rules(), fg= 'blue')

    pass

@main.command()
def start_castle():

    '''Start tha game'''

    while True:

        gs = start.start('Takeshi\'s Castle')
        g = games()

        reward = 0
        election = ''
        evil = persecutor()
        spinner = Halo()

        title = gs.title()

        click.echo('*'*80)
        click.secho(f'Welcome to {title}', fg= 'blue')
        click.echo('*'*80)
        time.sleep(1)
        click.echo('Let me give you the instructions... \n')
        click.secho(gs.rules(), fg= 'green')

        time.sleep(1)

        try:

            try:

                rooms = input('How many rooms do you want? ')
                rooms = int(rooms)

            except:

                print('You did not assigned an integer value room is 10 by default')
                rooms = 10

            assert int(rooms) <= 10, 'Don\'t use more than 10 rooms'

            print('\n')
            spinner.start()
            for r in range(rooms):

                cas = castle.castle(rooms)

                spinner.text = f'Creating rooms - {r}'
                time.sleep(r)

            
            ls = cas.create()

            spinner.succeed('Rooms created')
            spinner.info('Done, good luck!')
            spinner.stop()
            print('\n')
        
        except Exception as e:

            spinner.stop()
            Console().print(f'{e}', style='bold red')
            Console().print('Something went wrong... Game is gonna close, use integer numbers and don\'t create more than 10 rooms', style='bold red')
            print('\n')
            continue

        time.sleep(1)

        while True:

            election = input('Give me a command: ')
            print('\n')

            try:

                if 'rooms' in election.lower():

                    if evil <= time.time():

                        if reward < 300:

                            click.secho(f'You don\' have enough money to brive(reward = {reward})...', fg= 'red')
                            print('\n')
                            time.sleep(1)
                            Console().print('Game Over :skull:', style= 'red bold')
                            print('\n')
                            time.sleep(2)
                            break
                        
                        else:

                            click.secho('Briving...', fg= 'black')
                            print('\n')
                            reward = reward - 300
                            evil = persecutor()
                            time.sleep(1)

                    else:

                        reward, ls = cas.choosing_doors(reward, ls)

                elif 'time' in election.lower():

                    click.secho(time.ctime(evil))
                    print('\n')

                elif 'instructions' in election.lower():

                    click.secho(gs.rules, fg= 'green')
                    print('\n')
                    time.sleep(1)

                elif 'restart' in election.lower():
                    
                    click.secho('Restarting game', fg= 'green')
                    print('\n')
                    time.sleep(1)
                    break

                elif 'left' in election.lower():

                    click.secho(len(ls), fg= 'blue')
                    print('\n')
                    time.sleep(1)

                elif 'reward' in election.lower():

                    Console().print(f'Your current reward is {reward} :dollar:', style='bold yellow')
                    print('\n')

                elif 'exit' in election.lower():

                    click.secho('Good bye...', fg='red')
                    print('\n')
                    time.sleep(1)
                    break

                else:

                    click.secho(f'You wrote "{election}" which is not valid, try again', fg= 'red', bg= 'white')
                    print('\n')
                    time.sleep(1)

            except:

                print('Something wrong happened')
                print('\n')
                time.sleep(1)

                if 'exit' in election.lower():

                    break

                continue
        
        if 'exit' in election or 'rooms' in election:
            
            break

if __name__ == '__main__':

    main()