import __init__ as thread


def pubKeysInDict(_obj=thread.args):
    """
    This reads in objects and prints them as key / value pairs
    You can use them like this print(thread.args.device)
    :param _obj:
    """
    _dict = vars(_obj)
    for each in _dict:
        print(each, _dict[each])


if __name__ == '__main__':
    """
    I like to keep argparse in the __init__ file for readablity
    It lets you pass values into your script like this
    Useage: python main.py --device randomname --package randompackage --tests randomtests
    Items that you don't give it a value for, will use the defaults I set in __init__!
    Main will than print them out as key / value for you to see how you can use them
    """
    print("-----These are the values now availble to you in furthur code!")
    pubKeysInDict(thread.args)
    print("------------ Finish main")
