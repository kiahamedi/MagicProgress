# MagicProgress
A python package that allows to implement and draw various examples of progress bar.
> version 0.0.3

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# Demo
![Alt text](https://raw.githubusercontent.com/kiahamedi/MagicProgress/main/screenshots/mgprogress.gif "Optional title")

# Install
```python
pip install MagicProgress
```
<br>

# Examples of How To Use
## Progress
To have a dynamic progress bar, it is enough to send your percentage to it in each period<br>
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 100%
<br>
```python
from MagicProgress import Progress
from time import sleep

for i in range(1, 101):
    Progress(i)
    sleep(0.01)
```
<br>


## Progress without Percentage
To have a dynamic progress bar without Percentage, it is enough to send your percentage to it in each period<br>
🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
<br>
```python
from MagicProgress import ProgressNoPercentage
from time import sleep

for i in range(1, 101):
    ProgressNoPercentage(i)
    sleep(0.01)
```
<br>


## Progress without Color
To have a dynamic progress bar without Color, it is enough to send your percentage to it in each period<br>
 [████████████████████] 100%
<br>
```python
from MagicProgress import ProgressNoColor
from time import sleep

for i in range(1, 101):
    ProgressNoColor(i)
    sleep(0.01)
```
<br>


## Progress without Color and Percentage
To have a dynamic progress bar without Color and Percentage, it is enough to send your percentage to it in each period<br>
 [████████████████████]
<br>
```python
from MagicProgress import ProgressNoColorPercentage
from time import sleep

for i in range(1, 101):
    ProgressNoColorPercentage(i)
    sleep(0.01)
```
<br>


## Draw Progress
To draw a progress bar, send your percentage to this function and it will return you a progress bar<br>
🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️⬜️ 50%
<br>
```python
from MagicProgress import DrawProgress

progress = DrawProgress(50)
print(progress)
```
<br>


## Draw Progress without Percentage
To draw a progress bar without Percentage, send your percentage to this function and it will return you a progress bar<br>
🟩🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 
<br>
```python
from MagicProgress import DrawProgressNoPercentage

progress = DrawProgressNoPercentage(30)
print(progress)
```
<br>


## Draw Progress without Color
To draw a progress bar without Color, send your percentage to this function and it will return you a progress bar<br>
[████████████████----] 80% 
<br>
```python
from MagicProgress import DrawProgressNoColor

progress = DrawProgressNoColor(80)
print(progress)
```
<br>

## Draw Progress without Color and Percentage
To draw a progress bar without Color and Percentage, send your percentage to this function and it will return you a progress bar<br>
[████████████--------] 
<br>
```python
from MagicProgress import DrawProgressNoColorPercentage

progress = DrawProgressNoColorPercentage(60)
print(progress)
```



## Are you a developer?
> 1-Fork it!</br>
> 2-Create your feature branch: git checkout -b my-new-feature</br>
> 3-Commit your changes: git commit -am 'Add some feature'</br>
> 4-Push to the branch: git push origin my-new-feature</br>
> 5-Submit a pull request</br>


>Thank you dear Shahab Karimifar for the idea of developing this library.
