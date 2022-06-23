import psycopg2


class Connect:
	"""docstring for ClassName"""
	def __init__(self, host='188.166.99.136',user='postgres',password='',database='APLELIVE',port=''):
		# self.arg = arg
		self.host = host
		self.user = user
		self.password = password
		self.database = database
		self.port = port

	def postgresConnect(self):
		connection = psycopg2.connect(user = self.user,
									   password = self.password,
									   host = self.host,
									   port = self.port,
									   database = self.database)
		cr = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
		return cr
	def postgresConnectNorm(self):
		connection = psycopg2.connect(user = self.user,
									   password = self.password,
									   host = self.host,
									   port = self.port,
									   database = self.database)
		# cr = connection.cursor()
		return connection
	def postgresConnect137(self):
		connection = psycopg2.connect(user = 'postgres',
									   password = '',
									   host = '188.166.99.136',
									   port = '',
									   database = 'APLELIVE')
		cr = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
		return cr

	def insert(self,obj):
		count = 0
		count_1 = 0
		names = "("
		values = "("
		table = ""
		print(obj)
		try:
			obj.pop('csrfmiddlewaretoken')
			table = obj['table']
			obj.pop('table')
			obj.pop('appli')
		except Exception as e:
			print("no form")
		connection = self.postgresConnectNorm()
		cr = connection.cursor()
		
		print(obj.items())
		# for key,value in obj.items():
		# 	if key != 'table' and key != 'appli':
		# 		count = count + 1
		for key,value in obj.items():
			# print(count)
			
			count_1 = count_1 + 1
			if len(obj) != count_1:
				if key != 'table' and key != 'appli' :
					names = names + key + ","
					values = values + "'"+value + "',"
			else:
				names = names + key + ")"
				values = values + "'"+value + "')"
			# if key == 'table':
			# 	table = value
		print("insert into %s %s values %s" % (table, names,values))
		message = ""
		try:
			cr.execute("insert into %s %s values %s" % (table, names,values))
			connection.commit()
		except Exception as e:
			message = str(e)
			return message
		# except Exception as e:
			# print(e)
		
		if cr.rowcount == 1:
			message = "VALUE INSERTED"
		else:
			message = "An Error Occured"
		return message
	def update(self,obj,column,column_value):
		count = 0
		count_1 = 0
		names = ""
		values = ""
		table = ""
		print(obj)
		obj.pop('csrfmiddlewaretoken')
		obj.pop('edit')
		connection = self.postgresConnectNorm()
		cr = connection.cursor()
		
		print(obj.items())
		for key,value in obj.items():
			
			count = count + 1
		for key,value in obj.items():
			# print(count)
			
			count_1 = count_1 + 1
			if count > count_1:
				if key != 'table' and key != 'appli' :
					names = names + key + "=" + "'"+value + "',"
					# values = values + "'"+value + "',"
			else:
				if key != 'table' and key != 'appli':
					names = names + key + "=" + "'"+value + "'"
			if key == 'table':
				table = value
		
		cr.execute("update %s set %s where %s = %s" % (table, names,column,column_value))
		connection.commit()
		# except Exception as e:
			# print(e)
		message = ""
		if cr.rowcount == 1:
			message = "UPDATE WAS SUCCESSFUL"
		else:
			message = "An Error Occured"
		return message
	def selectall(self,sql):
		cr = self.postgresConnect()
		cr.execute(sql)
		row = cr.fetchall()
		if row == None:
			row = []
		return row
		# return row
	def select_single(self,sql):
		cr = self.postgresConnect()
		cr.execute(sql)
		row = cr.fetchone()		
		if row == None:
			row = []
		return row