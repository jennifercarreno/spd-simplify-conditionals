# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

from sqlalchemy import false, true


def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

ingredients = ['sodium benzoate']
toxins = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']

def toxin_in_ingredients(ingredients, toxins):
    toxin_count = 0
    for toxin in toxins:
        if toxin in ingredients:
            toxin_count +=1
   
    if toxin_count > 0:
       return true
    else:
        return false

if toxin_in_ingredients(ingredients, toxins):
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()

