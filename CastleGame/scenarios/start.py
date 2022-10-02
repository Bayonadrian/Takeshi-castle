class start:

    def __init__(self, name: str) -> None:
        
        self.name = name

    def title(self):

        return self.name

    def rules(self):

        txt = f'''
        Welcome to {self.name} here you have to pass thoughout all the doors we have for you before been catched by our persecutors,
        you are gonna have a random time to scape from them once you are capture you can brive them with gold you need 300 of gold to brive
        them... Follow the commands:

        - Instructions to get this information.
        - Rooms to get rooms options.
        - Time to know how much time you have left.
        - Brive to brive your persecutor.
        - Exit to finish the game.
        - Restart to restart the game.
        - Reward to know your reward.
        - Left to know how much doors are left.

        IMPORTANT: NEVER CREATE MORE THAN 10 ROOMS

        Just be aware and get the best reward, best regars...
        '''

        return txt