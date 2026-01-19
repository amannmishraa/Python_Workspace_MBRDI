# def evenorodd(num):
#     if num % 2 == 0:
#         print('even')
#     else:
#         print('odd')


class Employee:
    def __init__(self, name, salary, emp_id):
        self.name = name
        self.salary = salary
        self.__id = emp_id

    def get_id(self):
        return self.__id

    def display_info(self):
        print("Name   :", self.name)
        print("Salary :", self.salary)
        print("ID     :", self.__id)

    def dict_save(self):
        return {
            "Name": self.name,
            "Salary": self.salary,
            "ID": self.__id
        }


# Employees
emp1 = Employee("ABC", 3000, 12)
emp2 = Employee("New", 3000, 11)

emps = {emp1, emp2}

# Check duplicate by ID
emp3 = Employee("New", 3000, 13)
flag = False

for item in emps:
    if item.get_id() == emp3.get_id():
        print("Already exists")
        flag = True
        break

if not flag:
    emps.add(emp3)

# Save as list of dictionaries
emp_list = []
emp_list.append(emp1.dict_save())
emp_list.append(emp2.dict_save())

# Dictionary using ID as key
emp_dict = {
    emp1.get_id(): emp1,
    emp2.get_id(): emp2,
    emp3.get_id(): emp3
}

# # Display all employees
# for emp in emp_dict.values():
#     emp.display_info()
#     print("-" * 30)


class Manager(Employee):
    def __init__(self, name, salary, emp_id, number_of_teams):
        super().__init__(name, salary, emp_id)
        self.__number_of_teams = number_of_teams

    def show_details(self):
        print("Manager Details")
        print("---------------")
        super().display_info()
        print("Teams Managed:", self.__number_of_teams)
mgr = Manager("Amit", 8000, 101, 5)
# mgr.show_details()

from abc import ABC,abstractmethod
class Electronics(ABC):
    @abstractmethod
    def play_video():
        pass
class Laptop(Electronics):
    def play_video(self):
        print("press play to play")
class Mobile(Electronics):
    def play_video(self):
        print("press play button")
laptop = Laptop()
laptop.play_video()
mobile = Mobile()
mobile.play_video()