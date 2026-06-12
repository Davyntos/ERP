import pymysql

# Le dice a Django que trate a pymysql como el conector oficial de MySQL
pymysql.install_as_MySQLdb()