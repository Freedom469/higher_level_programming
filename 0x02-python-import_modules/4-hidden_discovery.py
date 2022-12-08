#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        if i.startswith("_"):
=======

if __name__ == "__main__":
    import hidden_4

    for i in dir(hidden_4):
        if i.startswith("__"):
>>>>>>> 5cd30d0f10ed0ee1021d0e5d3fc2351d69baef75
            continue
        print(i)
