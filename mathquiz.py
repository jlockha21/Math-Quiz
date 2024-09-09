import random
import time

OPPERATORS = ["+","-","*"]
MIN_APERAND = 3
MAX_APERAND = 12
TOTAL_PROBLEMS = 10  

def generate_problem():
    left = random.randint(MIN_APERAND, MAX_APERAND)
    right = random.randint(MIN_APERAND, MAX_APERAND)
    operator = random.choice(OPPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = + end_time - start_time

print("------------------------")
print("Nice work! YOu finished in", total_time, "seconds!")