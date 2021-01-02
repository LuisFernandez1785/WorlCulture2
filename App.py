from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexion a MySQL
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_DB']='worldculture'
mysql = MySQL(app)

#configuracion
app.secret_key = 'mykey'

#Rutas y funciones
@app.route('/')
def Index():
    return 'Ventana Raiz'

@app.route('/Productos')
def Productos():
    return 'Productos'

@app.route('/AdministrarProductos')
def AdministrarProductos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    return render_template('AdministrarProductos.html', productos = data)

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
        flash('El producto se agrego de manera correcta')
        return redirect(url_for('AdministrarProductos'))
    
@app.route('/EditProductos/<Id>')
def EditProductos(Id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE Id = %s', (Id))  
    data = cur.fetchall()
    return render_template('EditProductos.html', producto = data[0])

@app.route('/update/<Id>', methods=['POST'])
def update_contact(Id):
    if request.method == 'POST':
        Codigo = request.form['Codigo']
        Nombre = request.form['Nombre']
        Descripcion = request.form['Descripcion']
        Departamento = request.form['Departamento']
        Seccion = request.form ['Seccion']
        Stock = request.form['Stock']
        precioVenta = request.form['PrecioVenta']
        precioCompra = request.form['PrecioCompra']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE productos
            SET 
                Codigo = %s,
                Nombre= %s,
                Descripcion = %s,
                Departamento = %s,
                Seccion = %s,
                Stock = %s,
                PrecioVenta = %s,
                PrecioCompra = %s
            WHERE Id = %s
        """, (Codigo, Nombre, Descripcion, Departamento, Seccion, Stock, precioVenta, precioCompra, Id))
        flash('Producto editado de manera correcta')
        mysql.connection.commit()
        return redirect(url_for('AdministrarProductos'))

@app.route('/DeleteProductos/<string:Id>')
def DeleteProductos(Id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE Id = {0}'.format(Id))
    mysql.connection.commit()
    flash('Producto eliminado de manera correcta')
    return redirect(url_for('AdministrarProductos'))

if __name__== '__main__':
    app.run(port = 3000, debug = True)