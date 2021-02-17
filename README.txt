CRUD creado con Python 3.7 y SQLAlchemy siguiendo un modelo de base de datos relacionales.
El esquema de base de datos es sqlite3, para agregar un empleado a la base de datos se debe crear una instancia de la clase FactEmpleado, de la siguiente manera:
ej.1
emp1 = FactEmpleado(cedula=974513, nombres='Andrés', apellido='Baron', fechaNacimiento='22/10/1996', cargo='Doctor',email='af.baron10@uniandes.edu.co',isActive=1)

para añadir la experiencia se hace instanciando la clas experiencia de la siguiente forma:
exp1 = FactExperiencia(empresa='Google', cargo='Ingeniero', isActive=1, empleado=emp1)

Al consultar la base de datos encontrara la respectiva adicion de las instancias.