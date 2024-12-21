import random

class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
    
    def value(self, state):
        # Hàm đánh giá giá trị của trạng thái (càng lớn càng tốt)
        return -state**2 + 4*state + 10  # Ví dụ: hàm bậc hai
    
    def get_neighbors(self, state):
        # Trả về các trạng thái lân cận
        step_size = 1
        return [state - step_size, state + step_size]

def hill_climbing(problem, start_state):
    current_state = start_state
    while True:
        neighbors = problem.get_neighbors(current_state)
        next_state = max(neighbors, key=problem.value)
        if problem.value(next_state) <= problem.value(current_state):
            return current_state
        current_state = next_state

# Yêu cầu đầu vào từ người dùng
try:
    initial_state = int(input("Nhập trạng thái ban đầu (số nguyên): "))
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
    exit()

# Tạo đối tượng bài toán
problem = Problem(initial_state)

# Thực hiện tìm kiếm leo đồi
solution = hill_climbing(problem, initial_state)

# In kết quả
print(f"Trạng thái bắt đầu: {initial_state}")
print(f"Giải pháp tìm thấy: {solution}")
print(f"Giá trị của giải pháp: {problem.value(solution)}")