class Man:
    def __init__(self):
        self.name = "tsugimot"
        print("Initialized!")

    def hello(self):
        print(f"hello {self.name}")

    def goodbye(self):
        print(f"Goodbye {self.name}")

if __name__ == "__main__":
    man = Man()
    man.hello()
    man.goodbye()
