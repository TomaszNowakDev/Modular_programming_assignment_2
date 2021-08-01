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


def main():
    weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    employee_name, employee_age = employee_details()
    print(employee_name, employee_age)
    wages_catch = list_of_wages(weeks)
    print(wages_catch)


if __name__ == '__main__':
    main()
