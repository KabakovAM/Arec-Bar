import exception
import glass
import measure
import ingredient
import cocktail
import make


def main_menu():
    print('\nВас приветствует Arec-Bar: \nВыберите опцию:')
    print('\n1) Коктейли \n2) Ингредиенты \n3) Бокалы \n4) Меры измерения \n5) История \n0) Выйти из программы')
    data = input()
    if exception.menu_exc(data, 5, 'main_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return main_menu()


def cocktails_menu():
    print('\nВыберите опцию:')
    print('\n1) Поиск коктейля \n2) Список коктейлей \n3) Список избранного \n4) Добавить коктейль \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 4,'cocktails_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return cocktails_menu()


def ingredients_menu():
    print('\nВыберите опцию:')
    print('\n1) Поиск ингредиента \n2) Список ингредиентов \n3) Список ингредиентов в наличии \n4) Добавить ингредиент \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 4,'ingredients_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return ingredients_menu()


def glasses_menu():
    print('\nВыберите опцию:')
    print('\n1) Поиск бокала \n2) Список бокалов \n3) Добавить бокал \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 3, 'glasses_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return glasses_menu()


def measures_menu():
    print('\nВыберите опцию:')
    print('\n1) Поиск меры измерения \n2) Список мер измерения \n3) Добавить меру измерения \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 3, 'measures_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return measures_menu()


def cocktail_menu():
    print('\nВыберите опцию:')
    print('\n1) Приготовить коктейль \n2) Указать количество порций \n3) Изменить коктейль \n4) Удалить коктейль \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 4, 'cocktail_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return cocktail_menu()


def ingredient_menu():
    print('\nВыберите опцию:')
    print('\n1) Доступные коктейли \n2) Изменить ингредиент \n3) Удалить ингредиент \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 3, 'ingredient_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return ingredient_menu()


def glass_menu():
    print('\nВыберите опцию:')
    print('\n1) Доступные коктейли \n2) Изменить бокал \n3) Удалить бокал \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 3, 'glass_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return glass_menu()


def measure_menu():
    print('\nВыберите опцию:')
    print('\n1) Изменить меру измерения \n2) Удалить меру измерения \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 2, 'measure_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return measure_menu()


def make_menu():
    print('\nВыберите опцию:')
    print('\n1) Использовать ингредиент для замены только сейчас \
          \n2) Заменить и объеденить количество ингредиента во всех коктейлях, где он встречается \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 2, 'make_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return make_menu()


def cocktail_change_menu():
    print('\nВыберите опцию:')
    print('\n1) Изменить название коктейля \n2) Изменить бокал \
          \n3) Изменить описание коктейля \n4) Изменить рецепт коктейля \
          \n5) Изменить ингредиенты \n6) Добавить/Удалить в/из список/ка "Избранное"\n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 6, 'cocktail_change_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return measure_menu()


def ingredient_change_menu():
    print('\nВыберите опцию:')
    print('\n1) Изменить бренд ингредиента \n2) Изменить вид ингредиента \
          \n3) Изменить категорию ингредиента \n4) Изменить количество ингредиента \
          \n5) Изменить стоимость ингредиента \n6) Изменить отслеживание ингредиента \
          \n7) Добавить/Удалить в/из список/ка "В наличии" \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 7, 'ingredient_change_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return measure_menu()


def measure_change_menu():
    print('\nВыберите опцию:')
    print('\n1) Изменить название меры измерения \n2) Изменить объём меры измерения \n0) Выйти в предыдущее меню')
    data = input()
    if exception.menu_exc(data, 2, 'measure_change_menu'):
        return int(data)
    print('\nВведено неверное значение. Повторите ввод.')
    return measure_menu()


def create_cocktail(part, cocktail_list):
    data_list = list()
    if part == 1 or part == 'all':
        print('\nВведите название коктейля:')
        data = input()
        while data == '':
            print('\nПоле должно быть заполнено.')
            print('\nВведите название коктейля:')
            data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            cocktail_list[1] = data
    if part == 'all':
        data_list.append(name_glass())
    if part == 2:
        cocktail_list[2] = name_glass()
    if part == 3 or part == 'all':
        print('\nВведите описание коктейля или нажмите Enter для продолжения:')
        data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            cocktail_list[3] = data
    if part == 4 or part == 'all':
        print('\nВведите рецепт приготовления коктейля:')
        data = input()
        while data == '':
            print('\nПоле должно быть заполнено.')
            print('\nВведите рецепт приготовления коктейля:')
            data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            cocktail_list[4] = data
    if part == 'all':
        end = '1'
        while end == '1':
            data_list.append(name_ingredient())
            print('\nВведите количество ингредиента:')
            data = input()
            while not data.isdigit() and len(data) < 7 and data != '0':
                print('\nПоле должно быть заполнено положительным числом. Максимально 6 символов.')
                print('\nВведите количество ингредиента:')
                data = input()
            data_list.append(data)
            data_list.append(name_measure())
            print('\nДобавить ещё один ингредиент? Да - 1, Нет - 0.')
            data = input()
            while not (data == '1' or data == '0'):
                print('\nПоле должно быть заполнено 1 или 0.')
                print('\nДобавить ещё один ингредиент? Да - 1, Нет - 0.')
                data = input()
            end = data
    if part == 5:
        end = False
        while end != True:
            num_dic = cocktail.cocktail_ingredients_show(cocktail_list[0])
            print('Выберите ингредиент для изменения, нажмите Enter для добавления нового ингредиента, введите 0 для выхода в предыдущее меню:')
            i = input()
            if i == '':
                cocktail_list.append(name_ingredient())
                print('\nВведите количество ингредиента:')
                data = input()
                while not data.isdigit() and len(data) < 7 and data != '0':
                    print('\nПоле должно быть заполнено положительным числом. Максимально 6 символов.')
                    print('\nВведите количество ингредиента:')
                    data = input()
                cocktail_list.append(data)
                cocktail_list.append(name_measure())
                cocktail_name = cocktail_list.pop(0)
                cocktail.cocktail_change(cocktail_name, cocktail_list)
                cocktail_list = cocktail.cocktail_list(cocktail_name)
                return create_cocktail(5, cocktail_list)
            elif int(i) in num_dic and i != '0':
                print('\nУдалить или изменить ингредиент? Изменить - 1, Удалить - 0.')
                data = input()
                while not (data == '1' or data == '0'):
                    print('\nПоле должно быть заполнено 1 или 0.')
                    print('\nУдалить или изменить ингредиент? Изменить - 1, Удалить - 0.')
                    data = input()
                if data == '1':
                    cocktail_list[num_dic[int(i)]] = name_ingredient()
                    print('\nВведите количество ингредиента:')
                    data = input()
                    while not data.isdigit() and len(data) < 7 and data != '0':
                        print('\nПоле должно быть заполнено положительным числом. Максимально 6 символов.')
                        print('\nВведите количество ингредиента:')
                        data = input()
                    cocktail_list[num_dic[int(i)] + 1] = data
                    cocktail_list[num_dic[int(i)] + 2] = name_measure()                  
                else:
                    cocktail_list.pop(num_dic[int(i)])
                    cocktail_list.pop(num_dic[int(i)])
                    cocktail_list.pop(num_dic[int(i)])
                cocktail_name = cocktail_list.pop(0)
                cocktail.cocktail_change(cocktail_name, cocktail_list)
                cocktail_list = cocktail.cocktail_list(cocktail_name)
                return create_cocktail(5, cocktail_list)
            elif i == '0':
                end = True
            else:
                print('\nОшибка ввода. Повторите ввод.')
    if part == 6 or part == 'all':      
        print('\nДобавить коктейль в список избранного? Да - 1, Нет - 0.')
        data = input()
        while not (data == '1' or data == '0'):
            print('\nПоле должно быть заполнено 1 или 0.')
            print('\nДобавить коктейль в список избранного? Да - 1, Нет - 0.')
            data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            cocktail_list[5] = data
    if part == 'all':
        print('\nКоктейль успешно добавлен. Выход в предыдущее меню.')
        return data_list
    else:
        print('\nКоктейль успешно изменён. Выход в предыдущее меню.')
        cocktail_list.pop(0)
        return cocktail_list


def name_cocktail(type, filter):
    num_dic = cocktail.cocktails_show(type, 'all', filter)
    if len(num_dic) == 1:
        print('\nСписок пуст.')
        return 0
    else:
        print('\nВыберите коктейль или введите букву для фильтрации списка или нажмите Enter для выхода в предыдущее меню:')
    data = input()
    if data == '':
        return 0
    while not data.isdigit():
        if len(data) > 1:
            print('\nПо данному фильтру ничего не найдено.')
            num_dic = cocktail.cocktails_show(type, 'all', filter)
        else:
            num_dic = cocktail.cocktails_show(type, data, filter)
            if len(num_dic) == 1:
                print('\nПо данному фильтру ничего не найдено.')
                num_dic = cocktail.cocktails_show(type, 'all', filter)
        print('Выберите коктейль или введите букву для фильтрации списка:')
        data = input()
    data = exception.id_check(data, num_dic)
    if data == 0:
        print('\nОшибка ввода. Повторите ввод.')
        return name_cocktail(type, filter)
    return data


def search_cocktail():
    print('Введите название коктейля:')
    cocktail = exception.search_exc(input(), 'Arec-Bar/cocktail.csv')
    if cocktail == 0:
        print('\nКоктейль не найден. Выход в предыдущее меню.')
    return cocktail


def quantity_cocktail():
    print('\nВведите количество порций:')
    data = input()
    while not data.isdigit() and len(data) < 7 and data <= 0:
        print('\nПоле должно быть заполнено положительным числом. Максимально 6 символов.')
        print('\nВведите количество порций:')
        data = input()
    return data


def delete_cocktail():
    print('\nУдаление выполнено успешно. Выход в предыдущее меню.')


def create_ingredient(part, ingredient_list):
    data_list = list()
    if part == 1 or part == 'all':
        print('\nВведите бренд ингредиента или нажмите Enter для продолжения:')
        data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            ingredient_list[0] = data
    if part == 2 or part == 'all':
        print('\nВведите вид ингредиента:')
        data = input()
        while data == '':
            print('\nПоле должно быть заполнено.')
            print('\nВведите вид ингредиента:')
            data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            ingredient_list[1] = data
    if part == 3 or part == 'all':
        print('\nВведите категорию ингредиента:')
        data = input()
        while data == '':
            print('\nПоле должно быть заполнено.')
            print('\nВведите категорию ингредиента:')
            data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            ingredient_list[2] = data
    if part == 4 or part == 'all':
        print('\nВведите количество ингредиента или нажмите Enter для продолжения:')
        data = input()
        if data != '':
            while not data.isdigit() and len(data) < 7 and data != '0':
                print('\nПоле должно быть заполнено положительным числом. Максимально 6 символов.')
                print('\nВведите количество ингредиента:')
                data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            ingredient_list[3] = data
    if part == 5 or part == 'all':
        print('\nВведите стоимость ингредиента или нажмите Enter для продолжения:')
        data = input()
        if data != '':
            while not data.isdigit() and len(data) < 7 and data != '0':
                print('\nПоле должно быть заполнено положительным числом. Максимально 6 символов.')
                print('\nВведите стоимость ингредиента:')
                data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            ingredient_list[4] = data
    if part == 6 or part == 'all':
        print('\nОтслеживать остаток ингредиента? Да - 1, Нет - 0.')
        data = input()
        while not (data == '1' or data == '0'):
            print('\nПоле должно быть заполнено 1 или 0.')
            print('\nОтслеживать остаток ингредиента? Да - 1, Нет - 0.')
            data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            ingredient_list[5] = data
    if part == 7 or part == 'all':
        print('\nДобавить ингредиент в список "В наличии"? Да - 1, Нет - 0.')
        data = input()
        while not (data == '1' or data == '0'):
            print('\nПоле должно быть заполнено 1 или 0.')
            print('\nОтслеживать остаток ингредиента? Да - 1, Нет - 0.')
            data = input()
        if part == 'all':
            data_list.append(data)
        else: 
            ingredient_list[6] = data
    if part == 'all':
        print('\nИнгредиент успешно добавлен. Выход в предыдущее меню.')
        return data_list
    else:
        print('\nИнгредиент успешно изменён. Выход в предыдущее меню.')
        return ingredient_list


def name_ingredient(type):
    num_dic = ingredient.ingredients_show(type, 'all')
    if len(num_dic) == 1:
        print('\nСписок пуст.')
        return 0
    else:
        print('\nВыберите ингредиент или введите букву для фильтрации списка или нажмите Enter для выхода в предыдущее меню:')
    data = input()
    if data == '':
        return 0
    while not data.isdigit():
        if len(data) > 1:
            print('\nПо данному фильтру ничего не найдено.')
            num_dic = ingredient.ingredients_show(type, 'all')
        else:
            num_dic = ingredient.ingredients_show(type, data)
            if len(num_dic) == 1:
                print('\nПо данному фильтру ничего не найдено.')
                num_dic = ingredient.ingredients_show(type, 'all')
        print('\nВыберите ингредиент или введите букву для фильтрации списка:')
        data = input()
    data = exception.id_check(data, num_dic)
    if data == 0:
        print('\nОшибка ввода. Повторите ввод.')
        return name_ingredient()
    return data


def search_ingredient():
    print('Введите название ингредиента:')
    ingredient = exception.search_exc(input(), 'Arec-Bar/ingredient.csv')
    if ingredient == 0:
        print('\nИнгредиент не найден. Выход в предыдущее меню.')
    return ingredient


def delete_ingredient(data):
    if exception.delete_check(data, 'ingredient'):
        print('\nУдаление выполнено успешно. Выход в предыдущее меню.')
        return True
    print('\nУдаление невозможно. Существуют коктейли с данным ингредиентом. Выход в предыдущее меню.')
    return False


def create_glass():
    data_list = list()
    print('\nВведите название бокала:')
    data = input()
    while data == '':
        print('\nПоле должно быть заполнено.')
        print('\nВведите название бокала:')
        data = input()
    data_list.append(data)
    print('\nБокал успешно добавлен(изменён). Выход в предыдущее меню.')
    return data_list


def name_glass():
    num_dic = glass.glasses_show('all')
    if len(num_dic) == 1:
        print('\nСписок пуст.')
        return 0
    else:
        print('\nВыберите бокал или введите букву для фильтрации списка или нажмите Enter для выхода в предыдущее меню:')
    data = input()
    if data == '':
        return 0
    while not data.isdigit():
        if len(data) > 1:
            print('\nПо данному фильтру ничего не найдено.')
            num_dic = glass.glasses_show('all')
        else:
            num_dic = glass.glasses_show(data)
            if len(num_dic) == 1:
                print('\nПо данному фильтру ничего не найдено.')
                num_dic = glass.glasses_show('all')
        print('\nВыберите бокал или введите букву для фильтрации списка:')
        data = input()
    data = exception.id_check(data, num_dic)
    if data == 0:
        print('\nОшибка ввода. Повторите ввод.')
        return name_glass()
    return data


def search_glass():
    print('Введите название бокала:')
    data = exception.search_exc(input(), 'Arec-Bar/glass.csv')
    if data == 0:
        print('\nБокал не найден. Выход в предыдущее меню.')
    return data


def delete_glass(data):
    if exception.delete_check(data, 'glass'):
        print('\nУдаление выполнено успешно. Выход в предыдущее меню.')
        return True
    print('\nУдаление невозможно. Существуют коктейли с данным бокалом. Выход в предыдущее меню.')
    return False


def create_measure(part, measure_list):
    data_list = list()
    if part == 1 or part == 'all':
        print('\nВведите название меры измерения:')
        data = input()
        while data == '':
            print('\nПоле должно быть заполнено.')
            print('\nВведите название меры измерения:')
            data = input()
        if part == 'all':
            data_list.append(data)
        else:
            measure_list[0] = data
    if part == 2 or part == 'all':
        print('\nВведите эквивалентное количество миллилитров данной мере измерения:\nЕсли это невозможно введите 0.')
        data = input()
        while not data.isdigit() and len(data) < 7:
            print('\nПоле должно быть заполнено числом. Максимально 6 символов.')
            print('\nВведите эквивалентное количество миллилитров данной мере измерения:\nЕсли это невозможно введите 0.')
            data = input()
        if data == '0':
            data = 'н/а'
        if part == 'all':
            data_list.append(data)
        else:
            measure_list[1] = data
    if part == 'all':
        print('\nМера измерения успешно добавлена. Выход в предыдущее меню.')
        return data_list
    else:
        print('\nМера измерения успешно изменена. Выход в предыдущее меню.')
        return measure_list
    

def name_measure():
    num_dic = measure.measures_show('all')
    if len(num_dic) == 1:
        print('\nСписок пуст.')
        return 0
    else:
        print('\nВыберите меру измерения или введите букву для фильтрации списка или нажмите Enter для выхода в предыдущее меню:')
    data = input()
    if data == '':
        return 0
    while not data.isdigit():
        if len(data) > 1:
            print('\nПо данному фильтру ничего не найдено.')
            num_dic = measure.measures_show('all')
        else:
            num_dic = measure.measures_show(data)
            if len(num_dic) == 1:
                print('\nПо данному фильтру ничего не найдено.')
                num_dic = measure.measures_show('all')
        print('\nВыберите меру измерения или введите букву для фильтрации списка:')
        data = input()
    data = exception.id_check(data, num_dic)
    if data == 0:
        print('\nОшибка ввода. Повторите ввод.')
        return name_measure()
    return data


def search_measure():
    print('Введите меру измерения:')
    data = exception.search_exc(input(), 'Arec-Bar/measure.csv')
    if data == 0:
        print('\nМера измерения не найдена. Выход в предыдущее меню.')
    return data


def delete_measure(data):
    if exception.delete_check(data, 'measure'):
        print('\nУдаление выполнено успешно. Выход в предыдущее меню.')
        return True
    print('\nУдаление невозможно. Существуют коктейли с данной мерой измерения. Выход в предыдущее меню.')
    return False


def create_make(replace):
    num_dic = make.make_show(replace)
    if len(num_dic) == 1:
        print('\nИнгредиенты для замены не найдены. Приготовление коктейля невозможно.')
        return 0
    print('\nВыберите ингредиент для замены:')
    data = input()
    data = exception.id_check(data, num_dic)
    if data == 0:
        print('\nОшибка ввода. Повторите ввод.')
        return name_make(replace)
    return data


def name_make():
    check = make.makes_show('all')
    if check == False:
        print('\nСписок пуст.')
        return 0
    else:
        print('\nВведите букву для фильтрации списка, введите 1 для фильтрации списка по количеству коктейлей или нажмите Enter для выхода в предыдущее меню:')
    data = input()
    if data == '':
        return 0
    while data != '0':
        while not data.isdigit():
            if len(data) > 1:
                print('\nПо данному фильтру ничего не найдено.')
                check = make.makes_show('all')
            else:
                check = make.makes_show(data)
                if check == False:
                    print('\nПо данному фильтру ничего не найдено.')
                    check = make.makes_show('all')
            print('\nВведите букву для фильтрации списка, введите 1 для фильтрации списка по количеству коктейлей или нажмите 0 для выхода в предыдущее меню:')
            data = input()
        if data == '1':
            check = make.makes_show('top')
            print('\nВведите букву для фильтрации списка, введите 1 для фильтрации списка по количеству коктейлей или нажмите 0 для выхода в предыдущее меню:')
            data = input()
        elif data != '0':
            check = make.makes_show('all')
            print('\nОшибка ввода. Повторите ввод.')
            print('\nВведите букву для фильтрации списка, введите 1 для фильтрации списка по количеству коктейлей или нажмите 0 для выхода в предыдущее меню:')
            data = input()
    return data