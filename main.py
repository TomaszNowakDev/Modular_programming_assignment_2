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


def main():
    weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    employee_name, employee_age = employee_details()
    print(employee_name, employee_age)
    wages_catch = list_of_wages(weeks)
    over150_a_day = over150(weeks, wages_catch)
    print(f'Days with more than 150€ earned: {over150_a_day}')
    required_money = money_for_bonus(wages_catch)
    print(f'Money required for bonus {required_money:.2f}€.')


if __name__ == '__main__':
    main()
