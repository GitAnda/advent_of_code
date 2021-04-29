if __name__ == '__main__':
    with open("day16.txt") as f:
        array = [int(char) for char in f.readline()]
    offset = int(''.join([str(digit) for digit in array[0:7]]))
    print('offset:', offset)
    s = len(array)
    array = array[offset%s:] + array*(10000-offset//s-1)

    for x in range(100):
        for n in range(len(array)-1, -1, -1):
            array[n] = (array[n] + array[n+1]) % 10 if n < len(array)-1 else array[n]

    print(''.join([str(digit) for digit in array[:8]]))