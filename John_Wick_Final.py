import random


class Health:
    def __init__(self, mod_gun=0, mod_shirt=0, mod_pants=0, mod_shoes=0, mod_skill=0):
        self.mod_gun = mod_gun
        self.mod_shirt = mod_shirt
        self.mod_pants = mod_pants
        self.mod_shoes = mod_shoes
        self.mod_skill = mod_skill


class Hp_mod(Health):
    def __init__(self, mod_gun, mod_shirt, mod_pants, mod_shoes, mod_skill, armor='', tailor='', library='', shirt='',
                 pants='', shoes='', map_option='',
                 focus_option='', payment_option='', mind_option=''):
        Health.__init__(self, mod_gun, mod_shirt, mod_pants, mod_shoes, mod_skill)
        self.armor = armor
        self.tailor = tailor
        self.shirt = shirt
        self.pants = pants
        self.shoes = shoes
        self.library = library
        self.map_option = map_option
        self.focus_option = focus_option
        self.payment_option = payment_option
        self.mind_option = mind_option

    def Armor(self):
        if self.armor == 'HANDS':
            self.mod_gun += random.randrange(1, 24)
            return self.mod_gun

        if self.armor == 'PISTOL':
            self.mod_gun += random.randrange(25, 49)
            return self.mod_gun

        if self.armor == 'AR':
            self.mod_gun += random.randrange(50, 74)
            return self.mod_gun

        if self.armor == 'SHOTGUN':
            self.mod_gun += random.randrange(75, 99)
            return self.mod_gun

        if self.armor == 'PEN':
            self.mod_gun += 100
            return self.mod_gun

    def Tailor(self):
        if self.tailor == 'SHIRT':
            if self.shirt == 'FORMAL':
                self.mod_shirt += 50
                return self.mod_shirt

            if self.shirt == 'CASUAL':
                self.mod_shirt += 0
                return self.mod_shirt

        if self.tailor == 'PANTS':
            if self.pants == 'INDOOR':
                self.mod_pants += 25
                return self.mod_pants

            if self.pants == 'OUTDOOR':
                self.mod_pants += 0
                return self.mod_pants

        if self.tailor == 'SHOES':
            if self.shoes == 'OXFORDS':
                self.mod_shoes += 25
                return self.mod_shoes

            if self.shoes == 'BROGUES':
                self.mod_shoes += 0
                return self.mod_shoes

    def Library(self):
        if self.library == 'MAPPING':
            if self.map_option == 'YES':
                self.mod_skill += random.randrange(10, 25)
                return self.mod_skill

            if self.map_option == 'NO':
                self.mod_skill -= random.randrange(0, 15)
                return self.mod_skill

        if self.library == 'VISUALIZE':
            if self.focus_option == 'YES':
                self.mod_skill += random.randrange(10, 25)
                return self.mod_skill

            if self.focus_option == 'NO':
                self.mod_skill -= random.randrange(0, 15)
                return self.mod_skill

        if self.library == 'PAY OFF':
            if self.payment_option == 'YES':
                self.mod_skill += random.randrange(10, 25)
                return self.mod_skill

            if self.payment_option == 'NO':
                self.mod_skill -= random.randrange(0, 15)
                return self.mod_skill

        if self.library == 'MEDITATE':
            if self.mind_option == 'YES':
                self.mod_skill += random.randrange(10, 25)
                return self.mod_skill

            if self.mind_option == 'NO':
                self.mod_skill -= random.randrange(0, 15)
                return self.mod_skill


class InvalidEntryError(Exception):
    def __init__(self, value):
        self.value = value


class EnemyHealth:
    def __init__(self, E_mod_gun=0, E_mod_suit=0, E_mod_knowledge=0):
        self.E_mod_gun = E_mod_gun
        self.E_mod_suit = E_mod_suit
        self.E_mod_knowledge = E_mod_knowledge

    def Enemy_Gun(self):
        self.E_mod_gun += random.randrange(50, 100)
        return self.E_mod_gun

    def Enemy_Suit(self):
        self.E_mod_suit += random.randrange(50, 100)
        return self.E_mod_suit

    def Enemy_Knowledge(self):
        self.E_mod_knowledge += random.randrange(50, 100)
        return self.E_mod_knowledge


John = Hp_mod(0, 0, 0, 0, 0)
Enemy = EnemyHealth(0, 0, 0)
enemy_gun = Enemy.Enemy_Gun()
enemy_suit = Enemy.Enemy_Suit()
enemy_knowledge = Enemy.Enemy_Knowledge()
gun = 0
suit = 0
shirt = 0
pants = 0
shoes = 0
knowledge = 0

print(
    'Hello Mr.Wick, Welcome to the Rome Continental. I am the Concierge here at the hotel, if you need any assistance, '
    'please do let me know.\n')
while True:
    Choice = input('Where would you like to go Mr.Wick: Armor, Tailor, Library, Hunt?\n:').upper()
    if Choice == 'ARMOR':
        print('Good Evening Mr.Wick, I am the Arms Keeper here at the Continental.\n')
        while True:
            try:
                weapon = input(
                    'How would you like to be on tonight\'s endevors? Loud, Normal, Dim, Quiet, Ghostly, Exit\n:').upper()
                if weapon == 'LOUD':
                    John.armor = 'SHOTGUN'
                    if gun < 100:
                        gun = John.Armor()
                        break
                    else:
                        print('At Max Power')
                        break

                elif weapon == 'NORMAL':
                    John.armor = 'AR'
                    if gun < 100:
                        gun = John.Armor()
                        break
                    else:
                        print('At Max Power')
                        break

                elif weapon == 'DIM':
                    John.armor = 'PISTOL'
                    if gun < 100:
                        gun = John.Armor()
                        break
                    else:
                        print('At Max Power')
                        break

                elif weapon == 'QUIET':
                    John.armor = 'HANDS'
                    if gun < 100:
                        gun = John.Armor()
                        break
                    else:
                        print('At Max Power')
                        break

                elif weapon == 'GHOSTLY':
                    John.armor = 'PEN'
                    if gun < 100:
                        gun = John.Armor()
                        break
                    else:
                        print('At Max Power')
                        break
                elif weapon == 'EXIT':
                    break
                else:
                    raise InvalidEntryError('Invalid entry.')
            except InvalidEntryError as emessage:
                print(emessage)
                print('Please try again\n')
                continue

    elif Choice == 'TAILOR':
        print('Bonjour Mr.Wick, Welcome to the Best Tailor in all of Rome.\n')
        while True:
            try:
                clothing = input('How may I help you Mr.Wick: Shirt, Pants, Shoes, Exit\n:').upper()
                if clothing == 'SHIRT':
                    John.tailor = clothing
                    if shirt < 50:
                        material = input('How would you like the fabric?: Formal or Casual\n:').upper()
                        if material == 'FORMAL' or material == 'CASUAL':
                            John.shirt = material
                            shirt = John.Tailor()
                            continue
                        else:
                            raise InvalidEntryError('Invalid entry')
                    else:
                        print('At Max shirt power')
                        continue

                elif clothing == 'PANTS':
                    John.tailor = clothing
                    if pants < 25:
                        material = input('Will this be Indoor or Outdoor?\n:').upper()
                        if material == 'INDOOR' or material == 'OUTDOOR':
                            John.pants = material
                            pants = John.Tailor()
                            continue
                        else:
                            raise InvalidEntryError('Invalid entry')
                    else:
                        print('At Max pants power')
                        continue

                elif clothing == 'SHOES':
                    John.tailor = clothing
                    if shoes < 25:
                        material = input('What footwear would you prefer: Oxfords or Brogues\n:').upper()
                        if material == 'OXFORDS' or material == 'BROGUES':
                            John.shoes = material
                            shoes = John.Tailor()
                            continue
                        else:
                            raise InvalidEntryError('Invalid entry')
                    else:
                        print('At MAX shoes power')
                        continue

                elif clothing == 'EXIT':
                    break

                else:
                    raise InvalidEntryError('Invalid entry')
            except InvalidEntryError as emessage:
                print(emessage)
                print('Please try again\n')
                continue

    elif Choice == 'LIBRARY':
        print('Sir Wick, A pleasure to see you once again in the Library.\n')
        while True:
            try:
                planning = input(
                    'What are we looking for, Mr.Wick?: Mapping, Visualize, Pay off, Meditate, or Exit\n:').upper()
                if planning == 'MAPPING':
                    John.library = planning
                    if -100 <= knowledge <= 100:
                        choice = input('Would you like to see the layout, Mr.Wick? Yes or No\n:').upper()
                        if choice == 'YES' or choice == 'NO':
                            John.map_option = choice
                            knowledge = John.Library()
                            continue
                        else:
                            raise InvalidEntryError('Invalid entry')
                    else:
                        print('Already at Max/Min knowledge')
                        continue

                elif planning == 'VISUALIZE':
                    John.library = planning
                    if -100 <= knowledge <= 100:
                        choice = input(
                            'Would you like to run visualize your advantage points Mr.Wick? Yes or No\n:').upper()
                        if choice == 'YES' or choice == 'NO':
                            John.focus_option = choice
                            knowledge = John.Library()
                            continue
                        else:
                            raise InvalidEntryError('Invalid Entry')
                    else:
                        print('Already at Max/Min Knowledge')
                        continue

                elif planning == 'PAY OFF':
                    John.library = planning
                    if -100 <= knowledge <= 100:
                        choice = input(
                            'Would you like to see about Pay off the Guards before tonight\'s hunt, Mr.Wick? '
                            'Yes or No\n:').upper()
                        if choice == 'YES' or choice == 'NO':
                            John.payment_option = choice
                            knowledge = John.Library()
                            continue
                        else:
                            raise InvalidEntryError('Invalid entry')
                    else:
                        print('Already at MAX/MIN knowledge')
                        continue

                elif planning == 'MEDITATE':
                    John.library = planning
                    if -100 <= knowledge <= 100:
                        choice = input('Shall I leave you be in our meditation room, Mr.Wick? Yes or No\n:').upper()
                        if choice == 'YES' or choice == 'NO':
                            John.mind_option = choice
                            knowledge = John.Library()
                            continue
                        else:
                            raise InvalidEntryError('Invalid Entry')
                    else:
                        print('Already at MAX/MIN knowledge')
                        continue

                elif planning == 'EXIT':
                    break

                else:
                    raise InvalidEntryError('Invalid entry')
            except InvalidEntryError as emessage:
                print(emessage)
                print('Please try again')
                continue
    elif Choice == 'HUNT':
        break
    else:
        print('Invalid try again')
        continue

suit = shirt + pants + shoes
total_hp = gun + suit + knowledge
print('\n')
print(f'Your shirt level is at {shirt}')
print(f'Your pants level is at {pants}')
print(f'Your shoes level is at {shoes}')
print(f'Your weapon power is at {gun}.')
print(f'Your suit durability is at {suit}.')
print(f'Your Intelligence is at {knowledge}.')
print(f'Your total power and health is {total_hp}.')
enemy_hp = enemy_gun + enemy_suit + enemy_knowledge
print(f'Enemies suit durability is at {enemy_suit}')
print(f'Enemies weapon power is {enemy_gun}')
print(f'Enemies Intelligence is at {enemy_knowledge}')
print(f'Your enemies power and health is {enemy_hp}')
if enemy_hp > total_hp:
    print('You have died Mr.Wick')
else:
    print('You have won mr. wick')