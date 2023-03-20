def format_ingredients(items):
    if len(items) == 1:
        return ''.join(items)
    elif len(items) == 2:
        items_2 = items.append('and')
        items[-1], items[-2] = items[-2], items[-1]
        return ''.join(items)
    elif len(items) >= 3:
        items_2 = items.append('and')
        items[-1], items[-2] = items[-2], items[-1]
        items_2 = items[-3:]
        items_2 = ' '.join(items_2)
        items_3 = items[:-3]
        items_3 = ', '.join(items_3)
        items_4 = items_3 + ', ' + items_2
        return items_4
    else:
        return ''
    # print(items_4)


# '2 eggs, 1 liter sugar, 1 tsp salt  and  vinegar'
# '2 eggs, 1 liter sugar, 1 tsp salt and vinegar'
print(format_ingredients(['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar']))
