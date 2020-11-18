def fnc():
    x = 1
    raise Exception("Exceptia mea")

try:
    fnc()
    x = 10
    print("Try")


except Exception as err:
    raise err

finally:
    print("orice ar fi")