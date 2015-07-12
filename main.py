__author__ = 'Emanuel'

import mraa
import time

# Set port numbers
bt_Up = mraa.Gpio(13)
bt_Down = mraa.Gpio(13)
bt_Left = mraa.Gpio(13)
bt_Right = mraa.Gpio(13)
bt_Enter = mraa.Gpio(13)

# Set port direction
bt_Up.dir(mraa.DIR_IN)
bt_Down.dir(mraa.DIR_IN)
bt_Left.dir(mraa.DIR_IN)
bt_Right.dir(mraa.DIR_IN)
bt_Enter.dir(mraa.DIR_IN)


def showMenu():
    print()


def main():
    while True:
        print("Select a option:")


if __name__ == '__main__':
    main()
