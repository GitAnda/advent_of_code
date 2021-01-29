def set_initial_intcode(filename, noun, verb):
    f = open(filename, 'r')
    file_content = f.read().split(',')
    f.close()

    intcode = [int(number) for number in file_content]
    intcode[1] = noun
    intcode[2] = verb

    return intcode


def process_opcode(opcode_idx, intcode):
    first_number = intcode[intcode[opcode_idx+1]]
    second_number = intcode[intcode[opcode_idx+2]]
    intcode[intcode[opcode_idx+3]] = first_number + second_number if intcode[opcode_idx] == 1 else first_number * second_number
    return intcode


def run_intcode_program(intcode):
    idx = 0
    while intcode[idx] != 99:
        intcode = process_opcode(idx, intcode)
        idx += 4
    
    return intcode

def determine_noun_and_verb_for_output(filename, output):
    for noun in range(100):
        for verb in range(100):
            intcode = set_initial_intcode(filename, noun, verb)
            if run_intcode_program(intcode)[0] == output:
                return noun, verb
    
    return -1,-1


if __name__ == '__main__':
    import sys

    intcode = set_initial_intcode(sys.argv[1], 12, 2)
    
    print('Exercise 2.1')
    intcode = run_intcode_program(intcode)
    print('Value', intcode[0], 'is left at position 0 after the program stops')

    print('\nExercise 2.2')
    output = 19690720
    noun,verb = determine_noun_and_verb_for_output(sys.argv[1], output)
    print(noun, verb)
    print('The noun-verb combination', noun*100+verb, 'produces the output', output)

