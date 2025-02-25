from config.app import *
import pandas as pd

 
def GenerateReportVentas(app:App):
    conn=app.bd.getConection()
    query="""
        SELECT 
            p.pais,
            v.product_id,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE p
        ON 
            v.postal_code = p.code
        GROUP BY 
            p.pais, v.product_id
        ORDER BY 
            total_vendido DESC;
    """
    df=pd.read_sql_query(query,conn)
    fecha="08-02"
    path=f"/workspaces/Practica-Python-Datux/Practica_3_PROYECTO/files/reporte-{fecha}.csv"
    df.to_csv(path)
    sendMail(app,path)

#def sendMail(app:App,data):
    # cambiar el asunto 
    #app.mail.send_email('from@example.com','Reporte','Reporte',data)

def GenerateReportClientes(app:App):
    conn=app.bd.getConection()

    query="""
        SELECT
            c.country,
            COUNT(DISTINCT c.customer_id) AS total_clientes,
            c.customer_id,
            SUM(v.sales) AS total_compras,
            COUNT(DISTINCT v.product_id) AS prod_dif_comprados
        FROM CLIENTES c
        JOIN VENTAS v ON c.customer_id =v.customer_id
        GROUP BY c.country, c.customer_id
        ORDER BY total_compras DESC;
        """
    pf=pd.read_sql_query(query, conn)
    fecha='08-02'
    path=f"/workspaces/Practica-Python-Datux/Practica_3_PROYECTO/files/reporte-{fecha}.csv"
    pf.to_csv(path, index=False)
    sendMail(app,path)

def sendMail(app:App,data):
    # cambiar el asunto 
    app.mail.send_email('from@example.com','Reporte Practica 3','Reporte Practica 3',data)