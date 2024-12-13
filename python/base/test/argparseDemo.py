import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="这是一个示例脚本")

# 添加参数
parser.add_argument("name", type=str, help="输入你的名字")
parser.add_argument("age", type=int, help="输入你的年龄")

# 解析命令行参数
args = parser.parse_args()

# 使用参数
print(f"你好，{args.name}！你已经 {args.age} 岁了。")

# python argparseDemo.py Alice 25

parser = argparse.ArgumentParser(description="演示可选参数")

# 添加可选参数
parser.add_argument("-v", "--verbose", action="store_true", help="开启详细模式")
parser.add_argument("-n", "--number", type=int, default=1, help="指定一个数字，默认为 1")

args = parser.parse_args()

if args.verbose:
    print("详细模式已开启")

print(f"你指定的数字是 {args.number}")