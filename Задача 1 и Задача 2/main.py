with open('recipes.txt', 'rt', encoding='utf-8') as f:
    recipes = {}
    for line in f:
        dish_name = line.strip()
        count = int(f.readline())
        ingredients = []
        for i in range(count):
            ingredients.append(f.readline().strip())
            name, quantity, measure = ingredients[i].split(' | ')
            ingredients[i] = {'ingredient_name': name, 'quantity': int(quantity), 'measure': measure}
        f.readline()
        recipes[dish_name] = ingredients


# for dish_name, ingredients in recipes.items():
#     print(f'\n{dish_name}:')
#     for ingredient in ingredients:
#         print(ingredient)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in recipes[dish]:
            new_shop_list_item = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = new_shop_list_item
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


shop_list2 = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# print(shop_list2)
