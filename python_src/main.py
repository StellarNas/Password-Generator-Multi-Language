import os
from pathlib import Path
import logging
import random

logging.basicConfig(format='[%(asctime)s] (%(levelname)s) %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger()

debug_mode = True

if debug_mode:
    logger.setLevel(logging.DEBUG)
    logger.debug("Debug mode enabled")


chars_strs = {
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "lowercase": "abcdefghijklmnopqrstuvwxyz",
    "numbers": "0123456789",
    "symbols": "!@#$%^&*-"
}

initial_options = {
    '1': "Basic",
    '2': 'Advanced (Not finished)',
    '0': 'Exit'
}

def input_to_exit():
    input("\nPress enter to exit program")
    os._exit(0)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pt():
    print("\n[ CLI Password Generator Written in python ]\n")

def gen_random_pw(chars_to_use, amount):
   return "".join(random.choices(chars_strs[chars_to_use], k=amount))

def basic_pass_gen():
    clear_screen()
    pt()
    print("( Basic password generator )\n")
    
    pw_length = int(input("Password length (ex: 12) >> "))
    bpw_chars = {
        "uppercase": input("Use Uppercase? [A-Z] (Y/N) >> ").lower(),
        "lowercase": input("Use Lowercase? [a-z] (Y/N) >> ").lower(),
        "numbers": input("Use Numbers? [0-9] (Y/N) >> ").lower(),
        "symbols": input(f"Use Symbols? [{chars_strs["symbols"]}] (Y/N) >> ").lower()
    }

    chars_to_use = []
    
    amounts_test = {
        "uppercase": 0,
        "lowercase": 0,
        "numbers": 0,
        "symbols": 0
    }
    

    for char_type, answer in bpw_chars.items():
        
        if not answer == 'y' and not answer == 'n':
            logger.error("Invalid input")
            input_to_exit()
        if answer == 'y':
            for k, v in amounts_test.items():
                if v == 0:
                    amounts_test[k] += 1

            chars_to_use.append(char_type)

    print(f"\nGenerating...\n")

    for i in range(1, pw_length - sum(v for k, v in amounts_test.items()) + 1):
        amounts_test[random.choice(list(amounts_test.keys()))] += 1

    pw_list = []

    for char, amount in amounts_test.items():
        chars_random = gen_random_pw(char , amount)
        for i in chars_random:
            pw_list.append(i)
        print(f"{char.capitalize()} characters to generate: {amount}")

    print(f"\nTotal: {sum(v for k, v in amounts_test.items())}")
    
    random.shuffle(pw_list)
    print(f"Generated password: {''.join(pw_list)}")


def main():
    pt()

    for num, option in initial_options.items():
        print(f"[{num}] {option}")

    userinput = int(input(" >> "))

    if userinput == 0:
        input_to_exit()

    elif userinput == 1:
        basic_pass_gen()

    elif userinput == 2:
        print("Not finished")
    
    else:
        logger.error("Invalid input")
    input_to_exit()

main()

