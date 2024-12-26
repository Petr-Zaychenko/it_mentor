from task_13 import Monostate
from task_13_mod_2 import two

def one():
    return Monostate().data * 100

if __name__ == '__main__':
    result = one() + two()
    print(result)