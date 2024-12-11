# Numpy是 Python 中一个功能强大的科学计算库，主要用于处理多维数组（ndarray）以及执行高效的数值计算
import numpy as np

# 创建一维数组
arr1 = np.array([1, 2, 3])

# 创建二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# 创建全零数组
zeros = np.zeros((2, 3))

# 创建全一数组
ones = np.ones((2, 3))

# 创建指定范围的数组
arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# 创建随机数组
random_arr = np.random.rand(2, 3)

print(arr2.shape)  # (2, 3) - 数组形状
print(arr2.ndim)   # 2 - 数组维度
print(arr2.size)   # 6 - 元素总数
print(arr2.dtype)  # int32 - 数据类型

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 数组加法
print(a + b)  # [5, 7, 9]

# 数组减法
print(a - b)  # [-3, -3, -3]

# 数组乘法（逐元素）
print(a * b)  # [4, 10, 18]

# 数组点乘
print(np.dot(a, b))  # 32

# 数组广播
print(a + 10)  # [11, 12, 13]

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 获取特定元素
print(arr[0,1])  # 2

# 切片操作
print(arr[:, 1])  # 第二列 [2, 5, 8]
print(arr[1, :])  # 第二行 [4, 5, 6]

# 布尔索引
print(arr[arr > 5])  # [6, 7, 8, 9]

# 重塑数组
reshaped = arr.reshape((1, 9))

# 扁平化
flattened = arr.ravel()

# 转置
transposed = arr.T

# 数学操作
print(np.sum(arr))  # 元素总和
print(np.mean(arr)) # 平均值
print(np.max(arr))  # 最大值
print(np.min(arr))  # 最小值

# 排序
sorted_arr = np.sort(arr)

# 数学函数
print(np.sin(arr))
print(np.log(arr))

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 逐元素乘法
# 输出：
# [[ 5 12]
#  [21 32]]
result = a * b
print(a)
print(b)
# 如果 a 的形状是 (m, n)，b 的形状必须是 (n, p)，结果是形状 (m, p) 的矩阵。
dot = np.dot(a, b)
print(dot)




