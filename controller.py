import user_interface
import ingredient
import cocktail
import glass
import measure
import make


def click_button():
    data = user_interface.main_menu()
    if data == 1:
        return click_button_cocktails()
    if data == 2:
        return click_button_ingredients()
    if data == 3:
        return click_button_glasses()
    if data == 4:
        return click_button_measures()
    if data == 5:
        return click_button_makes()
    if data == 0:
        return


def click_button_cocktails():
    data = user_interface.cocktails_menu()
    if data == 1:
        cocktail_name = user_interface.search_cocktail()
        if cocktail_name == 0:
            return click_button_cocktails()
        return click_button_cocktail(cocktail_name, 1)
    if data == 2:
        cocktail_name = user_interface.name_cocktail('cocktail', None)
        if cocktail_name == 0:
            return click_button_cocktails()
        return click_button_cocktail(cocktail_name, 1)
    if data == 3:
        cocktail_name = user_interface.name_cocktail('select', None)
        if cocktail_name == 0:
            return click_button_cocktails()
        return click_button_cocktail(cocktail_name, 1)
    if data == 4:
        new_cocktail = user_interface.create_cocktail()
        cocktail.cocktail_add(new_cocktail)
        return click_button_cocktails()
    if data == 0:
        return click_button()


def click_button_ingredients():
    data = user_interface.ingredients_menu()
    if data == 1:
        ingredient_name = user_interface.search_ingredient()
        if ingredient_name == 0:
            return click_button_ingredients()
        return click_button_ingredient(ingredient_name)
    if data == 2:
        ingredient_name = user_interface.name_ingredient('all')
        if ingredient_name == 0:
            return click_button_ingredients()
        return click_button_ingredient(ingredient_name)
    if data == 3:
        ingredient_name = user_interface.name_ingredient('select')
        if ingredient_name == 0:
            return click_button_ingredients()
        return click_button_ingredient(ingredient_name)
    if data == 4:
        new_ingredient = user_interface.create_ingredient('all', None)
        ingredient.ingredient_add(new_ingredient)
        return click_button_ingredients()
    if data == 0:
        return click_button()


def click_button_glasses():
    data = user_interface.glasses_menu()
    if data == 1:
        glass_name = user_interface.search_glass()
        if glass_name == 0:
            return click_button_glasses()
        return click_button_glass(glass_name)
    if data == 2:
        glass_name = user_interface.name_glass()
        if glass_name == 0:
            return click_button_glasses()
        return click_button_glass(glass_name)
    if data == 3:
        new_glass = user_interface.create_glass()
        glass.glass_add(new_glass)
        return click_button_glasses()
    if data == 0:
        return click_button()


def click_button_measures():
    data = user_interface.measures_menu()
    if data == 1:
        measure_name = user_interface.search_measure()
        if measure_name == 0:
            return click_button_measures()
        return click_button_measure(measure_name)
    if data == 2:
        measure_name = user_interface.name_measure()
        if measure_name == 0:
            return click_button_measures()
        return click_button_measure(measure_name)
    if data == 3:
        new_measure = user_interface.create_measure('all', None)
        measure.measure_add(new_measure)
        return click_button_measures()
    if data == 0:
        return click_button()


def click_button_makes():
    data = user_interface.name_make()
    if data == 0:
        return click_button()


def click_button_cocktail(cocktail_name, quantity):
    cocktail.cocktail_show(cocktail_name, quantity)
    data = user_interface.cocktail_menu()
    if data == 1:
        return click_button_make(cocktail_name, quantity)
    if data == 2:
        quantity = user_interface.quantity_cocktail()
        return click_button_cocktail(cocktail_name, quantity)
    if data == 3:
        cocktail.cocktail_show(cocktail_name, 1)
        data = user_interface.cocktail_change_menu()
        if data == 0:
            return click_button_cocktail(cocktail_name, 1)
        cocktail_list = cocktail.cocktail_list(cocktail_name)
        change_cocktail = user_interface.create_cocktail(data, cocktail_list)
        cocktail.cocktail_change(cocktail_name, change_cocktail)
        return click_button_cocktail(cocktail_name, 1)
    if data == 4:
        cocktail.cocktail_delete(cocktail_name)
        user_interface.delete_cocktail()
        return click_button_cocktails()
    if data == 0:
        return click_button_cocktails()


def click_button_ingredient(ingredient_name):
    ingredient.ingredient_show(ingredient_name)
    data = user_interface.ingredient_menu()
    if data == 1:
        cocktail_name = user_interface.name_cocktail(
            'ingredient', ingredient_name)
        if cocktail_name == 0:
            return click_button_ingredient(ingredient_name)
        return click_button_cocktail(cocktail_name, 1)
    if data == 2:
        ingredient.ingredient_show(ingredient_name)
        data = user_interface.ingredient_change_menu()
        if data == 0:
            return click_button_ingredient(ingredient_name)
        ingredient_list = ingredient.ingredient_list(ingredient_name)
        change_ingredient = user_interface.create_ingredient(
            data, ingredient_list)
        ingredient.ingredient_change(ingredient_name, change_ingredient)
        return click_button_ingredient(ingredient_name)
    if data == 3:
        if user_interface.delete_ingredient(ingredient_name):
            ingredient.ingredient_delete(ingredient_name)
        return click_button_ingredients()
    if data == 0:
        return click_button_ingredients()


def click_button_glass(glass_name):
    glass.glass_show(glass_name)
    data = user_interface.glass_menu()
    if data == 1:
        cocktail_name = user_interface.name_cocktail('glass', glass_name)
        if cocktail_name == 0:
            return click_button_glass(glass_name)
        return click_button_cocktail(cocktail_name, 1)
    if data == 2:
        glass.glass_show(glass_name)
        change_glass = user_interface.create_glass()
        glass.glass_change(glass_name, change_glass)
        return click_button_glass(glass_name)
    if data == 3:
        if user_interface.delete_glass(glass_name):
            glass.glass_delete(glass_name)
        return click_button_glasses()
    if data == 0:
        return click_button_glasses()


def click_button_measure(measure_name):
    measure.measure_show(measure_name)
    data = user_interface.measure_menu()
    if data == 1:
        measure.measure_show(measure_name)
        data = user_interface.measure_change_menu()
        if data == 0:
            return click_button_measure(measure_name)
        measure_list = measure.measure_list(measure_name)
        change_measure = user_interface.create_measure(data, measure_list)
        measure.measure_change(measure_name, change_measure)
        return click_button_measure(measure_name)
    if data == 2:
        if user_interface.delete_measure(measure_name):
            measure.measure_delete(measure_name)
        return click_button_measures()
    if data == 0:
        return click_button_measures()


def click_button_make(cocktail_name, quantity):
    replace_dic = {}
    replace = make.make_check(cocktail_name, quantity, replace_dic)
    if replace == 0:
        click_button_cocktail(cocktail_name, quantity)
    if len(replace) < 1:
        make.make_cocktail(cocktail_name, quantity, replace_dic)
        return click_button_cocktails()
    while len(replace) > 0:
        make_name = user_interface.create_make(replace)
        if make_name == 0:
            return click_button_cocktails()
        data = user_interface.make_menu()
        if data == 1:
            replace_dic[replace[1]] = make_name
            replace = make.make_check(cocktail_name, quantity, replace_dic)
        if data == 2:
            make.make_replace(make_name, replace)
            replace = make.make_check(cocktail_name, quantity, replace_dic)
        if data == 0:
            return click_button_cocktails()
    make.make_cocktail(cocktail_name, quantity, replace_dic)
    return click_button_cocktails()
