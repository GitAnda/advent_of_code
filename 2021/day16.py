file_name = 'day16.txt'
with open(file_name) as f:
    code, key = f.read().strip().split('\n\n')
key = {line.split(' = ')[0]: line.split(' = ')[1] for line in key.split('\n')}

class BITS:
    def __init__(self, initial_code):
        self.version_sum = 0
        binary_code = ''.join([key[c] for c in initial_code])
        self.cracked_code = self.read_packet(binary_code)[0][0]
        self.answer = self.do_operation(*self.cracked_code)

    @staticmethod
    def read_literal(literal_string):
        binary_number = []
        id = 0
        while True:
            binary_number.append(literal_string[id + 1:id + 5])
            if literal_string[id] == '0':
                break
            id += 5
        return int(''.join(binary_number), 2), id+5

    def read_packet(self, string, max_count=None):
        children = []
        idx = 0
        count = 0
        while True:
            version = int(string[idx:idx + 3], 2)
            self.version_sum += version
            type_id = int(string[idx + 3:idx + 6], 2)
            idx += 6

            if type_id == 4:
                content, length = self.read_literal(string[idx:])
                idx += length
            else:
                length_id = string[idx]
                idx += 1
                if length_id == '0':
                    length = int(string[idx:idx + 15], 2)
                    idx += 15
                    content, i = self.read_packet(string[idx:idx + length])
                else:
                    length = int(string[idx:idx + 11], 2)
                    idx += 11
                    content, i = self.read_packet(string[idx:], max_count=length)
                idx += i
            children.append((type_id, content))
            count += 1

            if (max_count and count >= max_count) or string[idx:].count('1') == 0:
                break

        return children, idx

    def do_operation(self, type_id, values):
        if type_id == 0:
            return self.operation_0(values)
        elif type_id == 1:
            return self.operation_1(values)
        elif type_id == 0:
            return self.operation_0(values)
        elif type_id == 0:
            return self.operation_0(values)
        elif type_id == 0:
            return self.operation_0(values)
        elif type_id == 0:
            return self.operation_0(values)

        return eval('self.operation_'+str(type_id))(values)

    def operation_0(self, values):
        return sum([self.do_operation(*v) for v in values])

    def operation_1(self, values):
        res = 1
        for v in values:
            res *= self.do_operation(*v)
        return res

    def operation_2(self, values):
        return min([self.do_operation(*v) for v in values])

    def operation_3(self, values):
        return max([self.do_operation(*v) for v in values])

    @staticmethod
    def operation_4(values):
        return values

    def operation_5(self, values):
        return int(self.do_operation(*values[0]) > self.do_operation(*values[1]))

    def operation_6(self, values):
        return int(self.do_operation(*values[0]) < self.do_operation(*values[1]))

    def operation_7(self, values):
        return int(self.do_operation(*values[0]) == self.do_operation(*values[1]))


bits = BITS(code)
print(f'Part 1: {bits.version_sum}')
print(f'Part 2: {bits.answer}')






