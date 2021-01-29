def load_layers(filename, width, length):
    f = open(filename, 'r')
    raw_input = [int(x) for x in f.read().strip()]
    f.close()

    rows = [raw_input[i*width:(i+1)*width] for i in range(len(raw_input) // width)]
    layers = [rows[i*length:(i+1)*length] for i in range(len(rows)//length)]

    return layers


def count_digits_in_layer(layer, digit):
    return sum([row.count(digit) for row in layer])


def find_layer_with_fewest_zeros(layers):
    count = 100000
    for i,layer in enumerate(layers):
        # print(i, count_digits_in_layer(layer, 0), count_digits_in_layer(layer, 1), count_digits_in_layer(layer, 2))
        if count_digits_in_layer(layer, 0) < count:
            count = count_digits_in_layer(layer, 0)
            idx_min_layer = i

    return layers[idx_min_layer]


def find_decoded_image(layers):
    image = layers[0]
    for i in range(len(image)):
        for j in range(len(image[0])):
            for layer in layers:
                if layer[i][j] != 2:
                    image[i][j] = layer[i][j]
                    break

    return image


def print_decoded_image(image):
    from termcolor import colored
    from colorama import init
    init(autoreset=True)
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == 0:
                print(' ', end='')
            elif image[i][j] == 1:
                print(colored(' ', 'white', 'on_white'), end='')
            else:
                print(colored(str(image[i][j]), 'white', 'on_red'), end='')
        print('\n', end='')


if __name__ == '__main__':
    import sys

    layers = load_layers(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

    print('Exercise 8.1')
    layer_with_fewest_zeros = find_layer_with_fewest_zeros(layers)
    print('The answer is', count_digits_in_layer(layer_with_fewest_zeros, 1) * count_digits_in_layer(layer_with_fewest_zeros, 2))

    decoded_image = find_decoded_image(layers)
    print_decoded_image(decoded_image)


