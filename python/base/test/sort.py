def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[len(lst) // 2]  # 选择中间元素作为基准
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


range_ = [x * x for x in range(1, 11)]  # 列表生成
x_ = [x * x for x in range(1, 11) if x % 2 == 0]
xyz_ = [m + n for m in 'ABC' for n in 'XYZ']

# 要创建一个generator（生成器是一种特殊的迭代器，它可以在需要时逐个生成元素，而不是一次性构建整个结果集），有很多种方法。
# 第一种方法（生成器表达式）很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
# 第二种方式（生成器函数） ，生成器函数：通过包含 yield 语句的函数创建
# 生成器特征：
# 迭代器协议：生成器实现了迭代器协议，即它们有 __iter__() 和 __next__() 方法。
# 惰性求值：只有在调用 next() 或使用 for 循环时才会生成下一个元素。
# 一次性使用：一旦生成器被耗尽（即抛出 StopIteration 异常），它不能重新使用，除非重新创建。
g = (x * x for x in range(10))
for n in g:
    print(n)

# yield 是 Python 中用于定义生成器（generator）的关键字。生成器是一种特殊的迭代器，它允许你在函数中逐步返回值，而不需要一次性构建整个结果集
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
print(next(gen))  # 输出: 3


def sieve_of_eratosthenes(limit):
    # 创建一个布尔列表，默认所有数都是素数
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        # 如果 is_prime[p] 未被改变，那么它是一个素数
        if is_prime[p]:
            # 更新所有 p 的倍数为非素数
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    # 使用 filter 和 lambda 表达式筛选出素数
    primes = list(filter(lambda x: is_prime[x], range(2, limit + 1)))
    return primes
# 示例用法
limit = 50
print(f"小于等于 {limit} 的素数有: {sieve_of_eratosthenes(limit)}")

# 费波拉且数列
def fib(max):
    n, a, b, = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(6)

# 闭包
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

l = count()    # f()方法还未调用
print(l)    #把创建的3个函数都返回了。
for f in l:
    print(f())  # 每次循环启动f()方法 ,结果 9 9 9


def find_min_max_by_quick_sort(lst):
    if not lst:  # 检查列表是否为空
        return None  # 或者根据需求返回其他默认值或抛出异常

    sorted_lst = quick_sort(lst)  # 使用快速排序对列表进行排序

    print(sorted_lst)
    min_val = sorted_lst[0]  # 排序后的第一个元素是最小值
    max_val = sorted_lst[-1]  # 排序后的最后一个元素是最大值

    return (min_val, max_val)

# 示例用法
example_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = find_min_max_by_quick_sort(example_list)
print("最小值和最大值分别是:", result)  # 输出：最小值和最大值分别是: (1, 9)