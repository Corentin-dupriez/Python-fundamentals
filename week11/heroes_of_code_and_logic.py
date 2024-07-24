class Hero:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = int(health)
        self.mana = int(mana)

    def hero_cast_spell(self, mana_required, spell_name):
        if int(mana_required) <= self.mana:
            self.mana -= int(mana_required)
            print(f'{self.name} has successfully cast {spell_name} and now has {self.mana} MP!')
        else:
            print(f'{self.name} does not have enough MP to cast {spell_name}!')

    def hero_take_damage(self, damage_taken, attacked_by):
        self.health -= int(damage_taken)
        if self.health > 0:
            print(f'{self.name} was hit for {damage_taken} HP by {attacked_by} and now has {self.health} HP left!')
        else:
            print(f'{self.name} has been killed by {attacked_by}!')

    def recharge_hero(self, amount):
        if self.mana + int(amount) >= 200:
            amount_to_recharge = 200 - self.mana
            self.mana += amount_to_recharge
        else:
            self.mana += int(amount)
            amount_to_recharge = amount
        print(f'{self.name} recharged for {amount_to_recharge} MP!')

    def hero_heals(self, amount):
        if self.health + int(amount) >= 100:
            amount_to_heal = 100 - self.health
            self.health += amount_to_heal
        else:
            self.health += int(amount)
            amount_to_heal = amount
        print(f'{self.name} healed for {amount_to_heal} HP!')

    def present_hero(self):
        if self.health > 0:
            print(self.name)
            print(f'  HP: {self.health}')
            print(f'  MP: {self.mana}')


nb_heroes = int(input())
party = []

for hero in range(nb_heroes):
    hero_name, hp, mp = input().split()
    party.append(Hero(hero_name, hp, mp))

while True:
    command = input()
    if command == 'End':
        break
    if 'CastSpell' in command:
        action, hero_name, mp_needed, spell = command.split(' - ')
        for hero in party:
            if hero.name == hero_name:
                hero.hero_cast_spell(mp_needed, spell)
    elif 'TakeDamage' in command:
        action, hero_name, damage, attacker = command.split(' - ')
        for hero in party:
            if hero.name == hero_name:
                hero.hero_take_damage(damage, attacker)
    elif 'Recharge' in command:
        action, hero_name, amount_mana = command.split(' - ')
        for hero in party:
            if hero.name == hero_name:
                hero.recharge_hero(amount_mana)
    else:
        action, hero_name, amount_health = command.split(' - ')
        for hero in party:
            if hero.name == hero_name:
                hero.hero_heals(amount_health)

for hero in party:
    hero.present_hero()
