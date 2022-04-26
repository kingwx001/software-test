# #!/usr/bin/env python
# 2.输出0-2021之间所有闰年（闰年是4的倍数但不是100的倍数或者是400的倍数） 

# 3.求1-2+3-4+5...99表达式执行的结果


# sum = 0
# for i in range(1,100):
#     if i % 2 == 0:
#         i = -i  
#     sum += i


# 4.在1-100中，随机获取10个唯一值，并添加到一个列表中。

# import random

# lis = []
# while a< 10:
#     r = random.randint(1,100)
#     if r in lis:
#         continue
#     else:
#         lis.append(r)

# 5.定义一个列表list = [2,1,4,9,5,7]，使用循环语句将列表反转。

# l,r = 0,len(list) - 1
# while l < r:
#     list[l],list[r] = list[r],list[l]
#     l += 1
#     r -= 1

# for i in range(len(list) - 1,-1,-1):
#     newList.append(list[i])



# 6.定义一个列表list = [2,1,4,9,5,7]  使用冒泡排序算法将列表进行升序排序，并封装成函数。
# for i in range(0,n):
#     for j in range(0,n - i - 1):
#         if list[j] > list[j + 1]:
#             list[j],list[j + 1] = list[j + 1],list[j]