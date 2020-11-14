# Project 5: Classification
## Question 1: Perceptron
- Cài đặt phương thức `train` trong `perceptron.py` cập nhật trọng số.
- Công thức:</br>
    `wy = wy + f`</br>
    `wy'= wy'- f`</br>
- `f` là `featurebetter`
```
python dataClassifier.py -c perceptron 
```
## Question 2: Perceptron Analysis
- Cài đặt phương thức `findhighWeifeatures` trả về 100 features của `weight` cao nhất
- so sánh ta được `a` là kết quả và trả lời trong `answer.py`
```
python dataClassifier.py -c perceptron -w  
```
## Question 3: MIRA 
Cài đặt `trainAndTune` trong file `mira.py`. Train một trình phân loại `MIRA` bằng cách sử dụng từng giá trị của `C` trong `Cgrid`.
```
python dataClassifier.py -c mira --autotune 
```
## Question 4 Digit Feature Design
- Cài đặt hàm `enhancedFeatureExtractorDigit` trong file `dataClassifier.py`
```
python dataClassifier.py -d digits -c naiveBayes -f -a -t 1000  
```
# Question 5 Behavioral Cloning
- Cài đặt phương thức `train` trong `perceptron_pacman.py`. Cài đặt tương tự phương thức `train` khác
```
python dataClassifier.py -c perceptron -d pacman

```
# Question 6 Pacman Feature Design
- Thiết kế feature mới cho Pacman trong hàm `enhancedPacmanFeatures` trong `dataClassifier.py`
```
python dataClassifier.py -c perceptron -d pacman -f -g ContestAgent -t 1000 -s 1000
```