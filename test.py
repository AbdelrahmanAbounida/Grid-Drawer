import random

def generate_students():
    _max = 30

    course = [[],[],[]]
    wait_list = [[],[],[]]
    for i in range(0,_max):
        index = random.randint(0,2)

        if(len(course[index]) == 10):
            wait_list[index].append(i)
        else:
            course[index].append(i)
        print(f"Signup {i+1} for section {index+1}")

    print()
    print()
    print("__REGESTRATION SUMMARY__")
    print(f"section 1 has {len(course[0])} students enrolled. There are {len(wait_list[0])} in the waitlist.")
    print(f"section 2 has {len(course[1])} students enrolled. There are {len(wait_list[1])} in the waitlist.")
    print(f"section 3 has {len(course[2])} students enrolled. There are {len(wait_list[2])} in the waitlist.")


if __name__ == '__main__':
    generate_students()