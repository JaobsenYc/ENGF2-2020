import sys


class parity(object):
    def check(self, num):
        if (num & 1) == 0:  # check the last bit of the binary
            return True
        else:
            return False


class Selections(object):

    def check(self):
        num = int(input("Input the value to check: "))
        print('{} is even'.format(num) if parity.check(num)==True else "{} is odd".format(num))


class Menu(object):
    def __init__(self):
        self.selection = Selections()
        self.menuChoices = {
            "1": self.selection.check,
            "2": self.quit,
        }

    def display_menu(self):
        print("""
        -----------------Chen Yang Parity Check-----------------
        Operation Menu:
        1. Check number
        2. Quit
        ---------------------------------------------------
        """)

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = input("Enter an option: ")
            except BaseException:
                print("Please input a valid option!");
                continue

            choice = str(choice).strip()
            action = self.menuChoices.get(choice)

            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def quit(self):
        print("\nThank you for using Chen Yang Parity Check!\n")
        sys.exit(0)


if __name__ == '__main__':
    parity = parity()
    Menu().run()
