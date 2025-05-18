"""# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)"""

# Reorganizing code by writing two functions

def print_models(unprinted_designs, completed_models):
    # Simulate printing each design, until none are left.

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}.")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'doodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models) # you can pass a copy of list by using [:] but its better to use the original 
# The reason is because this avoids using time and memory needed to make a separate copy
show_completed_models(completed_models)