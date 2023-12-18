

# def countAndSay(n):
#     if n == 1:
#         return "1"
    
#     prev = countAndSay(n - 1)  # 遞迴生成前一項的報數序列
#     print(prev)
#     result = ""
    
#     count = 1
#     for i in range(len(prev)):
#         # 計算連續相同數字的個數
#         if i + 1 < len(prev) and prev[i] == prev[i + 1]:
#             count += 1
#         else:
#             result += str(count) + prev[i]
#             count = 1
    
#     return result

# n = 6
# print(countAndSay(n))  # 輸出: "111221"

###################################迭代

def countAndSay(n):
    if n == 1:
        return "1"
    
    result = "1"  # 初始項
    for _ in range(n - 1):  # 生成第 n 項需要遍歷 n - 1 次
        # print(_)
        temp = ""
        count = 1
        print("a")
        # print(result)
        for i in range(1, len(result)):
            print("i=",i)
            # print(result,result[i],result[i - 1])
            if result[i] == result[i - 1]:
                print("count+1")
                count += 1
            else:
                print("else")
                temp += str(count) + result[i - 1]
                count = 1
        temp += str(count) + result[-1]
        print(temp)
        result = temp
        
    
    return result

n = 5
print(countAndSay(n))  # 輸出: "111221"
