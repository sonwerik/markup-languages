class Player:
    def __init__(self, name="Player", health=100, status="ALIVE", position=0, weapon=None):
        self.name = name
        self.health = health
        self.status = status
        self.position = position
        self.weapon = weapon

    def __str__(self):
        return f'{self.name} - {self.health} PS'

class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Position: ({self.x}, {self.y})'

class Weapon:
    def __init__(self, name="Default", damage=20, weapon_range=1.5):
        self.name = name
        self.damage = damage
        self.range = weapon_range

    def __str__(self):
        return f'{self.name} - {self.damage} {self.range}'

class Game:
    def __init__(self):
        self.players = []
        self.weapons = []

    def add_player(self, player):
        self.players.append(player)

    def attack(self, target_player, target_position, weapon, attacker_position):
        distance = ((target_position.x - attacker_position.x) ** 2 +
                    (target_position.y - attacker_position.y) ** 2) ** 0.5
        if distance <= weapon.range:
            target_player.health -= weapon.damage
            print(f'{target_player.name} was attacked! Remaining health: {target_player.health}')
        else:
            print('Target is out of range.')