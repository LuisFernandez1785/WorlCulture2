from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexion a MySQL
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_DB']='worldculture'
mysql = MySQL(app)

#Rutas y funciones
@app.route('/')
def Index():
    return 'Ventana Raiz'

@app.route('/Productos')
def Productos():
    return 'Productos'

@app.route('/AdministrarProductos')
def AdministrarProductos():
    return render_template('AdministrarProductos.html')

@app.route('/AddProductos', methods=['POST'])
def add_productos():
    if request.method == 'POST':
        Codigo = request.form['Codigo']
        Nombre = request.form['Nombre']
        Descripcion = request.form['Descripcion']
        Departamento = request.form['Departamento']
        Seccion = request.form['Seccion']
        Stock = request.form['Stock']
        PrecioVenta = request.form['PrecioVenta']
        PrecioCompra = request.form['PrecioCompra']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO productos (Codigo, Nombre, Descripcion, Departamento, Seccion, Stock, PrecioVenta, PrecioCompra) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
        (Codigo, Nombre, Descripcion, Departamento, Seccion, Stock, PrecioVenta, PrecioCompra))
        mysql.connection.commit()

        return 'El producto fue guardado correctamente'
    



if __name__== '__main__':
    app.run(port = 3000, debug = True)