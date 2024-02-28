def make_pizza(picked_pizza, picked_topping):
    if picked_pizza == 0:
        print("Заказ завершен")
    elif picked_pizza in [1, 2, 3, 4]:
        toppings = {
            "Дополнительный сыр": 0,
            "Халопеньо": 0,
            "Ананасы": 0,
            "Ветчина": 0
        }
        if picked_topping in toppings:
            toppings[picked_topping] += 1
        selected_pizza = ""
        pizza_price = 0
        if picked_pizza == 1:
            selected_pizza = 'Пицца "4 сыра"'
            pizza_price += 3000
        elif picked_pizza == 2:
            selected_pizza = 'Пицца "Пепперони"'
            pizza_price += 3000
        elif picked_pizza == 3:
            selected_pizza = 'Пицца "Барбекью"'
            pizza_price += 4000
        elif picked_pizza == 4:
            selected_pizza = 'Пицца "Жульен"'
            pizza_price += 4500
        if picked_topping == 0:
            print(f"{selected_pizza} была добавлена в заказ!")
        else:
            print(f"{selected_pizza} с {picked_topping} была добавлена в заказ!")
        done_pizza = [selected_pizza, picked_topping]
        return pizza_bucket(done_pizza, pizza_price)


def pizza_bucket(done_pizza, pizza_price):
    bucket = []
    bucket.insert(0, done_pizza)
    return bucket, check_list(pizza_price)


def check_list(pizza_price):
    return f"Общая стоимость: {pizza_price} тенге"


def menu():
    print("==" * 50)
    print('Меню:\n1. Пицца "4 сыра" - 3000 тенге\n2. Пицца "Пепперони" - 3000 тенге\n'
          '3. Пицца "Барбекью" - 4000 тенге\n4. Пицца "Жульен" - 4500 тенге')
    print("==" * 50)
    picked_pizza = int(input("Введите номер вашей пиццы (0 для завершения): "))
    picked_topping = int(input('Дополнительные ингредиенты:\n1. Дополнительный сыр\n'
                               '2. Халопеньо\n3. Ананасы\n4. Ветчина\nВведите номер ингредиента (0 для пропуска): '))
    return make_pizza(picked_pizza, picked_topping)


if __name__ == "__main__":
    print('Добро пожаловать в пиццерию!')
    print(menu())
