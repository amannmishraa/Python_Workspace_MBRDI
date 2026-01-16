import logging
try:
    sal = float(input("Enter your Salary: "))
    logging.info("Salary entered: %s", sal)
except ValueError as e:
    logging.error("Invalid numeric input for salary: %s", e)
leaves = int(input("Enter number of leaves taken: "))
pd_sal = sal / 30.0
bonuses = {
    "coder": 0.10 * sal,
    "designer": 0.15 * sal,
    "manager": 0.05 * sal
}

desg = input("Enter Your Designation (coder/designer/manager): ")
bonus = bonuses[desg]
extra_leaves = max(0, leaves - 15)
deduction = pd_sal * extra_leaves

final_salary = sal + bonus - deduction
print(f"Final salary for {desg.capitalize()}: {final_salary:.2f}")