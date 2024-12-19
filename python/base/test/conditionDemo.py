import random
import threading
import time

condition = threading.Condition()
buffer = []

# 生产者
def producer():
    while True:
        item = random.randint(1, 100)
        with condition: # 获取锁
            while len(buffer) >= 5: # 如果缓冲区满了，等待消费者消费
                print("生产者等待。。。。缓冲区已满")
                condition.wait() # 进入等待状态
            buffer.append(item)
            print(f"生产者生产了物品：{item}，当前缓冲区：{buffer}")
            condition.notify_all() # 唤醒消费者线程
        time.sleep(random.randint(1,3)) # 模拟生产延迟

def consumer():
   while True:
       with condition:
           while not buffer:
               print("消费者等待。。。缓冲区为空")
               condition.wait()  # 进入等待状态，等待生产者生产
           item = buffer.pop(0) # 从缓冲区消费一个物品
           print(f"消费者消费了物品: {item}，当前缓冲区: {buffer}")
           condition.notify_all()  # 唤醒生产者线程
       time.sleep(random.randint(1,3))

# 创建线程
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# 启动线程
producer_thread.start()
consumer_thread.start()

# 等待线程结束
producer_thread.join()
consumer_thread.join()

