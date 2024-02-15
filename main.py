# Функция для просмотра истории транзакций
def view_transaction_history():
    print("1 - История доходов")
    print("2 - История расходов")
    choice = input("Выберите тип транзакции: ")
    if choice == "1":
        with open("revenues.txt", "r") as file:
            print("История доходов:")
            print(file.read())
    elif choice == "2":
        with open("expenditures.txt", "r") as file:
            print("История расходов:")
            print(file.read())
    else:
        print("Неверный выбор")


# Функция для анализа финансов
def financial_analysis():
    total_income = 0
    with open("revenues.txt", "r") as file:
        for line in file:
            total_income += float(line)

    total_expenditure = 0
    with open("expenditures.txt", "r") as file:
        for line in file:
            total_expenditure += float(line)

    balance = total_income - total_expenditure
    print(f"Общий доход: {total_income}")
    print(f"Общий расход: {total_expenditure}")
    print(f"Баланс: {balance}")


# Основное меню
def main_m():
    while True:
        try:
            main_main_menu = int(input("Выберите, что вы хотите сделать?\n"
                                       "1 - Посмотреть общий доход\n"
                                       "2 - Посмотреть общий расход\n"
                                       "3 - Ввести доход или расход\n"
                                       "4 - Просмотр истории транзакций\n"
                                       "5 - Анализ финансов\n"
                                       "6 - Выйти\n"
                                       "Ваш выбор: "))
            if main_main_menu == 1:
                print("Общий доход:")
                with open("revenues.txt", "r") as file:
                    print(file.read())
            elif main_main_menu == 2:
                print("Общий расход:")
                with open("expenditures.txt", "r") as file:
                    print(file.read())
            elif main_main_menu == 3:
                expenditures_or_revenues()
            elif main_main_menu == 4:
                view_transaction_history()
            elif main_main_menu == 5:
                financial_analysis()
            elif main_main_menu == 6:
                break
            else:
                print("Неверный выбор")
        except ValueError:
            print("Введите число")


# Росходи
def expenditures():
    main_menu = int(input(
        " 1 - Жилищные расходы: Включает аренду/ипотеку, коммунальные платежи, ремонт, страхование жилья и т. д.\n"
        " 2 - Питание: Расходы на продукты питания, обеды вне дома и т. д.\n"
        " 3 - Транспорт: Расходы на топливо, обслуживание автомобиля, общественный транспорт, такси и т. д.\n"
        " 4 - Здоровье: Расходы на медицинское обслуживание, лекарства, страхование здоровья и т. д.\n"
        " 5 - Личные расходы: Расходы на развлечения, хобби, путешествия, одежду, красоту и т. д.\n"
        " 6 - Образование: Расходы на образовательные курсы, книги, оплату учебы и т. д.\n"
        " 7 - Финансовые расходы: Расходы на выплату кредитов, проценты по кредитам, банковские сборы и т. д.\n"
        " 8 - Назад\n"
        " Выбирете категорию для ввода суммы росходов?: "))

    categories = {
        1: "Жилищные расходы",
        2: "Питание",
        3: "Транспорт",
        4: "Здоровье",
        5: "Личные расходы",
        6: "Образование",
        7: "Финансовые расходы"
    }

    if main_menu in categories:
        summa = input(f"Введите сумму расходов для категории '{categories[main_menu]}': ")
        with open("expenditures.txt", "a") as file:
            file.write(summa + "\n")
        print(f"Ваша сумма была успешно добавлена в расходы с категорией '{categories[main_menu]}'.")
    elif main_menu == 8:
        return main_m()
    else:
        print("Неверный выбор")
    return main_m()


# Доходы
def revenue():
    main_menu = int(input(
        " 1 - Заработная плата: Доход от работы, получаемый посредством зарплаты или почасовой оплаты.\n"
        " 2 - Бизнес-доход: Доход, полученный от собственного бизнеса или предпринимательской деятельности.\n"
        " 3 - Инвестиционные доходы: Доход от инвестиций, таких как проценты от банковских вкладов, дивиденды от акций, доход от облигаций и т. д.\n"
        " 4 - Социальные выплаты: Доход от социальных программ, таких как пенсии, пособия по безработице, пособия по инвалидности и т. д.\n"
        " 5 - Доход от недвижимости: Доход от аренды недвижимости или продажа недвижимости.\n"
        " 6 - Страховые выплаты: Доход от страховых выплат, таких как страхование жизни, медицинское страхование и т. д.\n"
        " 7 - Доход от образования: Доход от образовательных услуг, таких как учебные курсы, репетиторство и т. д.\n"
        " 8 - Назад\n"
        " Выбирете категорию для ввода суммы росходов?: "))

    categories = {
        1: "Заработная плата",
        2: "Бизнес-доход",
        3: "Инвестиционные доходы",
        4: "Социальные выплаты",
        5: "Доход от недвижимости",
        6: "Страховые выплаты",
        7: "Доход от образования"
    }

    if main_menu in categories:
        summa = input(f"Введите сумму доходов для категории '{categories[main_menu]}': ")
        with open("revenues.txt", "a") as file:
            file.write(summa + "\n")
        print(f"Ваша сумма была успешно добавлена в доходы с категорией '{categories[main_menu]}'.")
    elif main_menu == 8:
        return main_m()
    else:
        print("Неверный выбор")
    return main_m()


# Ввести Доход или Росход
def expenditures_or_revenues():
    choice = int(input("Введи что вы хотите сделать? (1 - Ввести доход, 2 - Ввести росход): "))
    if choice == 1:
        return revenue()
    elif choice == 2:
        return expenditures()


main_m()
