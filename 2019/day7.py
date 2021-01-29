def find_highest_signal_to_thrusters():
    from subprocess import run, PIPE
    from itertools import permutations

    phase_setting_candidates = permutations((0, 1, 2, 3, 4), 5)
    program_call = ['py', 'Intcode.py', 'day7.txt']
    thrusters = ["A", "B", "C", "D", "E"]

    max_thruster_signal = 0
    for phase_setting in phase_setting_candidates:
        signal = 0
        for i in range(5):
            print(signal, '->', thrusters[i], '->', end=' ')
            p = run(program_call, stdout=PIPE, input=str(phase_setting[i]) + '\n' + str(signal) + '\n',
                    encoding='ascii')
            signal = int(p.stdout.strip().split(' ')[-1])
        print(signal)
        max_thruster_signal = max(max_thruster_signal, signal)

    return max_thruster_signal


def find_highest_signal_to_thrusters_with_loop_command_line():
    from subprocess import Popen, PIPE

    # from itertools import permutations
    # phase_setting_candidates = permutations((5, 6, 7, 8, 9), 5)
    # TODO loop over all phase settings

    program_call = ['py', 'Intcode.py', 'day7_test.txt']

    max_thruster_signal = 0

    phase_setting = (5, 6, 7, 8, 9)
    signal = 0

    amplifier_a = Popen(program_call, stdin=PIPE, stdout=PIPE)
    amplifier_a.stdin.write(bytes(str(phase_setting[0]) + '\n' + str(signal) + '\n', 'utf-8'))
    # TODO fix reading output (use spaces?)
    signal = amplifier_a.stdout.read(10)

    amplifier_b = Popen(program_call, stdin=PIPE, stdout=PIPE)
    amplifier_b.stdin.write(bytes(str(phase_setting[0]) + '\n' + str(signal) + '\n', 'utf-8'))
    signal = amplifier_b.stdout.read(10)

    amplifier_c = Popen(program_call, stdin=PIPE, stdout=PIPE)
    amplifier_c.stdin.write(bytes(str(phase_setting[0]) + '\n' + str(signal) + '\n', 'utf-8'))
    signal = amplifier_c.stdout.read(10)

    amplifier_d = Popen(program_call, stdin=PIPE, stdout=PIPE)
    amplifier_d.stdin.write(bytes(str(phase_setting[0]) + '\n' + str(signal) + '\n', 'utf-8'))
    signal = amplifier_d.stdout.read(10)

    amplifier_e = Popen(program_call, stdin=PIPE, stdout=PIPE)
    amplifier_e.stdin.write(bytes(str(phase_setting[0]) + '\n' + str(signal) + '\n', 'utf-8'))
    signal = amplifier_e.stdout.read(10)

    # TODO add amplifier loops

    max_thruster_signal = max(max_thruster_signal, signal)

    return max_thruster_signal


def find_highest_signal_to_thrusters_with_loop():
    from itertools import permutations
    from Intcode import IntcodeProgram
    import sys

    f = open(sys.argv[1], 'r')
    file_content = f.read().split(',')
    f.close()

    phase_setting_candidates = permutations((5, 6, 7, 8, 9), 5)

    max_thruster_signal = 0
    for phase_setting in phase_setting_candidates:
        print(phase_setting)
        signal = 0

        amplifier_a = IntcodeProgram([int(number) for number in file_content])
        amplifier_b = IntcodeProgram([int(number) for number in file_content])
        amplifier_c = IntcodeProgram([int(number) for number in file_content])
        amplifier_d = IntcodeProgram([int(number) for number in file_content])
        amplifier_e = IntcodeProgram([int(number) for number in file_content])

        amplifier_a.run_intcode_program_until_next_input(phase_setting[0])
        signal = amplifier_a.run_intcode_program_until_next_input(signal)
        amplifier_b.run_intcode_program_until_next_input(phase_setting[1])
        signal = amplifier_b.run_intcode_program_until_next_input(signal)
        amplifier_c.run_intcode_program_until_next_input(phase_setting[2])
        signal = amplifier_c.run_intcode_program_until_next_input(signal)
        amplifier_d.run_intcode_program_until_next_input(phase_setting[3])
        signal = amplifier_d.run_intcode_program_until_next_input(signal)
        amplifier_e.run_intcode_program_until_next_input(phase_setting[4])
        signal = amplifier_e.run_intcode_program_until_next_input(signal)

        while amplifier_e.sequence[amplifier_e.idx] != 99:
            signal = amplifier_a.run_intcode_program_until_next_input(signal)
            signal = amplifier_b.run_intcode_program_until_next_input(signal)
            signal = amplifier_c.run_intcode_program_until_next_input(signal)
            signal = amplifier_d.run_intcode_program_until_next_input(signal)
            signal = amplifier_e.run_intcode_program_until_next_input(signal)

        max_thruster_signal = max(max_thruster_signal, signal)

    return max_thruster_signal

if __name__ == '__main__':

    thruster_signal = find_highest_signal_to_thrusters_with_loop()
    print('The maximum thruster signal is', thruster_signal)


