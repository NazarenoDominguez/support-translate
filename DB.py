import mysql.connector



class FormsDb():

    def __init__(self):
        self.conexion = mysql.connector.connect( 
            host='localhost',
            database ='db-support-translate', 
            user = 'root',
            password ='')


    def newFormdb(self, arr):
        cur = self.conexion.cursor()
        sql='''INSERT INTO forms (NOMBRE, DESCRIPCION, FORMULARIO) 
        VALUES('{}','{}', '{}')'''.format(arr[0],arr[1],arr[2])
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def selectAll(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM forms " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def selectNDes(self):
        cursor = self.conexion.cursor()
        sql = "SELECT NOMBRE , DESCRIPCION FROM forms " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
    
    def selectForm(self,name):
        cursor = self.conexion.cursor()
        sql = "SELECT FORMULARIO FROM forms WHERE NOMBRE = '{}'".format(name)  
        cursor.execute(sql)
        registro = cursor.fetchone()
        return registro
    
    def selectname(self,name):
        cursor = self.conexion.cursor()
        sql = "SELECT NOMBRE FROM forms WHERE NOMBRE = '{}'".format(name)  
        cursor.execute(sql)
        registro = cursor.fetchone()
        return registro
        
    def searchFormDb(self, name):
        cur = self.conexion.cursor()
        sql = '''SELECT * FROM forms WHERE NOMBRE = '{}' '''.format(name)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 


    def deleteFormDb(self, nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM forms WHERE NOMBRE = '{}' '''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
  
    def updateFormDb(self,name, descripcion, formula):
        cur = self.conexion.cursor()
        sql ='''UPDATE forms SET  DESCRIPCION = '{}', FORMULARIO = '{}'
        WHERE NOMBRE = '{}' '''.format(descripcion, formula,name)
        cur.execute(sql)
        cur_row = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return cur_row
##################
