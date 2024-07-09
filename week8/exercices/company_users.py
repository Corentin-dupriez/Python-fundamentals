def add_employee_to_company(company_name: str, employee: str):
    if companies_and_employees.get(company_name):
        if employee not in companies_and_employees[company_name]:
            companies_and_employees[company_name].append(employee)
    else:
        companies_and_employees[company_name] = [employee]


def print_companies(company_list: dict):
    for company_name in company_list.keys():
        print(company_name)
        for employee_name in company_list[company_name]:
            print(f'-- {employee_name}')


companies_and_employees = dict()

while True:
    command = input()
    if command == 'End':
        break
    company, number = command.split(' -> ')
    add_employee_to_company(company, number)

print_companies(companies_and_employees)
