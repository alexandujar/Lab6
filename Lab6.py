# Alex Andujar

def encode(password):
    encoded = ''
    for digit in password:
        encoded_dig = str((int(digit) + 3) % 10)
        encoded += encoded_dig
    return encoded


def decode(encoded):
    # decoded code
    pass



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