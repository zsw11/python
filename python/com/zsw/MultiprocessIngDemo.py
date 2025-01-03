import multiprocessing
import time

# 任务函数
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

if __name__ == "__main__":
    # 创建进程    multiprocessing.Process 用来创建进程。
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # 启动进程
    process1.start()
    process2.start()

    # 等待进程完成
    process1.join()
    process2.join()

    print("所有进程完成")
