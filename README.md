# Trí tuệ nhân tạo INT3401 8


## Bài tập 1: Pacman Search

### Câu hỏi 1: Finding a Fixed Food Dot using Depth First Search
#### Cách làm:
- Từ vị trí xuất phát, đi tới ô liền kề của nó mà chưa được thăm, lưu lại tọa độ của các ô đã này. Tiếp tục lấy ô mới nhất vừa được thăm, đi tiếp. Trong quá trình duyệt, nếu không thấy ô liền kề, chưa được thăm thì quay lại ô trước nó. Thuật toán dừng lại khi không còn ô chưa được thăm hoặc tới được đích. 
- Sử dụng stack để cài đặt thuật toán, các phần tử được thêm vào sau sẽ được lấy ra trước, các ô có chung một ô liền trước sẽ được lưu cạnh nhau trong stack, phải duyệt xong một nhánh rồi mới quay lại duyệt tiếp nhánh khác 
#### Cài đặt:
- **visited**: dùng để lưu vị trí các ô đã thăm
- **stack**: dùng để lưu vị trí, các hành động để mở rộng ra các ô tiếp theo
- **state**: dùng để lưu vị trí của ô hiện tại
- **actions**: danh sách các hành động để đi từ vị trí xuất phát đến ô hiện tại
- **successor**: vị trí của ô tỉếp theo có thể mở rộng
- **action**: hành động để đi từ ô hiện tại tới ô tiếp theo
- **cost**: chi phi cần cho việc đi từ ô hiện tại tới ô tiếp theo *( trong bài này không dùng đến )*
#### Chạy chương trình:     
- Đẩy vào stack vị trí xuất phát, và danh sách các hành động ( lúc này còn rỗng )
- Chạy vòng lặp cho đến khi không còn phần tử nào trong stack hoặc tìm được đích. 
    - Lấy vị trí, và danh sách các hành động ra khỏi stack 
        - Kiểm tra, nếu vị trí vừa lấy đã được thăm thì lấy phần tử tiếp theo ra khỏi stack, bỏ qua phần tử hiện tại, nếu chưa thăm thì thêm vào danh sách **visited**
        - Dùng hàm **isGoalState()** Kiểm tra, nếu vị trí vừa lấy là vị trí đích thì trả về danh sách các hành động để đi từ vị trí xuất phát đến đích, kết thúc vòng lặp
    - Dùng hàm **getSuccessors()** để lấy ra danh sách các ô có thể mở rộng tiếp theo 
        - Kiểm tra, đẩy vị trí và danh sách các hành động (từ vị trí xuất phát đến vị trí tiếp theo) vào stack nếu ô chưa được thăm
- Kết quả trả về là danh sách các hành động để đạt được trạng thái đích, trả về danh sách rỗng nếu không tìm được.
    > python pacman.py -l tinyMaze -p SearchAgent<br>
    > python pacman.py -l mediumMaze -p SearchAgent<br>
    > python pacman.py -l bigMaze -z .5 -p SearchAgent<br>
### Câu hỏi 2: Breadth First Search
#### Cách làm:
- Từ vị trí xuất phát, đi tới tất cả các ô liền kề nó mà chưa được thăm, lưu lại tọa độ của các ô này. Sau khi thăm hết các đỉnh liền kề này, tiếp tục thăm các ô liền kề của các ô vừa được thăm, tiếp tục cho đến khi không còn đỉnh nào chưa được thăm hoặc đến được đích.
- Sử dụng queue để cài đặt thuật toán, các phần tử được thêm vào trước sẽ được lấy ra trước, các ô có chung một ô liền trước sẽ được cạnh nhau trong queue, phải thăm hết các ô này rồi mới duyệt các ô liền kề các ô này
#### Cài đặt
- Tương tự bài trên
- Sử dụng **queue** thay cho **stack** để lưu vị trí và các hành động để mở rộng ra các ô tiếp theo
#### Chạy chương trình:
- Tương tự bài trên
    > python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5<br>
### Câu hỏi 3: Varying the Cost Function
#### Cách làm: 
- Tìm kiếm đường đi có chi phí ít nhất, từ vị trí xuất phát ban đầu tiếp tục đi tới các ô tiếp theo với chi phí thấp nhất tính từ vị trí ban đầu.
- Sử dụng hàng đợi ưu tiên (priority queue) để cài đặt thuật toán, sẽ lấy ra các phần tử có giá trị bé nhất trong hàng đợi, các phần tử có giá trị bé sẽ bị đẩy lên đầu hàng đợi.
#### Cài đặt:
- **visited**: dùng để lưu vị trí các ô đã thăm
- **queue**: hàng đợi ưu tiên (theo chi phí) dùng để lưu vị trí, các hành động và chi phí để mở rộng ra các ô tiếp theo
- **state**: dùng để lưu vị trí của ô hiện tại
- **actions**: danh sách các hành động để đi từ vị trí xuất phát đến ô hiện tại
- **successor**: vị trí của ô tỉếp theo có thể mở rộng
- **action**: hành động để đi từ ô hiện tại tới ô tiếp theo
- **cost**: chi phi cần cho việc đi từ ô hiện tại tới ô tiếp theo   

#### Chạy chương trình 
- Khởi tạo đẩy vào hàng đợi ưu tiên vị trí xuất phát, danh sách các hành động (lúc này còn rỗng) và chi phí để đến vị trí này là 0
- Chạy vòng lặp cho đến khi không còn phần tử nào trong hàng đợi hoặc tìm được đích
    - Lấy vị trí và danh sách các hành động ra khỏi hàng đợi
        - Kiểm tra, nếu vị trí vừa lấy đã được thăm thì lấy phần tử tiếp theo ra khỏi stack, bỏ qua phần tử hiện tại, nếu chưa thăm thì thêm vào danh sách **visited**
        - Dùng hàm **isGoalState()** Kiểm tra, nếu vị trí vừa lấy là vị trí đích thì trả về danh sách các hành động để đi từ vị trí xuất phát đến đích, kết thúc vòng lặp
    - Dùng hàm **getSuccessors()** để lấy ra danh sách các ô có thể mở rộng tiếp theo 
        - Kiểm tra, đẩy vị trí, danh sách các hành động, chi phí ( bằng tổng chi phí từ điểm xuất phát đến vị trí hiện tại và từ đây đến vị trí tiếp theo ) vào hàng đợi ưu tiên nếu ô chưa được thăm
- Kết quả trả về là danh sách các hành động để đạt được trạng thái đích có chi phí bé nhất, trả về danh sách rỗng nếu không tìm được đích.
    > python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs<br>
### Câu hỏi 4: A* search
#### Cách làm:
- Sử dụng hàm Heuristic để ước lượng khoảng cách để giải quyết bài toán tìm đường đi ( Khoảng cách manhatan )
- Sử dụng hàng đợi ưu tiên ( đối với tổng chi phí ước lượng với chi phí đến vị trí của ô ) để cài đặt thuật toán
    > python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
#### Các phần còn lại tương tự bài trên
### Câu hỏi 5: Finding All the Corners
#### Cách làm:
- Trạng thái sẽ bao gồm vị trí hiện tại, và danh sách các góc cần phải đến
- Trạng thái đích đạt được khi danh sách góc cần phải đến không còn phần tử nào
- Lấy danh sách các trạng thái tiếp theo:
    - Successors bao gồm vị trí tiếp theo, danh sách các góc phải đến, danh sách các hành động và chi phí để đến vị trí tiếp theo 
    - Dựa vào các hướng và vị trí của tường  tìm được danh sách các ô có thể tới  
        - Nếu vị trí của ô tiếp theo là góc cần tới -> Cập nhật danh sách các góc cần tới còn lại
- Sử dụng thuật toán bfs để tìm đường đi 

    > python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem<br>
    > python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
### Câu hỏi 6: Corners Problem: Heuristic
- Tìm khoảng cách manhattan xa nhất từ điểm đang xét đến góc chưa được thăm
    > python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
### Câu hỏi 7: Eating All The Dots
### Câu hỏi 8: Suboptimal Search
- Tìm ra điểm thức ăn gần nhất và đi đến đó
    > python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
