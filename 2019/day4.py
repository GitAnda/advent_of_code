def is_valid_password(number, question_number):
    import regex
    reg = r'(?=^\d{6}$)(?=.*(\d)\1{1,})^1*2*3*4*5*6*7*8*9*$' if question_number == 1 else r'(?=^\d{6}$)(?=.*(\d)(?!\1)(\d)\2(?!\2)|^(\d)\3(?!\3))^1*2*3*4*5*6*7*8*9*$'
    return bool(regex.search(reg, str(number)))


def find_valid_passwords(password_candidates, question_number):
    return [candidate for candidate in password_candidates if is_valid_password(candidate, question_number)]

if __name__ == '__main__':
    import sys

    candidates = range(136760, 595730+1)

    print('Exercise 3.1')
    valid_passwords = find_valid_passwords(candidates, 1)
    print(len(valid_passwords), 'passwords within the range match the criteria')

    print('\nExercise 3.2')
    valid_passwords = find_valid_passwords(candidates, 2)
    print(len(valid_passwords), 'passwords within the range match the criteria')

