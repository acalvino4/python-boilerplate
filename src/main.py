from distutils.sysconfig import get_python_lib


def add_nums(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(get_python_lib())

    print("sum:")
    print(add_nums(5, 4))
