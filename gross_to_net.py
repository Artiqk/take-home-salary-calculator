
def get_net_salary(gross_salary):
    return gross_salary - (gross_salary * 0.23)


def get_tax_range_index(net_salary, tax_range):
    index = 0
    
    for tax in tax_range:
        min_tax = tax[0]
        
        max_tax = tax[1]
        
        if net_salary >= min_tax and net_salary <= max_tax:
            return index
        
        index += 1


import sys

def get_total_tax(net_salary, tax_range):
    
    tax_range_index = get_tax_range_index(net_salary, tax_range)

    total_tax = 0

    for i in range(tax_range_index + 1):
        min_tax = tax_range[i][0]
        
        max_tax = tax_range[i][1]
       
        percentage = tax_range_percentage[i]
        
        if net_salary >= max_tax:
            total_tax += (max_tax - min_tax) * percentage
        else:
            total_tax += (net_salary - min_tax) * percentage
    
    return total_tax




if len(sys.argv) != 2:
    print(f"Usage : python {sys.argv[0]} <salary>")
    exit(1)


try:
    int(sys.argv[1])
except:
    print("Argument is not a number")
    exit(1)


gross_salary = int(sys.argv[1])

tax_range = [
    [0, 10777],
    [10778, 27478],
    [27479, 78570],
    [78571, 168994],
    [168995, 999999]
]

tax_range_percentage = [0, 0.11, 0.3, 0.41, 0.45]

net_salary = int(get_net_salary(gross_salary))

annual_tax = int(get_total_tax(net_salary, tax_range))

take_home_salary = int(net_salary - annual_tax)

separator = ','

print(f"GROSS SALARY : {format(gross_salary, separator)}€")
print(f"NET SALARY : {format(net_salary, separator)}€")
print("================================")
print(f"TOTAL TAX (ANNUAL): {format(annual_tax, separator)}€")
print(f"TOTAL TAX (MONTHLY): {format(int(annual_tax / 12), separator)}€")
print("================================")
print(f"TAKE HOME SALARY (ANNUAL): {format(take_home_salary, separator)}€")
print(f"TAKE HOME SALARY (MONTHLY) : {format(int(take_home_salary / 12), separator)}€")