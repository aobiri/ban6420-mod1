# Load necessary library
library(dplyr)

# Initialize variables
workers <- list() # list of workers
number_of_workers <- 450 # Number of employees
genders <- c('male', 'female') # gender group

# Creation of a dynamic employee details
tryCatch({
    for (i in 1:number_of_workers) {
        worker <- list( # Put worker details into a list
            employee_ID = i,
            name = paste('Worker', i, sep = '-'),
            gender = sample(genders, 1), # random selection of gender
            salary = sample(7499:30001, 1) # random assignment of salary between $7,499 and $30,001
        )
        workers[[i]] <- worker # append list to the worker list
    }
    print(workers)
}, error = function(e) {
    cat("An error occurred while creating worker details:", e$message, "\n")
})

# Assign employee level based on conditional statements
tryCatch({
    for (worker in workers) {
        if (worker$salary < 10000) {
            worker$level <- 'Junior'
        } else if (worker$salary >= 10000 && worker$salary < 20000) {
            worker$level <- 'Mid-level'
        } else {
            worker$level <- 'Senior'
        }
    }
    print(workers)
}, error = function(e) {
    cat("An error occurred while assigning employee levels:", e$message, "\n")
})