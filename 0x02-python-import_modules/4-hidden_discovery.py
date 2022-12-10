#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # iterate through dir module
    for name in dir(hidden_4):
        if name[:2] != "__":
            print(name)
