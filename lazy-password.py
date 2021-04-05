
CONST = 76543210

from getpass import getpass
from time import sleep
from hashlib import sha256

# Help functions
def valid_time(time):
    try:
        time = int(time)
    except:
        return False
    if time <= 0:
        return False
    return True

if __name__ == "__main__":

    pw1 = getpass(prompt="Password: ", stream=None)
    pw2 = getpass(prompt="Password(repeat): ", stream=None)
    while pw1!=pw2:
        print("\nPassword missmatch. Please type again!")
        pw1 = getpass(prompt="Password: ", stream=None)
        pw2 = getpass(prompt="Password(repeat): ", stream=None)

    print('Minutes to wait: ', end='')
    t = input()
    while not valid_time(t):
        print("Time ist not valid. Please type again!")
        print('Minutes to wait: ', end='')
        t = input()
    t = int(t)

    for i in range(60*t-1, -1, -1):
        sleep(1)
        print("Time to wait: " + str(int(i/60)).zfill(2) + ":" + str(i%60).zfill(2) + "\r", end = "")

    pw_bytes = pw1.encode()
    time_bytes = t.to_bytes(4, "little")
    const_bytes = CONST.to_bytes(4, "little")

    lazy_pw = sha256(pw_bytes+time_bytes+const_bytes)
    print("\nLazy Password:\n")
    print(lazy_pw.hexdigest())
    print()

    user_input = None
    while user_input != "exit":
        print("You can close the programm with 'exit'")
        user_input = input()
