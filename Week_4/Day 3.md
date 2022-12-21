## SQL in Python
***


### Querying in Python
```py
from psycopg2 import sql query = sql.SQL("select {field} from {table} where {pkey} = %s").format(
	field=sql.Identifier('my_name'),
	table=sql.Identifier('some_table'), 
	pkey=sql.Identifier('id'))

cur.execute(query, (42,))
```

```py
def query_user(num): 
	query = "SELECT * FROM logins WHERE userid = " + str(num) + ";" 
	
cur.execute(query_user(num))
```

```py
def is_user(id: int) -> bool: 
	cur.execute("""SELECT * FROM logins 
					WHERE userid = %(id)s""",
					{'id': username}) 
	
	result = cur.fetchone() 
	
	if result is None: 
		# User does not exist 
		return False 
		
	user, = result 
	return user
```