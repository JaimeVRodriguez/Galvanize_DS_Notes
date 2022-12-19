## EDA Project
***

### File Structure
data
- empty.csv
images
* tb.txt
notebooks
* eda.ipynb
* testing.ipynb
src
- functions.py


Importing sys for 
```py
import sys
sys.path.insert(0, '../src')
sys.path.insert(0, '../data')


import <file_name>

%load_ext autoreload
%autoreload 2
```


functions.py
```py
def function(a, b):
	return a + b


if __name__ == '__main__':

	function(a, b)
```
