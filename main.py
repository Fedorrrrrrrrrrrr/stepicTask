# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import step16
import MptsSeleniumTests.sign_in

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    import math
    fun = lambda x: 1 if x == 1 else math.ceil(math.sinh(fun(x - 1)))
    print("test: ")
    print(fun(5))
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    step16.step_task()


    # test = MptsSeleniumTests.sign_in.SignInTest("https://dev-mpts.i-core.ru/app/#/auth/login")
    # test.run_tests("fedorqa", "mptsQA", "bad", "bad")
    #MptsSeleniumTests.sign_in.sign_in_test("https://dev-mpts.i-core.ru/app/#/auth/login", "fedorqa", "mptsQA")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
