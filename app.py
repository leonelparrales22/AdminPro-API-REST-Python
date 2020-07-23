# DEPENDENCIAS:
# FLASK
# FLASK_MYSQL
from datetime import date, timedelta

from flask import Flask, render_template, request, redirect, url_for, json, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)

# DATABASE CONFIG
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'bdd'
app.config['MYSQL_DATABASE_Host'] = 'localhost'
mysql.init_app(app)
# DATABSE CONNECTION
conn = mysql.connect()
cursor = conn.cursor()

# BDD MANAGE
# colores = ["#75389b", "#2c63e2", "#e90504", "#fed10c", "#00a728", "#ff9a00"]
colores = ["rgba(119,77,155, 0.9)", "rgba(47,108,226, 0.9)", "rgba(233,64,55, 0.9)", "rgba(254,210,56, 0.9)",
           "rgba(62,168,42, 0.9)", "rgba(255,156,59, 0.9)"]


def comprobar_usuario(cedula_usuario, contrasenia):
    cursor.execute(
        f'SELECT * FROM `USUARIOS` WHERE rol="ADMIN" AND cedula_usuario="{cedula_usuario}" AND contrasenia="{contrasenia}"')
    data = cursor.fetchone()
    return data


# SELECT CELULARES.marca_celular, COUNT(CELULARES.marca_celular) AS PROMEDIO
# FROM `DETALLE_VENTA`,`CELULARES`, `VENTAS`
# WHERE DETALLE_VENTA.id_celular = CELULARES.id_celular
# AND DETALLE_VENTA.codigo_venta = VENTAS.codigo_venta
# AND YEAR(VENTAS.fecha) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH)
# AND MONTH(VENTAS.fecha) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH)
# GROUP BY CELULARES.marca_celular

# ultimos 7 dias
# SELECT DATE_FORMAT(fecha, '%m/%d/%Y') FROM VENTAS WHERE fecha BETWEEN CURDATE() - INTERVAL 6 DAY AND CURDATE() + 1 ORDER BY `DATE_FORMAT(fecha, '%m/%d/%Y')` ASC
# SELECT  DATE_FORMAT(fecha, '%Y-%m-%d') AS FECHA, SUM(CELULARES.precio_celular*DETALLE_VENTA.cantidad) AS TOTAL
# FROM    VENTAS, DETALLE_VENTA, CELULARES
# WHERE   fecha BETWEEN CURDATE() - INTERVAL 6 DAY AND CURDATE() + 1
# AND VENTAS.codigo_venta = DETALLE_VENTA.codigo_venta
# AND DETALLE_VENTA.id_celular = CELULARES.id_celular
# GROUP BY FECHA
# ORDER BY `FECHA` ASC


def calcular_marca_mas_vendido():
    cursor.execute(
        'SELECT CELULARES.marca_celular, COUNT(CELULARES.marca_celular) AS PROMEDIO FROM `DETALLE_VENTA`,`CELULARES` '
        'WHERE DETALLE_VENTA.id_celular = CELULARES.id_celular GROUP BY CELULARES.marca_celular')
    data = cursor.fetchall()
    total = 0
    contador = -1
    grafico = "["
    for x in data:
        total += x[1]
        contador += 1
    contador = 1
    for x, color in zip(data, colores):
        lista = {
            "label": x[0],
            "data": x[1] / total,
            "color": color
        }
        y = json.dumps(lista)
        grafico += y
        if len(data) != contador:
            grafico += ","
        contador += contador
    grafico += "]"
    return grafico


def calcular_rango_celulares_mas_vendido():
    cursor.execute(
        'SELECT CELULARES.precio_celular FROM `DETALLE_VENTA`, `CELULARES` WHERE DETALLE_VENTA.id_celular = '
        'CELULARES.id_celular')
    data = cursor.fetchall()
    contador_menos_100 = 0
    contador_entre_100_200 = 0
    contador_entre_200_300 = 0
    contador_entre_300_400 = 0
    contador_entre_400_500 = 0
    contador_mayores_500 = 0
    total = -1
    for x in data:
        total += 1
        if x[0] <= 100:
            contador_menos_100 += 1
            continue
        if 100 < x[0] <= 200:
            contador_entre_100_200 += 1
            continue
        if 200 < x[0] <= 300:
            contador_entre_200_300 += 1
            continue
        if 300 < x[0] <= 400:
            contador_entre_300_400 += 1
            continue
        if 400 < x[0] <= 500:
            contador_entre_400_500 += 1
            continue
        if x[0] > 500:
            contador_mayores_500 += 1
            continue

    grafico = "["
    lista = {
        "label": "Menos de $100",
        "data": contador_menos_100 / total,
        "color": colores[0]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Entre $100 y $200",
        "data": contador_entre_100_200 / total,
        "color": colores[1]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Entre $200 y $300",
        "data": contador_entre_200_300 / total,
        "color": colores[2]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Entre $300 y $400",
        "data": contador_entre_300_400 / total,
        "color": colores[3]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Entre $400 y 500",
        "data": contador_entre_400_500 / total,
        "color": colores[4]
    }
    y = json.dumps(lista)
    grafico += y + ","
    lista = {
        "label": "Mayores a 500",
        "data": contador_mayores_500 / total,
        "color": colores[5]
    }
    y = json.dumps(lista)
    grafico += y
    grafico += "]"
    return grafico


def calcular_reporte_ventas_semanal():
    cursor.execute(
        "SELECT  DATE_FORMAT(fecha, '%Y-%m-%d') AS FECHA, SUM(CELULARES.precio_celular*DETALLE_VENTA.cantidad) AS "
        "TOTAL FROM    VENTAS, DETALLE_VENTA, CELULARES WHERE   fecha BETWEEN CURDATE() - INTERVAL 6 DAY AND CURDATE("
        ") + 1 AND VENTAS.codigo_venta = DETALLE_VENTA.codigo_venta AND DETALLE_VENTA.id_celular = "
        "CELULARES.id_celular GROUP BY FECHA ORDER BY `FECHA` ASC")
    data = cursor.fetchall()
    current_date = date.today()
    fechas = [1, 2, 3, 4, 5, 6, 7]
    for i in range(7):
        fechas[i] = str(current_date - timedelta(days=i))
    fechas.reverse()

    totales = [1, 2, 3, 4, 5, 6, 7]
    for i, x in enumerate(fechas):
        totales[i] = 0
        for y in data:
            if x == y[0]:
                totales[i] = str(y[1])
                break
    plantilla = '[{"fechas": '
    plantilla += str(fechas)
    plantilla += ',"data": '
    plantilla += str(totales)
    plantilla += '}]'
    plantilla = plantilla.replace("'", '"')
    return plantilla


def calcular_reporte_ventas_mensual():
    current_year = date.today().year
    anios = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    info = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i, x in enumerate(anios):
        cursor.execute(
            "SELECT SUM(CELULARES.precio_celular) FROM VENTAS, DETALLE_VENTA, CELULARES WHERE VENTAS.codigo_venta = "
            f"DETALLE_VENTA.codigo_venta AND DETALLE_VENTA.id_celular = CELULARES.id_celular AND MONTH(fecha) = {x} AND "
            f"YEAR(fecha) = {current_year}")
        data = cursor.fetchone()
        if data[0] is None:
            info[i] = '0'
        else:
            info[i] = str(data[0])
    plantilla = '[{"totales": '
    plantilla += str(info)
    plantilla += '}]'
    plantilla = plantilla.replace("'", '"')
    print(plantilla)
    return plantilla


# WEB APLICATION
validar = False


@app.route('/', methods=['GET', 'POST'])
def index():
    global validar
    validar = False
    texto = "Cuenca"
    if request.method == "POST":
        usuario = request.form['cedula']
        password = request.form['password']
        data = comprobar_usuario(usuario, password)
        if data is None:
            return render_template("index.html", error="Con_error")
        else:
            validar = True
            return redirect(url_for('dashboard'))
    return render_template("index.html", error="Sin_error")


@app.route('/dashboard')
def dashboard():
    texto = "Cuenca"
    print(validar)
    if not validar:
        return redirect(url_for('.index'))
    else:
        return render_template("dashboard.html", texto=texto, g1=calcular_marca_mas_vendido(),
                               g2=calcular_rango_celulares_mas_vendido(), g3=calcular_reporte_ventas_semanal(),
                               g4=calcular_reporte_ventas_mensual()
                               )


@app.route('/logout')
def logout():
    global validar
    validar = False
    return redirect(url_for('.index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)
