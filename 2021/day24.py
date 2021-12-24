import queue

file_name = 'day24.txt'
with open(file_name) as f:
    operations = f.read().strip().split('\n')

x = []
y = []
for j in range(14):
    line_x = 18 * j + 5
    x.append(int(operations[line_x][6:]))
    line_y = 18 * j + 15
    y.append(int(operations[line_y][6:]))

# print('{X}:', x)
# print('{Y}:', y, '\n')

stack = queue.LifoQueue()
conditions = []
for i in range(14):
    if x[i] > 0:
        stack.put((i, y[i]))
    else:
        j, n = stack.get()
        conditions.append((i, j, n + x[i]))
#         print(f'input[{i}] = input[{j}] + {n + x[i]}')
# print()

max_number = [0] * 14
min_number = [0] * 14
for a, b, d in conditions:
    max_number[a] = str(min(9, 9 + d))
    max_number[b] = str(min(9 - d, 9))
    min_number[a] = str(max(1 + d, 1))
    min_number[b] = str(max(1, 1 - d))

print(f"Part 1: {''.join(max_number)}")
print(f"Part 2: {''.join(min_number)}")


"""
The total instruction is the following instruction set repeated
for each input digit. The repetitions differ only in the values
of {Z}, {X} and {Y}. Note that if {X} is negative {Z} is 26 and
if {X} is positive {Z} is 1.

    inp w
    mul x 0
    add x z
    mod x 26
    div z {Z}
    add x {X}
    eql x w
    eql x 0
    mul y 0
    add y 25
    mul y x
    add y 1
    mul z y
    mul y 0
    add y w
    add y {Y}
    mul y x
    add z y

Each iteration does the following:
    1. Read input number
    2. if {X} is negative z = z / 26
    3. if (input == z % 26 + {X}) do nothing
       otherwise do z = 26 * z + input + {Y}

Note that if {X} is positive it is greater than 9. In this case,
the condition in step 3 can never be true since the input is 
smaller than 10 and z % 26 is a positive number. So if {X} is 
positive the value of z increases. (The value of z is always greater 
than or equal to zero.) The only case in which z decreases in an 
iteration is when {X} is negative and the condition in step 3 is 
true. 

We can think of z as a base-26 number. Each time the condition is 
not met we multiply by 26 and add a remainder. If {X} is negative 
we divide by 26 and discard the remainder. Thus, when {X} is 
positive the value of z will increase, but if {X} is negative z 
can decrease if the condition is met. 

In the input {X} is negative half of the time and positive the
other times. For z to end on 0 it MUST decrease when {X} is 
negative. So each time {X} is negative the condition of step 3 
must be met. 

We model the base-26 number using a stack of digits. Each time
the condition is not true, a value is pushed onto the stack.
Increasing the stack size is a multiplication by 26 and the 
remainder is the top value on the stack. Now, if {X} is negative
we must have that the remainder + {X} is equal to the input.  

    {X}: [12, 10, 10, -6, 11, -12, 11, 12, 12, -2, -5, -4, -4, -12]
    {Y}: [6, 2, 13, 8, 13, 8, 3, 11, 10, 8, 14, 6, 8, 2]

If we play this out, and assume that each time the condition of 
step 3 is met, we get the following actions on the stack:

    PUSH input[0] + 6
    PUSH input[1] + 2
    PUSH input[2] + 13
    POP                    input[3] = popped_value - 6
    PUSH input[4] + 13
    POP                    input[5] = popped_value - 12
    PUSH input[6] + 3
    PUSH input[7] + 11
    PUSH input[8] + 10
    POP                    input[9] = popped_value - 2
    POP                    input[10] = popped_value - 5
    POP                    input[11] = popped_value - 4
    POP                    input[12] = popped_value - 4
    POP                    input[13] = popped_value - 12

Each pop operation links one input value to another. The seven
conditions that result from this are:

    input[3] = input[2] + 7
    input[5] = input[4] + 1
    input[9] = input[8] + 8
    input[10] = input[7] + 6
    input[11] = input[6] - 1
    input[12] = input[1] - 2
    input[13] = input[0] - 6
    
Now, we can choose digits that meet these critera but are as
large (or small) as possible.
"""

