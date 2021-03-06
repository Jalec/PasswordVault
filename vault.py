import pyfiglet
#import click

result = pyfiglet.figlet_format("Password Vault")
print(result)

# ---- DISPLAY MENU ----
def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('Q. Exit')
    print('-'*30)
    return input(': ')

if __name__ == '__main__':
    menu()