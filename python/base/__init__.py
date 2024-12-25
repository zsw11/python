# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#  print(player.title())
#
# print(9/2)  #4.5
# print(9//2)  # 4 向下取整
#
#
# """确定列表不是空的
#     ddd
# """
# requested_toppings = []
# if requested_toppings:
#  for requested_topping in requested_toppings:
#   print(requested_topping)
# else:
#  print("空的列表")
#
#  responses = {}
# # 设置一个标志，指出调查是否继续
#  polling_active = True
#  while polling_active:
#   name = input("\nWhat's your name?")
#   response = input("Which mountain would you like to climb someday?")
# # 将答案存储在字典中
#   responses[name] = response
# # 看看是否还有人要参与调查
#   repeat = input("Would you like to let another personrespond?(yes / no)")
#   if repeat == 'no':
#    polling_active = False
# # 调查结束，显示结果
#  print("\n--- Poll Results ---")
#  for name, response in responses.items():
#   print(name + " would like to climb " + response + ".")
