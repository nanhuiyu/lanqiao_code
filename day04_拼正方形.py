def max_square_side():
    max_two_by_two = 7385137888721  # 2×2 方块数量
    max_one_by_one = 10470245       # 1×1 方块数量

    # 设定合理的二分查找范围
    left, right = 1, int((max_two_by_two * 4 + max_one_by_one) ** 0.5)

    while left < right:
        mid = (left + right + 1) // 2  # 取上中位数，防止死循环
        total_area = mid * mid  # 需要填充的总面积

        # 计算最多能使用的 2×2 方块数量
        max_used_two_by_two = min(max_two_by_two, total_area // 4)
        remaining_area = total_area - max_used_two_by_two * 4  # 需要补充的 1×1 方块面积

        if remaining_area < max_one_by_one:
            left = mid  # 继续尝试更大的 n
        elif remaining_area == max_one_by_one:
            return left
        else:
            right = mid - 1  # n 太大了，尝试更小的 n

    return left  # 返回最大合法的 n

print(max_square_side())  # 输出最大边长
