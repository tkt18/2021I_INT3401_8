# Project 4: Ghostbusters

## Question 1: Exact Inference Observation
- Cập nhật phương thức `observe` lớp `ExactInference` trong file `inference.py` để cập nhật xác suất phân bổ vị trí của ma qua cảm biến cảu Pacman.
- 
> python autograder.py -q q1
## Question 2: Exact Inference with Time Elapse
- Cài đặt phương thức `elapseTime` của lớp `ExactInference`
> python autograder.py -q q2</br>
> python autograder.py -t test_cases/q2/2-ExactElapse

## Question 3: Exact Inference Full Test
- Cài đặt phương thức `chooseAction` của `GreedyBusterAgent` trong file `bustersAgents.py`.
> python autograder.py -q q3</br>
> python autograder.py -q q3 --no-graphics
## Question 4: Approximate Inference Observation
- Cài đặt các hàm `initializeUniformly`, `getBeliefDistribution`, và `observe` cho lớp `ParticleFilter` trong file `inference.py`.
> python autograder.py -q q4

## Question 5: Approximate Inference with Time Elapse
- Cài đặt hàm `elapseTime` cho lớp `ParticleFilter` trong `inference.py`
> python autograder.py -q q5</br>
> python autograder.py -t test_cases/q5/2-ParticleElapse

# Question 6: Joint Particle Filter Observation
- Cài đặt hàm `initializeParticles`, `getBeliefDistribution`, và `observeState` trong `JointParticleFilter`.
> python autograder.py -q q6
# Question 7: Joint Particle Filter with Elapse Time
- Hoàn thành phương thức `elapseTime` cho `JointParticleFilter` trong `inference.py` để lấy mẫu lại từng `particle` một cách chính xác cho lưới Bayes.
>  python autograder.py -q q7 --no-graphics </br>
>  python autograder.py -q q7 

