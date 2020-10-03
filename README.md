# Trí tuệ nhân tạo INT3401 8


## Bài tập 1: Pacman Search

### Câu hỏi 1: Tìm điểm cố định bằng phương pháp tìm kiếm theo chiều sâu (depth first search)
<!-- Màn hình được chia thành các ô vuông được đánh số thứ tự tương ứng -->
#### Cách làm:
- Từ vị trí xuất phát, đi tới ô liền kề của nó mà chưa được thăm, lưu lại tọa độ của các ô đã này. Tiếp tục lấy ô mới nhất vừa được thăm, đi tiếp. Trong quá trình duyệt, nếu không thấy ô liền kề, chưa được thăm thì quay lại ô trước nó. Thuật toán dừng lại khi không còn ô chưa được thăm hoặc tới được đích. 
<!-- - Trong quá trình đi từ đỉnh này sang đỉnh kia , tiến hành lưu lại đỉnh cha của đỉnh kề, để khi đi ngược lại từ đỉnh Kết Thúc đến đỉnh Xuất Phát, ta có được đường đi cần tìm. -->
- Sử dụng stack để cài đặt thuật toán, các phần tử được thêm vào sau sẽ được lấy ra trước, các ô có chung một ô liền trước sẽ được lưu cạnh nhau trong stack, phải duyệt xong một nhánh rồi mới quay lại duyệt tiếp nhánh khác 
#### Cài đặt:
- **visited**: dùng để lưu vị trí các ô đã thăm
- **stack**: dùng để lưu vị trí, các hành động để có thể mở rộng ra các ô tiếp theo
- **state**: dùng để lưu vị trí của ô hiện tại
- **actions**: danh sách các hành động để đi từ vị trí xuất phát đến ô hiện tại
- **successor**: vị trí của ô tỉếp theo có thể mở rộng
- **action**: hành động để đi từ ô hiện tại tới ô tiếp theo
- **cost**: chi phi cần cho việc đi từ ô hiện tại tới ô tiếp theo *( trong bài này không dùng đến )*
#### Chạy chương trình:     
- Đẩy vào stack vị trí xuất phát, và danh sách các hành động ( lúc này là rỗng )
- Chạy vòng lặp cho đến khi không còn phần tử nào trong stack hoặc tìm được đích. 
    - Lấy vị trí, và danh sách các hành động ra khỏi stack 
        - Kiểm tra, nếu vị trí vừa lấy đã được thăm thì lấy phần tử tiếp theo ra khỏi stack, bỏ qua phần tử hiện tại
        - Dùng hàm **isGoalState()** Kiểm tra, nếu vị trí vừa lấy là vị trí đích thì trả về danh sách các hành động để đi từ vị trí xuất phát đến đích, kết thúc vòng lặp
    - Dùng hàm **getSuccessors()** để lấy ra danh sách các ô có thể mở rộng tiếp theo 
        - Kiểm tra, đẩy vị trí và danh sách các hành động vào stack nếu ô chưa được thăm
- Kết quả trả về là danh sách các hành động để đạt được trạng thái đích, trả về danh sách rỗng nếu không tìm được.
### Câu hỏi 2: Tìm điểm cố định bằng phương pháp tìm kiếm theo chiều rộng (breadth first search)
#### Cách làm:
- Từ vị trí xuất phát, đi tới tất cả các ô liền kề nó mà chưa được thăm, lưu lại tọa độ của các ô này. Sau khi thăm hết các đỉnh liền kề này, tiếp tục thăm các ô liền kề của các ô vừa được thăm, tiếp tục cho đến khi không còn đỉnh nào chưa được thăm hoặc đến được đích.
- Sử dụng queue để cài đặt thuật toán, các phần tử được thêm vào trước sẽ được lấy ra trước, các ô có chung một ô liền trước sẽ được cạnh nhau trong queue, phải thăm hết các ô này rồi mới duyệt các ô liền kề các ô này
#### Cài đặt

