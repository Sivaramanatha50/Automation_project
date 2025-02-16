#url = ["https://indeedemo-fyc.watch.indee.tv/login"]
#
# def fibnacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibnacci(n-1) + fibnacci(n-2)
# # n = 10
# print(fibnacci(n))
#
# import pytest
# from selenium import webdriver
# @pytest.mark.parametrize("a b",[2,4])
# def test_addition(a,b):
#     print(a + b)
#
# def test_login(url,username,password):
#     driver = webdriver.Chrome()
#     driver.get(url)
#     driver.find_element(By.ID,"username").send_keys("siva")
#     driver.find_element(By.ID,"password").send_keys("sivaram")
#     driver.find_element(By.XPATH,"submit-button").click()

# l = lambda x: x * 2
# print(l(5))

def generator(n):
    for _ in range(n):
        yield n
gen = generator(5)
print(next(gen))
print(next(gen))
print(next(gen))