from model.DAO import DAO, DAOList

if __name__=="__main__":
	d=DAO()
	dl=DAOList()
	dl.add(d)
	try:
		dl.add(None)
	except BaseException as exc:
		print(exc)
	dl.add(d)