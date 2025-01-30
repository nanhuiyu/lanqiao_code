def is_good_number(num):
    # 将数字转换为字符串，便于逐位处理
    num_str = str(num)
    length = len(num_str)
    
    for i, digit in enumerate(num_str): # 使用enumerate提取每一位数字及其对应的下标
        digit = int(digit)
        # 奇数位检查（从右到左，1到based）：位索引 i 从 0 开始，因此 (length - i) 是 1到based 的位数
        if (length - i) % 2 == 1:  # 奇数位
            if digit % 2 == 0:  # 奇数位上的数字必须是奇数
                return False
        else:  # 偶数位
            if digit % 2 != 0:  # 偶数位上的数字必须是偶数
                return False
    return True # 没有提前跳出函数，说明该数字符合要求


def count_good_numbers(N):
    count = 0 # 初始计数器为0
    for num in range(1, N + 1): # 遍历范围内所有的数
        if is_good_number(num): # 符合“好数”条件
            count += 1
    return count


# 输入处理
if __name__ == "__main__":
    N = int(input().strip())
    print(count_good_numbers(N))