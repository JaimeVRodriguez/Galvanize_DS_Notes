## SQL in Python
***

### Create connection
```py
import psycopg2 
from psycopg2 import OperationalError 

def create_connection(db_name, db_user, db_password, db_host, db_port): 
	connection = None 
	try: 
		connection = psycopg2.connect( 
			database=db_name, 
			user=db_user, 
			password=db_password, 
			host=db_host, port=db_port, 
		) 
		print("Connection to PostgreSQL DB successful") 
	except OperationalError as e: 
		print(f"The error '{e}' occurred") 
	return connection
```

### Querying in Python


```py
from psycopg2 import sql query = sql.SQL("select {field} from {table} where {pkey} = %s").format(
	field=sql.Identifier('my_name'),
	table=sql.Identifier('some_table'), 
	pkey=sql.Identifier('id'))

cur.execute(query, (42,))
```

#### Bad Practice
```py
def query_user(num): 
	query = "SELECT * FROM logins WHERE userid = " + str(num) + ";" 
	
cur.execute(query_user(num))
```

#### Best practice
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