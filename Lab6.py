# Alex Andujar

def encode(password):
    # adds 3 to each digit, while taking modulo 10 to keep within single digits
    encoded = ''
    for digit in password:
        encoded += str((int(digit) + 3) % 10)
    return encoded


def decode(encoded):
    #KM added in decode function
    decoded = ''
    for digit in encoded:
        num = int(digit)
        num -= 3
        if num < 0:
            num += 10
        decoded += str(num)
    return decoded



def main():
    encoded = ""
    decoded = ""

    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        option = input('Please enter an option: ')

        if option == "1":
            password = input('Please enter your password to encode: ')
            encoded = encode(password)
            print('Your password has been encoded and stored!')
            print()

        elif option == "2":
            decoded = decode(encoded)
            print(f'The encoded password is {encoded}, and the original password is {decoded}')
            print()

        elif option == "3":
            break

        else:
            print('Invalid option!')
            print()



if __name__ == '__main__':
    main()