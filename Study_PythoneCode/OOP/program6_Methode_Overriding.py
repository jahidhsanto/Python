class Phone:
    def __init__(self):
        print("I am in Phone class")


class Samsung(Phone):
    # __init__
    def __init__(self):
        super().__init__()
        print("I am in Samsung class")


s = Samsung()
