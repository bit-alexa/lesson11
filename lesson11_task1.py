# Files Task 1
def create_file():
    with open('myfile.txt', 'w') as file:
        file.write('Hello world!')


def print_file():
    with open('myfile.txt', 'r') as file:
        print(file.readline())


if __name__ == '__main__':
    create_file()
    print_file()
