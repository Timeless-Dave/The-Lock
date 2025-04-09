import time
from colorama import init, Fore, Style
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
    ╔══════════════════════════════════╗
    ║          THE LOCK v1.0           ║
    ║  Simple Encryption/Decryption    ║
    ╚══════════════════════════════════╝
    """
    print(Fore.CYAN + banner + Style.RESET_ALL)

def the_lock():  # Changed function name
    init()  # Initialize colorama
    clear_screen()
    print_banner()
    
    # create keys string with more special characters
    keys = 'abcdefghijklmnopqrstuvwxyz ,.!?-_\'\"@#$%^&*()'
    values = keys[-1] + keys[0:-1]
    
    # create dictionaries
    dict_e = dict(zip(keys, values))
    dict_d = {value:key for key, value in dict_e.items()}
    
    # user input with improved UI
    print(Fore.GREEN + "\n[*] " + Style.RESET_ALL + "Enter your message:")
    msg = input(Fore.WHITE + ">>> " + Style.RESET_ALL)
    
    print(Fore.GREEN + "\n[*] " + Style.RESET_ALL + "Select mode:")
    print("    1. Encode (e)")
    print("    2. Decode (d)")
    mode = input(Fore.WHITE + ">>> " + Style.RESET_ALL)
    
    print(Fore.YELLOW + "\n[*] Processing..." + Style.RESET_ALL)
    time.sleep(1)  # Add a small delay for effect
    
    # process message
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
        operation = "Encoded"
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
        operation = "Decoded"
    
    # display result
    print(Fore.GREEN + f"\n[✓] {operation} Message:" + Style.RESET_ALL)
    print(Fore.CYAN + f">>> {new_msg.capitalize()}" + Style.RESET_ALL)
    
    return new_msg.capitalize()

if __name__ == "__main__":
    while True:
        the_lock()  # Changed function call
        print(Fore.YELLOW + "\n[*] " + Style.RESET_ALL + "Would you like to try again? (y/n)")
        if input(Fore.WHITE + ">>> " + Style.RESET_ALL).lower() != 'y':
            print(Fore.GREEN + "\nThanks for using The Lock!" + Style.RESET_ALL)  # Changed exit message
            break
        clear_screen()