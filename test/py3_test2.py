# encoding=utf-8
def oo():
    try:
        1/0
    except Exception as e:
        print(e.args)
        print(1)

    try:
        3/0
    except Exception as e:
        print(e.args)
        print(3)


oo()