if __name__ == '__main__':
    import sys
    from Intcode import IntcodeProgram

    f = open(sys.argv[1], 'r')
    file_content = f.read().split(',')
    f.close()

    intcode = IntcodeProgram([int(number) for number in file_content])
    intcode.run_intcode_program()
