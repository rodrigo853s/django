from django.db import models
import oracledb

# Create your models here.

class Departamento:
    numero = 0
    nombre = ""
    localidad = ""

class ServiceDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM'
            ,password='oracle', dsn='localhost/xe')
    
    def getDepartamentos(self):
        sql = "select * from DEPT"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista = []
        for row in cursor:
            dept = Departamento()
            dept.numero = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            lista.append(dept)
        cursor.close()
        return lista
    
    # Método para insertar un departamento

    def insertDepartamento(self, numero, nombre, localidad):
        sql = "insert into DEPT values (:p1, :p2, :p3)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        # Si queremos, obtenemos los registros
        return registros 
    
    # Método para eliminar un departamento
    
    def eliminarDepartamento(self, numero):
        sql = "delete from DEPT where DEPT_NO = :p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, ))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        # Si queremos, obtenemos los registros
        return registros 
    
    # Método para actualizar un departamento
    
    def actualizarDepartamento(self, numero, nombre, localidad):
        sql = "update DEPT set DNOMBRE = :p1, LOC = :p2 where DEPT_NO = :p3"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, localidad, numero))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        # Si queremos, obtenemos los registros
        return registros 
    
    # Detalles departamento

    def detallesDepartamento(self, numero):
        sql = "select * from DEPT where DEPT_NO = :p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, ))
        row = cursor.fetchone()
        dept = Departamento()
        dept.numero = row[0]
        dept.nombre = row[1]
        dept.localidad = row[2]
        cursor.close()
        return dept
    
class Hospital:
    hosp_cod = 0
    nombre = ""
    direccion = ""

class ServiceHospitales:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM'
            ,password='oracle', dsn='localhost/xe')
    
    def getHospitales(self):
        sql = "select * from HOSPITAL"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista = []
        for row in cursor:
            hosp = Hospital()
            hosp.hosp_cod = row[0]
            hosp.nombre = row[1]
            hosp.direccion = row[2] 
            lista.append(hosp)
        cursor.close()
        return lista

class Empleado:
    idEmpleado = 0
    apellido = ""
    oficio = ""
    salario = 0
    departamento = 0

class ServiceEmpleados:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM'
           , password='oracle', dsn='localhost/xe')
    
    def getEmpleados(self):
        sql = "select * from EMP"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista = []
        for row in cursor:
            emp = Empleado()
            emp.idEmpleado = row[0]
            emp.apellido = row[1]
            emp.oficio = row[2]
            emp.salario = row[5]
            emp.departamento = row[7]
            lista.append(emp)
        cursor.close()
        return lista
    
    def getEmpleadosDepartamento(self, numDept):
        sql = "select * from EMP where DEPT_NO=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numDept, ))
        lista = []
        for row in cursor:
            emp = Empleado()
            emp.idEmpleado = row[0]
            emp.apellido = row[1]
            emp.oficio = row[2]
            emp.salario = row[5]
            emp.departamento = row[7]
            lista.append(emp)
        cursor.close()
        return lista