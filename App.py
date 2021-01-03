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
@app.route('/Index')
def Index():
    return render_template('Index.html')

@app.route('/Productos')
def Productos():
    return 'Productos'

@app.route('/PanelAdministracion')
def PanelAdministracion():
    return render_template('PanelAdministracion.html')

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


##Administradores
@app.route('/AdministrarAdmin')
def AdministrarAdmin():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Administradores')
    data = cur.fetchall()
    return render_template('AdministrarAdmin.html', Administradores = data)


@app.route('/AddAdministradores', methods=['POST'])
def add_Administradores():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Usuario = request.form['Usuario']
        Password = request.form['Password']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Administradores (Nombre, Usuario, Password) VALUES (%s, %s, %s)',
        (Nombre, Usuario, Password))
        mysql.connection.commit()
        flash('El Usuario Administrador se agrego de manera correcta')
        return redirect(url_for('AdministrarAdmin'))

@app.route('/EditAdministradores/<Id>')
def EditAdministradores(Id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Administradores WHERE Id = %s', (Id))  
    data = cur.fetchall()
    return render_template('EditAdministradores.html', Administrador = data[0])

@app.route('/updateAdmin/<Id>', methods=['POST'])
def update_Administradores(Id):
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Usuario = request.form['Usuario']
        Password = request.form['Password']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Administradores
            SET 
                Nombre= %s,
                Usuario = %s,
                Password = %s
            WHERE Id = %s
        """, (Nombre, Usuario, Password, Id))
        flash('El Usuario Administrador editado de manera correcta')
        mysql.connection.commit()
        return redirect(url_for('AdministrarAdmin'))

@app.route('/DeleteAdministradores/<string:Id>')
def DeleteAdministradores(Id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Administradores WHERE Id = {0}'.format(Id))
    mysql.connection.commit()
    flash('El Usuario Administrador eliminado de manera correcta')
    return redirect(url_for('AdministrarAdmin'))

##Pedidos
@app.route('/AdministrarPedidos')
def AdministrarPedidos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Pedidos')
    data = cur.fetchall()
    return render_template('AdministrarPedidos.html', Pedidos = data)


@app.route('/AddPedidos', methods=['POST'])
def add_Pedidos():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Usuario = request.form['Usuario']
        Direccion = request.form['Direccion']
        Contenido = request.form['Contenido']
        Costo = request.form['Costo']
        CostoEnvio = request.form['CostoEnvio']
        CodigoRastreo = request.form['CodigoRastreo']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO Pedidos (Nombre, Usuario, Direccion, Contenido, Costo, CostoEnvio, CodigoRastreo) VALUES (%s, %s, %s, %s, %s, %s, %s)',
        (Nombre, Usuario, Direccion, Contenido, Costo, CostoEnvio, CodigoRastreo))
        mysql.connection.commit()
        flash('El Pedido se agrego de manera correcta')
        return redirect(url_for('AdministrarPedidos'))

@app.route('/EditPedidos/<Id>')
def EditPedidos(Id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Pedidos WHERE Id = %s', (Id))  
    data = cur.fetchall()
    return render_template('EditPedidos.html', Pedido = data[0])


@app.route('/updatePedidos/<Id>', methods=['POST'])
def update_Pedidos(Id):
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Usuario = request.form['Usuario']
        Direccion = request.form['Direccion']
        Contenido = request.form['Contenido']
        Costo = request.form['Costo']
        CostoEnvio = request.form['CostoEnvio']
        CodigoRastreo = request.form['CodigoRastreo']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Pedidos
            SET 
                Nombre= %s,
                Usuario = %s,
                Direccion = %s,
                Contenido = %s,
                Costo = %s,
                CostoEnvio = %s,
                CodigoRastreo = %s
            WHERE Id = %s
        """, (Nombre, Usuario, Direccion, Contenido, Costo, CostoEnvio, CodigoRastreo, Id))
        flash('Pedido editado de manera correcta')
        mysql.connection.commit()
        return redirect(url_for('AdministrarPedidos'))

@app.route('/DeletePedidos/<string:Id>')
def DeletePedidos(Id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Pedidos WHERE Id = {0}'.format(Id))
    mysql.connection.commit()
    flash('Pedido eliminado de manera correcta')
    return redirect(url_for('AdministrarPedidos'))

if __name__== '__main__':
    app.run(port = 3000, debug = True)