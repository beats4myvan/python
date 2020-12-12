first_emp_efficiency = int(input())
second_emp_efficiency = int(input())
third_emp_efficiency = int(input())
count_of_ppl = int(input())
time_need = 0
answers = first_emp_efficiency + second_emp_efficiency + third_emp_efficiency

while count_of_ppl > 0:
    time_need += 1
    if time_need % 4 == 0:
        pass
    else:
        count_of_ppl -= answers
print(f"Time needed: {time_need}h.")
