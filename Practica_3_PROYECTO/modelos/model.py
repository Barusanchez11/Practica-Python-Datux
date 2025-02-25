from sqlite3 import Connection

class Pais: 
    """ Tabla ID Name"""
    def create_table(self, conn:Connection):
        query="""
                CREATE TABLE IF NOT EXISTS PAIS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50) NOT NULL
                );
            """
        cursor=conn.cursor()
        cursor.execute(query)
        conn.commit()

class PostalCode:
    """ Tabla CODIGO POSTAL: id, code, pais, ciudad  y estado """ 
    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS POSTALCODE (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code VARCHAR(50) NOT NULL,
                pais VARCHAR(50) NOT NULL,
                state VARCHAR(50) NOT NULL
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()

class Categorias:
    """ Tabla CATEGORIAS: id, name, subcategory """

    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS CATEGORIAS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                subcategory VARCHAR(50) NOT NULL
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()

class Productos:
    """ Tabla PRODUCTOS: id, name, product_id, subcategory_id """

    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS PRODUCTOS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(50) NOT NULL,
                product_id INTEGER NOT NULL,
                category_id INTEGER NOT NULL
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()

class Ventas:
    """ Tabla VENTAS con múltiples relaciones """

    def create_table(self, con: Connection):
        query = """
            CREATE TABLE IF NOT EXISTS VENTAS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id VARCHAR(20) NOT NULL,
                postal_code VARCHAR(20),
                product_id INTEGER NOT NULL,
                customer_id VARCHAR(50) NOT NULL,
                sales_amount REAL NOT NULL,
                quantity INTEGER NOT NULL,
                discount REAL NOT NULL,
                profit REAL NOT NULL,
                shipping_cost REAL NOT NULL,
                order_priority VARCHAR(20) NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES CLIENTES (customer_id)
            );
        """
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()

# Agregar una clase catálogo
class Clientes:
    """Tabla CLIETNES: id, customer_id, name, segment, country, region"""
    def create_table(self, con:Connection):
        query="""
                CREATE TABLE IF NOT EXISTS CLIENTES (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id VARCHAR(50) NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    segment VARCHAR(50),
                    country VARCHAR(50),
                    region VARCHAR(50)
                );
            """
        cursor=con.cursor()
        cursor.execute(query)
        con.commit()