if __name__ == '__main__':
    with open("day16.txt") as f:
        array = [int(char) for char in f.readline()]
    # array = {i: int(char) for i, char in enumerate('03036732577212944063491565474664')}
    s = len(array)

    for x in range(100):
        new_array = []

        for n, digit in enumerate(array):
            sign = 1
            number = 0
            for i in range((s-n-1)//(2*(n+1))+1):
                number += sign*sum(array[n+2*(n+1)*i:min((2*n+1)+2*(n+1)*i, s)])
                sign *= -1
            new_array.append(abs(number) % 10)

        array = new_array

    print(''.join([str(digit) for digit in array[0:8]]))