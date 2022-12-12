## Matplotlib
***

![[Screenshot 2022-12-12 at 10.23.11 AM.png]]


### Styling
```py
import matplotlib.pyplot as plt

plt.style.use("seaborn-colorblind")
```

Link to more styles
https://matplotlib.org/3.2.2/gallery/style_sheets/style_sheets_reference.html


Custom styling
```py
import matplotlib.pyplot as plt 
SMALL_SIZE = 8 
MEDIUM_SIZE = 10 
BIGGER_SIZE = 12 
plt.rc('font', size=SMALL_SIZE) # controls default text sizes 
plt.rc('axes', titlesize=SMALL_SIZE) # fontsize of the axes title 
plt.rc('axes', labelsize=MEDIUM_SIZE) # fontsize of the x and y labels 
plt.rc('xtick', labelsize=SMALL_SIZE) # fontsize of the tick labels 
plt.rc('ytick', labelsize=SMALL_SIZE) # fontsize of the tick labels 
plt.rc('legend', fontsize=SMALL_SIZE) # legend fontsize 
plt.rc('figure', titlesize=BIGGER_SIZE) # fontsize of the figure title
```

``` note
===== ================= 
Alias Property 
===== =================
'lw' 'linewidth' 
'ls' 'linestyle' 
'c' 'color' 
'fc' 'facecolor' 
'ec' 'edgecolor' 
'mew' 'markeredgewidth' 
'aa' 'antialiased' 
===== =================
```

```py
font = {
	'family' : 'monospace', 
	'weight' : 'bold', 
	'size' : 'larger'} 
	
rc('font', **font) # pass in the font dict as kwargs
```

