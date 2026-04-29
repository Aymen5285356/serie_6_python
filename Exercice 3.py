employee = {
    'emp1': {'name': 'Fatima Ezzahrae', 'genre': 'F', 'salary': 7500},
    'emp2': {'name': 'Ibrahim', 'genre': 'H', 'salary': 8000},
    'emp3': {'name': 'Khalid', 'genre': 'H', 'salary': 6500},
    'emp4': {'name': 'Karima', 'genre': 'F', 'salary': 6500},
}
employee['emp4']['salary'] = 7000
cumul_salaires = 0
for emp in employee:
    employee[emp]['name'] = employee[emp]['name'].upper()
    cumul_salaires += employee[emp]['salary']
hommes = {}
femmes = {}
for emp in employee:
    if employee[emp]['genre'] == 'H':
        hommes[emp] = employee[emp]
    else:
        femmes[emp] = employee[emp]
