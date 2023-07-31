# Algoritimo para calcular sua idade usando meses

# Imports library to grab today date
import datetime

# Gets local date
today = datetime.datetime.now()
print(f"Hoje é dia {today.day} do mês {today.month} de {today.year}\n")

# Inputs
ano = int(input("Em que ano você nasceu? (Ex: 2004): "))
mes = int(input("Em que ano você nasceu? (Ex: 9): "))
dia = int(input("Em que dia você nasceu? (Ex: 3): "))

# Calculates date using years
age = today.year - ano

# Calculates if user had a bday this year
if today.month < mes: # If his bday month didn't passed yet, age = -1
   age -= 1
elif today.month == mes and today.day < dia: # If his bday month is the actual one, but day didn't passed yet, age = -1
   age -= 1

# Calculates date using months
monthFinal = today.month - mes

# Same as if above but with month/days. If his bday didn't passed yet, month = -1
if today.day < dia:
   monthFinal -= 1
if monthFinal < 0:
   monthFinal += 12

# Outputs results
print(f"Você tem {age} anos de idade e faltam {monthFinal} para seu aniversário!")