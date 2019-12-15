from collections import defaultdict
import math
def input(lines):
    recipe = {}
    raw = {}
    for l in lines:
        ingredients = l.strip().split(' => ')
        ins = ingredients[0].replace(',','').split(' ')
        out = ingredients[1].replace(',','').split(' ')
        if ins[1] == 'ORE':
            raw[out[1]] = [int(ins[0]),int(out[0])]
        else:
            recipe[out[1]] = [int(out[0]),ins]
    return recipe,raw

def estimate(recipe,raw,current_ore):
    fuel = 1
    max = 1000000000000
    while True:
        fuel = fuel * max // current_ore
        estimate_ore = required_ore(recipe,raw,fuel)
        if current_ore == estimate_ore <= max:
            break
        else:
            current_ore = estimate_ore
    return fuel
def required_ore(recipe,raw,amount_fuel):
    inventory = defaultdict(int)
    inventory['FUEL'] = amount_fuel
    ingredients = {'FUEL'}
    raw_ingredients = set()

    while ingredients:
        item = ingredients.pop()
        required_amount = inventory[item]
        if item in recipe:
            rec = recipe[item]
            ratio = math.ceil(required_amount / rec[0])
            for x in range(0,len(rec[1]),2):
                amount = ratio * int(rec[1][x])
                item_needed = rec[1][x+1]
                inventory[item_needed] += amount
                ingredients.add(item_needed)
            produced = rec[0] * ratio
            inventory[item] -= produced
        else:
            raw_ingredients.add(item)
    count_ore = 0
    for item in raw_ingredients:
        required_amount = inventory[item]
        if required_amount > 0:
            rec = raw[item]
            ratio = math.ceil(required_amount / rec[1])
            required_amount -= rec[1] * ratio
            count_ore += rec[0] * ratio
    return count_ore

r,raw = input(open('input.txt').readlines())
ore = required_ore(r,raw,1)
print("Part One: ",ore)

print("Part Two: ",estimate(r,raw,ore))
