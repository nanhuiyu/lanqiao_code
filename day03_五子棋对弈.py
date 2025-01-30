board_size = 5
draw_count = 0

# 统计数组，分别记录行、列、主对角线、副对角线的棋子数
row_count = [0] * (board_size + 1)
col_count = [0] * (board_size + 1)
main_diag_count = [0] * (2 * board_size + 1)
anti_diag_count = [0] * (2 * board_size + 1)

def count_draw_games(position, white_pieces, black_pieces):
    global draw_count

    if position == board_size * board_size + 1:
        draw_count += 1
        return

    x = (position - 1) // board_size + 1
    y = (position - 1) % board_size + 1

    # 尝试放置白棋
    if (white_pieces > 0 and row_count[x] < board_size - 1 and col_count[y] < board_size - 1 and 
        main_diag_count[x + y] < board_size - 1 and anti_diag_count[x - y + board_size] < board_size - 1):

        row_count[x] += 1
        col_count[y] += 1
        main_diag_count[x + y] += 1
        anti_diag_count[x - y + board_size] += 1

        count_draw_games(position + 1, white_pieces - 1, black_pieces)

        row_count[x] -= 1
        col_count[y] -= 1
        main_diag_count[x + y] -= 1
        anti_diag_count[x - y + board_size] -= 1

    # 尝试放置黑棋
    if (black_pieces > 0 and row_count[x] > 1 - board_size and col_count[y] > 1 - board_size and 
        main_diag_count[x + y] > 1 - board_size and anti_diag_count[x - y + board_size] > 1 - board_size):

        row_count[x] -= 1
        col_count[y] -= 1
        main_diag_count[x + y] -= 1
        anti_diag_count[x - y + board_size] -= 1

        count_draw_games(position + 1, white_pieces, black_pieces - 1)

        row_count[x] += 1
        col_count[y] += 1
        main_diag_count[x + y] += 1
        anti_diag_count[x - y + board_size] += 1

# 计算所有可能的平局棋局数
count_draw_games(1, (board_size * board_size + 1) // 2, board_size * board_size // 2)

print(draw_count)

# def generate_permutations(elements):
#     """
#     递归生成列表元素的全排列（手工实现 permutations 生成器）
    
#     参数：
#         elements: list，需要生成排列的元素列表
    
#     Yields：
#         list: 一个排列组合
#     """
#     # 基本情况：空列表只有一种排列（空列表）
#     if len(elements) == 0:
#         yield []
#     else:
#         # 遍历每个元素作为排列的第一个元素
#         for i in range(len(elements)):
#             # 排除当前元素后的剩余元素列表
#             rest = elements[:i] + elements[i+1:]
#             # 递归生成剩余元素的所有排列
#             for p in generate_permutations(rest):
#                 # 将当前元素与子排列组合
#                 yield [elements[i]] + p

# def check_five_in_a_row(board):
#     """
#     检查五子棋棋盘是否存在五连珠情况
    
#     参数：
#         board: list[list[int]]，5x5的二维数组，0表示空，1/2表示玩家
    
#     返回：
#         bool: 是否存在五连珠
#     """
#     def check_line(x, y, dx, dy):
#         """
#         检查从(x,y)出发，沿(dx,dy)方向是否存在五连珠
        
#         参数：
#             x, y: 起始坐标
#             dx, dy: 方向步长（取值应为0或±1）
        
#         返回：
#             bool: 是否五连
#         """
#         color = board[x][y]
#         # 空位置直接返回否
#         if color == 0:
#             return False
#         # 检查连续五个位置
#         for i in range(1, 5):  # 只需要检查后续四个位置（共五个）
#             nx, ny = x + i*dx, y + i*dy
#             # 确保不会越界（根据调用方式其实不需要，但保留更安全）
#             if nx >= 5 or ny >= 5 or nx < 0 or ny < 0:
#                 return False
#             if board[nx][ny] != color:
#                 return False
#         return True
    
#     # 检查所有可能的五连珠路线
#     for i in range(5):
#         # 横向检查（每行的起始位置）
#         if check_line(i, 0, 0, 1):
#             return True
#         # 纵向检查（每列的起始位置）
#         if check_line(0, i, 1, 0):
#             return True
    
#     # 对角线检查
#     return check_line(0, 0, 1, 1) or check_line(0, 4, 1, -1)

# def count_draw_games():
#     """
#     计算所有可能的平局棋局数量（无五连珠的完整棋盘）
    
#     注意：此实现因时间复杂度为O(25!)而无法实际运行，仅作为逻辑演示
    
#     返回：
#         int: 平局数量（理论值）
#     """
#     # 生成所有棋盘位置坐标
#     positions = [(i, j) for i in range(5) for j in range(5)]
#     draw_count = 0
    
#     # 遍历所有可能的落子顺序排列
#     for perm in generate_permutations(positions):
#         # 初始化空棋盘
#         board = [[0] * 5 for _ in range(5)]
        
#         # 模拟落子过程
#         for turn, (x, y) in enumerate(perm):
#             # 交替玩家落子（玩家1先手）
#             board[x][y] = 1 if turn % 2 == 0 else 2
#             # 每次落子后立即检查五连珠
#             if check_five_in_a_row(board):
#                 break  # 出现五连则终止当前棋局
#         else:
#             # 完整25步且无五连珠的情况计数
#             draw_count += 1
    
#     return draw_count

# # 注意：实际运行时本代码无法完成计算
# print(count_draw_games())