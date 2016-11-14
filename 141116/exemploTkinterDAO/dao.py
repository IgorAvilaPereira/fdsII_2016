import psycopg2

from user import *

class DAO:
	def __init__(self):
		self.conn = psycopg2.connect("host=localhost dbname=flask_admin user=postgres password=postgres")
	def removerPorUsername(self, username):
		cur = self.conn.cursor()
		cur.execute("DELETE FROM public.user WHERE username = %s", [username])
		self.conn.commit()
		cur.close()
	def listar(self):
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM public.user;")
		vet = []
		for row in cur:
			vet.append(User(row[0], row[1]))
		cur.close()
		return vet
	def inserir(self, user):
		cur = self.conn.cursor()
		try:
			cur.execute("INSERT INTO public.user (username, email) VALUES (%s, %s)", [user.username, user.email])
			self.conn.commit()
			cur.close()
			return True
		except:
			cur.close()
			return False
