#
import random

# Initialize variables
workers = [] # list of workers
number_of_workers = 10 # Number of employees
genders = ['male', 'female'] # gender group

# Creation of a dynamic employee details
for i in range(1,number_of_workers):
    worker = { # Put worker details into a dictionary
        'employee ID': i,
        'name': f'Worker-{i}',
        'gender': random.choice(genders), # random selection of gender
        'salary': random.randint(7499, 30001) # random assignment of salary between $7,499 and $30,001
        }
    workers.append(worker) # append dictonary to the worker list
    i += 1 # Increment number by 1
print(workers)

# Assign employee level based on conditional statements
for w in workers:
    if w['salary'] > 10000 < 20000:
        w.update({'employee Level': 'A1'})
    elif w['salary'] > 7500 < 30000 and w['gender'] == 'female':
        w.update({'employee Level': 'A5-F'})

print("=======================")
print(workers)


