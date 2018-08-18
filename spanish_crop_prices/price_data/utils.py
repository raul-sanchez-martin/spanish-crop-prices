COOKIES = {'JSESSIONID': '001DD1B6E9B2F1153D65CB770F15BDE9',}

HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://www.lasalina.es',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://www.lasalina.es/Aplicaciones/GestorInter.jsp?prestacion=Lonja&funcion=BusquedaCotizacion',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

REQUEST_DATA = [
    ('prestacion', 'Lonja'),
    ('funcion', 'BusquedaCotizacion'),
    ('valor1', ''),
    ('valor2', ''),
    ('productoStr1', ''),
    ('categoriaStr1', ''),
    ('codigoProducto', ''),
    ('mesa', '0'),
    ('producto', '0'),
    ('categoria', '0'),
]

COLUMNS = [
    "Producto",
    "Categoría",
    "Anterior", 
    "Último",
    "Diferencia",
    "Medida",
    "Tendencia",
    "Fecha"
]