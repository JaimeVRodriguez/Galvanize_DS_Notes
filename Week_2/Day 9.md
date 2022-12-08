## Pandas
***

### Instantiating and Indexing Series

``` py
import pandas as pd

#create a series
animals = pd.Series([20,5,3,10],
					index=['dog', 'snake', 'bird', 'cat'])

print(animals)
```


``` output
dog 20 
snake 5 
bird 3 
cat 10 
dtype: int64
```


``` py
Access by calling the index name print(animals['snake'], '\n') 

Access the labeled index print(animals.loc['snake'], '\n') 

Access the series at the 1st index print(animals.iloc[1])

```

``` py
prices = pd.Series([100, 15, 40, 50], 
					index=['dog', 'snake', 'cat']) 
					
print(animals * prices)
```


``` output
dog 2000 
snake 75 
bird NaN 
cat 500
```


### Instatiating and Indexing DataFrames

``` py
import pandas as pd 
import numpy as np 

price_lst = [1, 2, 5, 3, 1] 
inventory_lst = [22, 50, np.nan, 41, 10] discount_lst = [1, 1, 2, 2.5, 0] 
fruit_lst = ['apple', 'banana', 'jackfruit', 'mango', 'pear'] 

prices = pd.Series(price_lst, index=fruit_lst) 
discount_prices = pd.Series(discount_lst, index=fruit_lst) 
inventory = pd.Series(inventory_lst, index=fruit_lst) 

produce = pd.DataFrame({ 
		'price': prices, 
		'discount': discount_prices, 
		'inventory': inventory }) 
		
print(produce)
```

``` output
		price discount inventory 
apple     1      1.0     22.0 
banana    2      1.0     50.0 
jackfruit 5      2.0     NaN 
mango     3      2.5     41.0 
pear      1      0.0     10.0
```

### 
