#LIBRERÍA PARA MEJORAR EL ESTILO DEL UI
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from config.app import App
from controller.funtion import *
from controller.report import *


def menu(app:App):
    console=Console()
    while True:
        menu_text=Text()
        menu_text.append("\n📊 Proyecto Datux\n", style="underline bold cyan")
        menu_text.append("\n[1] 🟢 Ingresar Data\n", style="green")
        menu_text.append("[2] 📈 Reporte de Ventas\n", style="blue")
        menu_text.append("[3] ❌ Salir\n", style="red")
       
        console.print(Panel(menu_text, title="[bold magenta]Menu Principal[/bold magenta]",expand=False,border_style="yellow"))
        opcion=Prompt.ask("[bold yellow]Selecciona una opcion-> [/bold yellow]", choices=["1","2","3"],default="3")

        if opcion =="1":
            IngestDataProducts(app)
            pass
        elif opcion=="2":
            GenerateReportVentas(app)
            GenerateReportClientes(app)
            pass
        elif opcion=="3":
            pass
            break
        else: 
            print("Opción no reconocida")
