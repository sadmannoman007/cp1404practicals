# age=int(input("How old?"))
# if (age<=0)and (age>=120):
#  print("Invalid age,try again.")
# age=int(input("How old?"))

total=0.0
num_ages=int(input("How many?"))
for count = range(num_ages):
    age=int(input("How old?"))
    total += age
print("Average age",total/num_ages)