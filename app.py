from flask import Flask, request, render_template
import pymysql




class web_inteface():

	"""Класс интерфейса"""
	def __init__(self):
		self.con()
		self.web_start()
	def db_check(self):
		"""Проверка на наличие таблицы"""

		self.cursor = self.conn.cursor()
		self.cursor.execute("""
						SELECT table_name
						FROM information_schema.tables
						WHERE table_schema = 'mycont'
						AND table_name = 'web_interface_test21'
				  		""")
		self.ell1 = self.cursor.fetchall()

		if () == self.ell1:
			self.cursor.execute("""CREATE TABLE web_interface_test21
			(
			id int PRIMARY KEY AUTO_INCREMENT,
			title text NOT NULL,
			description text NOT NULL,
			created_at date NOT NULL,
			updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
			)""")

	def con(self):
		"""Подключение локального сервера MySQL"""

		try:
			self.conn = pymysql.connect(
				host='127.0.0.1',
				port=3306,
				user='root',
				password='1234',
				database='mycont',
				cursorclass=pymysql.cursors.DictCursor
			)
			self.cursor = self.conn.cursor()
			self.db_check()
		except:
			print("Error connect")
	def delete_work(self, ID):
		"""Удалить задачу в базе данных"""
	def update_mysql(self, ID, title, desc):
		"""Обновить задачу в базе данных"""
	def get_info_to_work(self, ID):
		"""Получить информацию о конкретной задаче"""
	def get_list(self):
		"""Получить список всех задач"""
		self.cursor.execute("""
		SELECT * FROM web_interface_test21
		""")
		item = self.cursor.fetchall()
		print(item)
	def insert_mysql(self, title, desc):
		print('yes')
		"""Занести информацию о новой задаче в базу данных"""
		self.cursor.execute(f"""INSERT INTO web_interface_test21(title, description) VALUES ('{title}','{desc}')""")
		elms = self.cursor.fetchall()
		self.conn.commit()
		return elms

	def web_start(self):
		"""Начало работы веб блока"""

		app = Flask(__name__)

		@app.route('/')
		def intopage():
			"""Титульный лист"""
			return render_template('index.html')

		@app.route('/tasks', methods=['POST', 'GET'])
		def tasks():
			"""Методы приложения"""
			if request.method == 'POST':
				opt = request.form['input_title']
				opd = request.form['input_desc']
				if opt and opd:
					self.insert_mysql(opt, opd)
			if request.method == 'GET':
				i = self.get_list()
			return render_template('creater.html')

		@app.route('/tasks/<id>')
		def Id_tasks(id):
			"""Переход по ID"""
			return f'menrorne {id}'

		app.run(debug=True)

if __name__ == '__main__':
	web_inteface()