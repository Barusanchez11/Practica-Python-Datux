import sqlite3
from rich.progress import Progress
#Progress es una función de embellecimiento
#de texto

class Database:
    def __init__(self,path:str):
        self.path=path
    
    def initConnection(self):
        try:
            self.conection=sqlite3.connect(self.path)
        except Exception as E:
            print("Error Conection!",E)
    
    def getConection(self):
        if not hasattr(self,'conection'):
            self.initConnection()
        return self.conection

#d1=Database('path.db')#1
#d1.initConnection()
#d1.initConnection()
#d1.initConnection()
#d1.getConection()
#d2=Database('path2.db')#2

    def insert_many(self, table: str, columns: list, data: list):
            if not data:
                print("⚠️ No hay datos para insertar.")
                return

            MAX_BATCH_SIZE = 1000  
            num_batches = (len(data) // MAX_BATCH_SIZE) + 1

            column_names = ", ".join(columns)
            placeholders = ", ".join(["?"] * len(columns))
            query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"

            # Inicializar la barra de progreso
            with Progress() as progress:
                task = progress.add_task(f"[green]Insertando datos en {table}...", total=num_batches)

                # Insertar datos por lotes
                for i in range(num_batches):
                    batch = data[i * MAX_BATCH_SIZE : (i + 1) * MAX_BATCH_SIZE]
                    if batch:
                        cursor = self.conection.cursor()
                        cursor.executemany(query, batch)
                        self.conection.commit()
                    
                    # Avanzar la barra de progreso
                    progress.update(task, advance=1)

            print(f"✅ {len(data)} filas insertadas en '{table}'.")

    def close_connection(self):
        """ Cierra la conexión con la base de datos """
        self.conection.close()