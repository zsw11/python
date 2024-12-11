# main.py

# 导入整个模块
import python.com.module.module as mymodule

# 调用模块中的函数
mymodule.greet("Alice")
result = mymodule.add(3, 5)
print(f"3 + 5 = {result}")

# 从模块中导入特定的函数
from python.com.module.module import multiply

# 调用导入的函数
product = multiply(4, 6)
print(f"4 * 6 = {product}")

# 从模块中导入所有函数（不推荐，容易引起命名冲突）
from module import *

# 调用导入的函数
greet("Bob")
result = add(7, 8)
print(f"7 + 8 = {result}")

def print_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()  # 换行

# 打印前 10 个斐波拉契数
print_fibonacci(10)

# 动态规划（Dynamic Programming，简称 DP）是一种解决复杂问题的方法，通过将问题分解为更小的子问题，并保存这些子问题的解，从而避免重复计算。
# 动态规划的核心思想是“记忆化”（Memoization）或“表格化”（Tabulation），通过存储已经计算过的结果来优化计算过程。
def print_fibonacci_dp(n):
    if n <= 0:
        return
    fib = [0] * n
    fib[0] = 0
    if n > 1:
        fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    for num in fib:
        print(num, end=' ')
    print()  # 换行

# 打印前 10 个斐波拉契数
print_fibonacci_dp(10)

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# 测试
print(fibonacci_memo(10))  # 输出: 55