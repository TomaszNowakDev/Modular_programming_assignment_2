# Tomasz Nowak
import functions


def employee_details():
    name = functions.read_non_empty_string("Employee name ==> ")
    age = functions.read_positive_integer("Employee age ==> ")
    return name, age


def list_of_wages(days):
    wages = []
    for i in range(len(days)):
        x = functions.read_positive_float(f'{days[i]} ==> ')
        wages.append(x)
    return wages


def over150(days, wages):
    return [days[i] for i in range(len(days)) if wages[i] > 150]


def money_for_bonus(money):
    return sum(money) * .1


def display(name, age, days, wage):
    print(f"{'Name':15}{'Age':<7}{'Day':<10}{'Wage':<10}")
    print('============================================')
    for i in range(len(days)):
        if wage[i] > 175:
            print(f"{name:15}{age:<7}{days[i]:<10}{wage[i]:.2f}€{'':<3}{'#'}")
        else:
            print(f'{name:15}{age:<7}{days[i]:<10}{wage[i]:.2f}€')


def most_earned(days, wages):
    me = max(wages)
    print(f'\nMost earned ({me:.2f}€) in:')
    for i in range(len(wages)):
        if wages[i] == me:
            print(f'{days[i]}')


def display_day(days, wages):
    day_wanted = functions.valid_day_of_week("\nEnter a day ==> ")
    for i in range(len(days)):
        if day_wanted == days[i].lower():
            print(f'Money earned on {days[i]} => {wages[i]:.2f}€')


def reduced(x):
    for i in range(len(x)):
        x[i] = x[i] * .95


def main():
    weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    employee_name, employee_age = employee_details()
    print(employee_name, employee_age)
    wages_catch = list_of_wages(weeks)
    over150_a_day = over150(weeks, wages_catch)
    print(f'\nDays with more than 150€ earned: {over150_a_day}')
    required_money = money_for_bonus(wages_catch)
    print(f'\nMoney required for bonus {required_money:.2f}€.\n')
    display(employee_name, employee_age, weeks, wages_catch)
    most_earned(weeks, wages_catch)
    display_day(weeks, wages_catch)
    reduced(wages_catch)
    print('\nMoney after reduction:')
    display(employee_name, employee_age, weeks, wages_catch)


if __name__ == '__main__':
    main()
