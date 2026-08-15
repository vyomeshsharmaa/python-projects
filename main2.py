import employee2_module

e = employee2_module.Employee("Ramesh", 40000)
print(e.describe())

m = employee2_module.Manager("Sunita", 55000, 5)
print(m.describe())

i = employee2_module.Intern("Aman",20000, "Sunita")
print(i.describe())

staff = [
    employee2_module.Employee("Vyomesh", 1900000000),
    employee2_module.Intern("Krish", 190000, "Vyomesh"),
    employee2_module.Manager("Void", 900000, 10)
]

print(f"Total Salary of staff {employee2_module.total_payroll(staff)}") 