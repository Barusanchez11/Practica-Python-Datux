from config.app import *
from modelos.model import *
import pandas as pd

def IngestDataProducts(app: App):
    bd = app.bd
    conn = bd.getConection()

    dataPais = GetDataSourcePais()
    CreateTablesPais(conn)
    InsertDataPais(bd, dataPais)

    dataPostalCode = GetDataSourcePostalCode()
    CreateTablePostalCode(conn)
    InsertDataPostalCode(bd, dataPostalCode)

    dataCategories = GetDataSourceCategories()
    createTableCategories(conn)
    InsertManyCategories(bd, dataCategories)

    dataProducts = GetDataSourceProductos(conn)
    createTableProducts(conn)
    InsertManyProducts(bd, dataProducts)

    dataClientes = GetDataSourceClientes()
    createTableClientes(conn)
    InsertManyClientes(bd, dataClientes)

    dataVentas = GetDatasourceOrders(conn)
    createTableVentas(conn)
    insertManyVentas(bd, dataVentas)



def GetDataSourcePais():
    pathData="/workspaces/Practica-Python-Datux/Practica_3_PROYECTO/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    print(df.shape)
    print(df.keys())
    df_country=df['Country'].unique()
    print(df_country.shape)
    country_tuples = [(country,) for country in df_country] # hacer una lista de tuplas simplificado
    return country_tuples

def CreateTablesPais(conn:Connection):
    pais=Pais()
    pais.create_table(conn)
    
def InsertDataPais(bd:Database,data):
    bd.insert_many('PAIS',['name'],data)


def GetDataSourcePostalCode():
    pathData="/workspaces/Practica-Python-Datux/Practica_3_PROYECTO/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df['Postal Code'] = df['Postal Code'].astype(str)
    df_postalCode=df[['Postal Code','Country','State']]
    df_postalCode=df_postalCode.dropna()
    df_postalCode=df_postalCode.drop_duplicates()

    print(df_postalCode.head())
    postal_code_tuples=[tuple(x) for x in df_postalCode.to_records(index=False)]
    return postal_code_tuples

def CreateTablePostalCode(conn:Connection):
    postalCode=PostalCode()
    postalCode.create_table(conn)

def InsertDataPostalCode(bd:Database,data):
    bd.insert_many('POSTALCODE',['code','pais','state'],data)

def GetDataSourceCategories():
    pathData="/workspaces/Practica-Python-Datux/Practica_3_PROYECTO/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df_categories=df[['Category','Sub-Category']].dropna().drop_duplicates()
    categories_tuples=[tuple(x) for x in df_categories.to_records(index=False)]
    return categories_tuples

def createTableCategories(conn:Connection):
    categories=Categorias()
    categories.create_table(conn)

def InsertManyCategories(bd:Database,data):
    bd.insert_many('CATEGORIAS',['name','subcategory'],data)


def GetDataSourceProductos(conn):
    pathData="/workspaces/Practica-Python-Datux/Practica_3_PROYECTO/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df_products=df[['Product ID','Product Name','Category']].dropna().drop_duplicates()
    df_categoria=pd.read_sql_query("SELECT id,name FROM CATEGORIAS",conn)
    #df_newProducts=df_products.merge(df_categoria,how="left",left_on='Category',right_on='name')
    #print(df_newProducts.head())
    df_newProducts=df_products.merge(df_categoria,how="left",left_on='Category',right_on='name')
    df_newProducts=df_newProducts[['Product ID','Product Name','id']]
    df_newProducts=[tuple(x) for x in df_newProducts.to_records(index=False)]
    return df_newProducts

def createTableProducts(conn:Connection):
    productos=Productos()
    productos.create_table(conn)

def InsertManyProducts(bd:Database,data):
    bd.insert_many('PRODUCTOS',['product_id','name','category_id'],data)


def GetDatasourceOrders(conn):
    pathData = "/workspaces/Practica-Python-Datux/Practica_3_PROYECTO/files/datafuente.xls"
    df = pd.read_excel(pathData, sheet_name="Orders")

    df_products = pd.read_sql_query("SELECT id as id_product, name, product_id FROM PRODUCTOS", conn)
    df_clients = pd.read_sql_query("SELECT id as id_client, customer_id FROM CLIENTES", conn)

    df_orders = df[['Order ID', 'Customer ID', 'Postal Code', 'Product ID', 'Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost', 'Order Priority']].dropna().drop_duplicates()
    df_orders['Postal Code'] = df_orders['Postal Code'].astype(str)

    df_newOrders = df_orders.merge(df_products, how="left", left_on="Product ID", right_on="product_id")
    df_newOrders = df_newOrders.merge(df_clients, how="left", left_on="Customer ID", right_on="customer_id")

    df_newOrders = df_newOrders[['Order ID', 'Postal Code', 'id_client', 'id_product', 'Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost', 'Order Priority']]
    
    list_tuples = [tuple(x) for x in df_newOrders.to_records(index=False)]
    
    return list_tuples


def createTableVentas(conn):
    ventas=Ventas()
    ventas.create_table(conn)

def insertManyVentas(bd:Database,data):
    bd.insert_many('VENTAS',['order_id','postal_code','customer_id','product_id','sales_amount','quantity','discount','profit','shipping_cost','order_priority'],data)

def GetDataSourceClientes():
    pathData="/workspaces/Practica-Python-Datux/Practica_3_PROYECTO/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    
    #Selección de columnas y eliminando duplicados: 
    df_clientes=df[['Customer ID','Customer Name','Segment','Country','Region']].dropna().drop_duplicates()

    #conviertiendo en tuplas:
    clientes_tuples=[tuple(x) for x in df_clientes.to_records(index=False)]
    return clientes_tuples

def createTableClientes(conn:Connection):
    clientes=Clientes()
    clientes.create_table(conn)

def InsertManyClientes(bd:Database, data):
    bd.insert_many('Clientes',['customer_id','name','segment','country','region'],data)
