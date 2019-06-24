from xmlrpc import client
from pprint import pprint


class libraryApi():
	def __init__(self, srv , port,db ,user , pwd ):
		common = client.ServerProxy('http://%s:%d/xmlrpc/2/common' %(srv,port))
		self.api = client.ServerProxy('http://%s:%d/xmlrpc/2/object' %(srv,port))
		self.uid = common.authenticate(db , user, pwd, {})
		self.pwd=pwd
		self.db=db
		self.model='library.book'
	
	def execute(self,method , arg_list ,kwarg_dict=None):
		return self.api.execute_kw(self.db, self.uid ,self.pwd ,  self.model , method , arg_list ,kwarg_dict or {})
	
	def search_read(self,text=None):
		domain = [('name','ilike','text')] if text else []
		fields = ['id','name']
		return self.execute('search_read' ,[domain,fields])
		
	def create(self,title):
		value = {'name':title}
		return self.execute('create',[value])
		
	def write(self,id,title):
		value = {'name':title}
		return self.execute('write',[[id],value])
	
	def unlink(self , id ):
		return self.execute('unlink',[[id]])
	
	
	
	
if __name__=='__main__':
	srv , port , db = 'localhost',8060,'test22'
	user , pwd = 'chetan@gmail.com' , 'chetan'
	api = libraryApi(srv , port , db ,user , pwd )
	pprint(api.search_read())
	
	
