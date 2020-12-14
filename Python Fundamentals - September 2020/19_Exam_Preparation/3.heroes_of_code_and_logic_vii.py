num_of_heroes = int(input())

heroes = {}
for _ in range(num_of_heroes):
    name_hero = input().split(" ")
    name, hp, mana = name_hero
    heroes[name] = {"HP": int(hp), "MP": int(mana)}

command = input().split(" - ")


def heal(hero_name, amount):
    heroes[hero_name]["HP"] = heroes[hero_name]["HP"] + amount
    healed = 0
    if heroes[hero_name]["HP"] > 100:
        healed = 100 - heroes[hero_name]["HP"] + amount
        heroes[hero_name]["HP"] = 100
        print(f"{hero_name} healed for {healed} HP!")
    else:
        print(f"{hero_name} healed for {amount} HP!")


def recharge(hero_name, amount):
    heroes[hero_name]["MP"] = heroes[hero_name]["MP"] + amount
    recharged = 0
    if heroes[hero_name]["MP"] > 200:
        recharged = 200 - heroes[hero_name]["MP"] + amount
        heroes[hero_name]["MP"] = 200
        print(f"{hero_name} recharged for {recharged} MP!")
    else:
        print(f"{hero_name} recharged for {amount} MP!")


def take_damage(hero_name, damage, attacker):
    heroes[hero_name]["HP"] = heroes[hero_name]["HP"] - damage
    if heroes[hero_name]["HP"] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
    else:
        del heroes[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")

def cast(hero_name, mp_needed, spell_name):
    if heroes[hero_name]["MP"] >= mp_needed:
        heroes[hero_name]["MP"] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")

while not command[0] == "End":

    if command[0] == "Heal":
        heal(command[1], int(command[2]))
    elif command[0] == "Recharge":
        recharge(command[1], int(command[2]))
    elif command[0] == "TakeDamage":
        take_damage(command[1], int(command[2]), command[3])
    elif command[0] == "CastSpell":
        cast(command[1],int(command[2]), command[3])
    command = input().split(" - ")

sorted_heroes = sorted(heroes.items(), key=lambda x: (-x[1]["HP"], x[0]))


for key, value in sorted_heroes:
    print(key)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")
