import random, string, sys, time
while True:
    user_input = (int(input('\n' + 'Password length: ')))
    for user_input in range(int(user_input)):
        sys.stdout.write(random.choice(random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits)))
