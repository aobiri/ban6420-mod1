#
import random

# Initialize variables
workers = [] # list of workers
number_of_workers = 10 # Number of employees
genders = ['male', 'female'] # gender group

# Creation of a dynamic employee details
try:
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
except ValueError as ve:
    print("ValueError:", ve)
except IndexError as ie:
    print("IndexError:", ie)
except Exception as e:
    print("An error occurred while creating worker details.")


# Assign employee level based on conditional statements
try:
    for worker in workers:
        if worker['salary'] < 10000:
            worker['level'] = 'Junior'
        elif 10000 <= worker['salary'] < 20000:
            worker['level'] = 'Mid-level'
        else:
            worker['level'] = 'Senior'
    print(workers)
except ValueError as ve:
    print("ValueError:", ve)
except IndexError as ie:
    print("IndexError:", ie)
except Exception as e:
    print("An error occurred while assigning employee levels.")


