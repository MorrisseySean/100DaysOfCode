# FileNotFound & KeyError

try:
    file = open('a_file.txt')
    a_dict = {'key':'value'}
    print(a_dict['daefoidsjf'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('Something')
except KeyError as error_message:
    print(f"The key {error_message} does not exist!")
else:
    content = file.read()
    print(content)
finally:
    file.close()