# Taylor series
### Formula for taylor series: ![](https://latex.codecogs.com/svg.latex?\Large%20\\sin^2(2x)=0.5+\\sum_{k=0}^{n}{\\frac{(-1)^{k+1}{2}^{4k-1}}{(2k!)}{x}^{2k}})
### Usage
* Calculate taylor series with given number of elements and given argument
```python
>>> calc_taylor_series(.4, 5)
0.5145849010793652
```
* Calculate error with given number of elements and given argument between approximated series and actual value 
```python
>>> calc_error(.56, 6)
1.620769026267066e-05
```
* Calculate maximum error with given number of elements on range from 0 to pi/2 between approximated series and actual value 
```python
>>> calc_max_error(10)
0.0016788970882212256
```
* Calculate number of elements you need to achieve epsilon accuracy at point x 
```python
>>> get_count(.13, 10 ** -2)
2
```
* View accuracy at point x
```python
>>> view_accuracy(.5)
  Iterations        Diff
------------  -----------
           2  0.291927
           5  0.00013691
           7  9.24225e-08
           8  1.54588e-09
          10  2.13718e-13
          12  1.11022e-16
          15  1.11022e-16
          20  1.11022e-16
```
* View overall accuracy
```python
>>> view_overall_accuracy()
  Iterations    Max diff on (0; pi/2)
------------  ------------------------
           2               9.83446
           5               9.82659
           7               0.714976
           8               0.121102
          10               0.0016789
          12               1.04301e-05
          15               1.5154e-09
          20               7.90513e-15
```
* Animation \
Firstly, you need to install manim + ffmpeg + latex, then
``` bash
python animation.py
```
### Visualisation with explanation
Video can be found at [assets/animation.mp4](assets/animation.mp4) 
![](assets/animation.gif)