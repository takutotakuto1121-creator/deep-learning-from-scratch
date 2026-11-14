from src.ch01 import Man, hungry

def main():
    print("== Ch01: basics of python ==")
    print("= hungry.py =")
    hungry()
    print()

    print("= man.py =")
    man = Man()
    man.hello()
    man.goodbye()


if __name__ == "__main__":
    main()
    