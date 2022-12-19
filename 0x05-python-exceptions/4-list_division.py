#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for elem in range(0, list_length):
        try:
            new_list.append(my_list_1[elem] / my_list_2[elem])
        except ZeroDivisionError:
            new_list.append(0)
            print('division by 0')
        except TypeError:
            new_list.append(0)
            print('wrong type')
        except LookupError:
            new_list.append(0)
            print('out of range')
        finally:
            pass

    return new_list
