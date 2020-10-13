# PROJECT 2: Multi-Agent Search
```
 python autograder.py -q q1
 python autograder.py -q q2
 ..............
```
## Question 1: Reflex Agent
Viết lại hàm `evaluationFunction` để có được hàm đánh giá tốt hơn.
Đánh giá theo 
- Khoảng cách manhattan giữa Pacman và con ma gần nhất : Khoảng cách càng xa càng tốt
- Khoảng cách manhattan giữa Pacman và điểm thức ăn gần nhất: Khoảng cách càng gần càng tốt
![alt](https://cdn.fbsbx.com/v/t59.2708-21/121594216_809372076516676_1659725217425377384_n.gif?_nc_cat=108&_nc_sid=041f46&_nc_ohc=aJYztO52qnYAX-NpwxY&_nc_ht=cdn.fbsbx.com&oh=3aca18fc8ce879133b96d2b896511bf4&oe=5F8787C4)
