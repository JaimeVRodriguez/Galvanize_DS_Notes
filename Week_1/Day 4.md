 ## Functions
***

### Single line code
Below code is typical
`evens = [] 
`for num in range(10):`
	`if num % 2 == 0:`
		`evens.append(num)`

Single line version
`evens = [num for num in range(10) if num % 2 == 0]`

Dictionary example
`squares_dict = {}`
`for num in range(1, 6):`
	`squares_dict[num] = num ** 2

`squares_dict = {num: num ** 2 for num in range(1, 6)}`

### Optional Parameter

`def func_name(n=arg):`
n will automatically be used if user does not input argument

`isintance(to_add, checker)`

