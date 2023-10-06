import os


with open('Recipes.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()

cook_book = {}
current_recipe = ''
current_ingredients = []
for line in lines:
    line = line.strip()
    if line:
        if not current_recipe:
            current_recipe = line
        elif line.isdigit():
            current_ingredients = []
        else:
            ingredient_name, quantity, measure = line.split(' | ')
            ingredient_info = {
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure,
            }
            current_ingredients.append(ingredient_info)
    else:
        cook_book[current_recipe] = current_ingredients
        current_recipe = ''
        current_ingredients = []

# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if name not in shop_list:
                    shop_list[name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[name] += quantity
        else:
            return 'Такое мы не умеем готовить'
    return shop_list

# print(get_shop_list_by_dishes(["Утка"], 2))

files = ['1.txt', '2.txt', '3.txt']

file_info = []

for file in files:
    with open(file, 'r', encoding='utf8') as f:
        lines = f.readlines()
        num_lines = len(lines)
        content = ''.join(lines)
        file_info.append((file, num_lines, content))

file_info.sort(key=lambda x: x[1])

# print(file_info)

with open('Joined.txt', 'w', encoding='utf8') as f:
    for file, num_lines, content in file_info:
        f.write(f'Имя файла: {file}\n')
        f.write(f'Количество строк в файле: {num_lines}\n')
        f.write(content)
        f.write('\n')