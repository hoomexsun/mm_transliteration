import random

num_person = 10
num_scripts = 20
num_script_per_person = 5

persons = [f"P{i}" for i in range(101, 101 + num_person)]
scripts = [f"S{i}" for i in range(201, 201 + num_scripts)]

distribution = {
    person: random.sample(scripts, num_script_per_person) for person in persons
}
print(distribution)
