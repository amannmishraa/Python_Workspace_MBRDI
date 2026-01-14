sal = int(input("Enter your Salary: "))
pd_sal = sal/30
coder_bonus = 0.1*sal
designer_bonus = 0.15*sal
Manager_bonus = 0.05*sal
desg = input('Enter Your Designation: ')
Leaves = int(input('Enter number of leaves taken: '))
if (desg=="coder" and Leaves >= 15):
    salary = sal+coder_bonus - pd_sal*(Leaves-15)
    print(salary)
else:
    salary = sal+coder_bonus


if (desg=="designer" and Leaves >= 15):
    salary = sal+designer_bonus - pd_sal*(Leaves-15)
    print(salary)
else:
    salary = sal+designer_bonus



if (desg=="manager" and Leaves >= 15):
    salary = sal+Manager_bonus - pd_sal*(Leaves-15)
else:
    salary = sal+Manager_bonus



