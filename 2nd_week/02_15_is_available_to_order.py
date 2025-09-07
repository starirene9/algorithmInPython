shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort() #정렬 먼저
    for order in orders:
        if not is_exist_target_number_binary(order, menus):
            return False
    return True

def is_exist_target_number_binary(target, array):
    cur_min_num = 0
    cur_max_num = len(array) - 1
    cur_guess_num = cur_min_num + cur_max_num // 2

    while cur_min_num <= cur_max_num:
        if array[cur_guess_num] == target:
            return True
        elif array[cur_guess_num] < target:
            cur_min_num = cur_guess_num + 1
        else:
            cur_max_num = cur_guess_num - 1
        cur_guess_num = (cur_min_num + cur_max_num) // 2
    return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)