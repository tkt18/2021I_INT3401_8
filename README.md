# 2021I_INT3401_8
```
python pacman.py

python pacman.py --layout testMaze --pacman GoWestAgent

python pacman.py -h

python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch

python pacman.py -l bigMaze -z .5 -p SearchAgent

python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

python pacman.py -l mediumDottedMaze -p StayEastSearchAgent

python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
...........................................................................
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

-p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic

python pacman.py -l testSearch -p AStarFoodSearchAgent

python pacman.py -l trickySearch -p AStarFoodSearchAgent

python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 

```
# Trí tuệ nhân tạo INT3401 8


## Bài tập 1: Pacman Search

### Câu hỏi 1: 
Tìm điểm cố định bằng phương pháp tìm kiếm theo chiều sâu (depth first search)
<!-- Màn hình được chia thành các ô vuông được đánh số thứ tự tương ứng -->
- Cách làm:
    - Từ vị trí xuất phát, duyệt tới các ô kề của nó, lưu lại tọa độ của các ô này. Tiếp tục lấy ô mới nhất vừa được lưu vào, duyệt cho đến khi không còn ô nào có thể đi hoặc đạt được trạng thái đích.
    <!-- - Trong quá trình đi từ đỉnh này sang đỉnh kia , tiến hành lưu lại đỉnh cha của đỉnh kề, để khi đi ngược lại từ đỉnh Kết Thúc đến đỉnh Xuất Phát, ta có được đường đi cần tìm. -->
    - Sử dụng stack để lưu danh sách các ô kề, khi không còn ô nào có thể đi nữa có thể quay lại vị trí đỉnh cha 

### Câu hỏi 2:
Tìm điểm cố định bằng phương pháp tìm kiếm theo chiều rộng (breadth first search)
- Cách làm:
    - tương tự dfs
    - Sử dụng queue để lưu danh sách các ô kề, 
