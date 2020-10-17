# PROJECT 2: Multi-Agent Search

## Question 1: Reflex Agent
Viết lại hàm `evaluationFunction` để có được hàm đánh giá tốt hơn.
Đánh giá theo 
- Khoảng cách manhattan giữa Pacman và con ma gần nhất : Khoảng cách càng xa càng tốt.
- Khoảng cách manhattan giữa Pacman và điểm thức ăn gần nhất: Khoảng cách càng gần càng tốt.

>python pacman.py --frameTime 0 -p ReflexAgent -k 2 

>python autograder.py -q q1


## Question 2: Minimax

- Cài đặt thuật toán Minimax, xác định hành động cho pacman.
- Cây Minimax sẽ có nhiều lớp min tương ứng với 1 lớp max 
> python autograder.py -q q2
## Question 3: Alpha-Beta Pruning
- tương tự câu 2
- Sử dụng thêm 2 biến `alpha`, `beta` để cắt một số nhánh không cần thiết trên cây minimax
> python autograder.py -q q3
## Question 4: Expectimax
- Tương tự câu 2.
- hàm minimize() trả về giá trị minimax trung bình trong các trạng thái kế tiếp.
> python autograder.py -q q4
## Question 5: Evaluation Function
- Đánh giá dựa trên khoảng cách đến thức ăn gần nhất, khoảng cách với ma, sô thức ăn.
> python autograder.py -q q5