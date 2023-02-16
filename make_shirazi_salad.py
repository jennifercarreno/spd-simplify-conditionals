# by Kami Bigdely
# Consolidate conditional expressions

from sqlalchemy import true


def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)

def check_required_ingredients(ingredients):
    required_ingredients = ['cucumber', 'tomato', 'lemon juice', 'onion']
    missing = 0
    for ingredient in required_ingredients:
        if ingredient not in ingredients:
            missing += 1
    if missing > 0:
        return True
    else:
        return False 

def make_shirazi_salad(ingredients):
    if check_required_ingredients(ingredients):
        print('lacks ingredients.')
        return
        
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
