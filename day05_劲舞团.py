def calculate_longest_k_combo(log_file_path):
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    # 初始化变量
    longest_k = 0
    current_k = 0
    last_timestamp = None

    # 遍历日志记录
    for log in logs:
        correct_char, typed_char, timestamp = log.strip().split()
        timestamp = int(timestamp)

        # 检查是否正确敲击并且时间间隔是否小于等于1秒
        if correct_char == typed_char:
            if last_timestamp is None or (timestamp - last_timestamp) <= 1000: # 见文章中的解析
                current_k += 1
            else:
                current_k = 1
        else:
            current_k = 0

        # 更新最长连击
        if current_k > longest_k:
            longest_k = current_k

        # 更新最后的时间戳
        last_timestamp = timestamp

    return longest_k

# 假设log.txt文件位于当前目录
log_file_path = 'log.txt'
print(calculate_longest_k_combo(log_file_path))
