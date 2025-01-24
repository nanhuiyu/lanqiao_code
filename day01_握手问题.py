# 计算组合数 C(n, 2)，即从 50 人中任意选择 2 人进行握手
def comb(n):
    """计算组合数 C(n, 2)"""
    return n * (n - 1) // 2

# 计算总握手次数
def calculate_handshakes(total_people, excluded_people):
    total_handshakes = comb(total_people)  # 总人数之间的握手数
    excluded_handshakes = comb(excluded_people)  # 排除的7人之间的握手数
    return total_handshakes - excluded_handshakes

# 参数设置
total_people = 50
excluded_people = 7

# 计算结果
result = calculate_handshakes(total_people, excluded_people)
print(result)
