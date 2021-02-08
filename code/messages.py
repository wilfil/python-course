count = 1
message = input("Type your greeting message: ")
count = int(input("how many times to repeat? ").strip())

def multi_echo(message, count):
    i = 1
    while i <= count:
        print(message)
        i += 1

multi_echo(message, count)
