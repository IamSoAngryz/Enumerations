"""
Treating exceptions locally vs delegating them
(Tratarea exceptiilor local, in sectiunea de program unde sunt ridicate sau
delegarea lor - tratarea intr-o alta sectiune de program decat cea in care
sunt ridicate)
"""

# tratare exceptii / erori local
# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError as e:
#         return e
#         # return 'Diviziune la zero'

# if __name__ == '__main__':
#     print(divide(4, 5))
#     print(divide(5, 0))

def divide(x, y):
    return x / y

def main():
    try:
        print(divide(4, 5))
        # print(divide(5, 0))
        value = input()
        print(devide("4", 3))
    except ZeroDivisionError as e:
        print(f'{e.__class__.__name__}: {e}')
    except TypeError as e:
        print(f'{e.__class__.__name__}: {e}')
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        # eprint(f'{e.__traceback__}')
    except KeyboardInterrupt as e:
        print(f'{e.__class__.__name__}: {e}')


if __name__ == '__main__':
    main()