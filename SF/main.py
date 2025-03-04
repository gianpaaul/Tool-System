import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import time
import threading
import pymysql
import productos_gestion
import ventas_ordenar
import ventas_gestion

# Conexión con la base de datos MySQL 
conexion = pymysql.connect(host='localhost', user = 'root', passwd = '', db='ferreteria')
cur = conexion.cursor()

# Menú principal
app = ctk.CTk()
app.title("Sistema de Ferretería")
app.geometry("550x300")
app.resizable(False, False)

titulo = ctk.CTkLabel(app, text="Sistema de Ferretería", font=("Arial", 25))
titulo.pack(pady=40)

def ejecutar_con_hilo(funcion):
    def ejecucion():
        inicio = time.time()
        funcion()
        fin = time.time()
        messagebox.showinfo("Mensaje", f"Tiempo de ejecución: {fin - inicio} segundos")
    
    hilo = threading.Thread(target=ejecucion)
    hilo.start()
    
def mostrar_menu_producto():
    # Menu de gestión de prodcutos
    app.withdraw()
    ventana_producto = ctk.CTkToplevel(app)
    ventana_producto.title("Gestionar Productos")
    ventana_producto.geometry("500x400")
    ventana_producto.resizable(False, False)
    
    label_titulo = ctk.CTkLabel(ventana_producto, text="Gestión de productos", font=("Arial", 25))
    label_titulo.pack(pady=20)
    
    frame_producto = ctk.CTkFrame(ventana_producto)
    frame_producto.pack(pady=20)
    
    agregar_producto = ctk.CTkButton(
    master=frame_producto,
    text="Agregar producto",
    command=lambda:ejecutar_con_hilo(productos_gestion.mostrar_agregar_producto),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    agregar_producto.pack(side="top", padx=10, pady=5)
    
    eliminar_producto = ctk.CTkButton(
    master=frame_producto,
    text="Eliminar producto",
    command=lambda:ejecutar_con_hilo(productos_gestion.mostrar_eliminar_producto),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    eliminar_producto.pack(side="top", padx=10, pady=5)
    
    listar_productos = ctk.CTkButton(
    master=frame_producto,
    text="Listar productos",
    command=lambda:ejecutar_con_hilo(productos_gestion.mostrar_listar_producto),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    listar_productos.pack(side="top", padx=10, pady=5)
    
    actualizar_stock = ctk.CTkButton(
    master=frame_producto,
    text="Actualizar stock",
    command=lambda:ejecutar_con_hilo(productos_gestion.mostrar_actualizar_stock),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    actualizar_stock.pack(side="top", padx=10, pady=5)
    
    def cerrar_y_mostrar(ventana_nueva, ventana_anterior):
       ventana_nueva.destroy()
       ventana_anterior.deiconify()

    boton_cerrar = ctk.CTkButton(
    ventana_producto, 
    text="Cerrar", 
    command=lambda:cerrar_y_mostrar(ventana_producto, app),
    width=150,
    height=40,
    fg_color="Red",
    text_color="white",
    hover_color="Darkred",
    corner_radius=10
    )
    boton_cerrar.pack(pady=10)

def mostrar_menu_venta():
    # Menú de gestión de ventas
    app.withdraw()
    ventana_venta = ctk.CTkToplevel(app)
    ventana_venta.title("Gestionar Ventas")
    ventana_venta.geometry("500x400")
    ventana_venta.resizable(False, False)
    
    label_titulo = ctk.CTkLabel(ventana_venta, text="Gestión de ventas", font=("Arial", 25))
    label_titulo.pack(pady=20)
    
    frame_venta = ctk.CTkFrame(ventana_venta)
    frame_venta.pack(pady=20)
    
    registrar_venta = ctk.CTkButton(
    master=frame_venta,
    text="Rgistrar nueva venta",
    command=lambda:ejecutar_con_hilo(ventas_gestion.mostrar_agregar_venta),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    registrar_venta.pack(side="top", padx=10, pady=5)
    
    eliminar_venta = ctk.CTkButton(
    master=frame_venta,
    text="Eliminar venta",
    command=lambda:ejecutar_con_hilo(ventas_gestion.mostrar_eliminar_venta),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    eliminar_venta.pack(side="top", padx=10, pady=5)
    
    listar_ventas = ctk.CTkButton(
    master=frame_venta,
    text="Listar ventas",
    command=lambda:ejecutar_con_hilo(ventas_gestion.mostrar_listar_venta),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    listar_ventas.pack(side="top", padx=10, pady=5)
    
    def cerrar_y_mostrar(ventana_nueva, ventana_anterior):
       ventana_nueva.destroy()
       ventana_anterior.deiconify()
       
    boton_cerrar = ctk.CTkButton(
    ventana_venta, 
    text="Cerrar", 
    command=lambda:cerrar_y_mostrar(ventana_venta, app),
    width=150,
    height=40,
    fg_color="Red",
    text_color="white",
    hover_color="Darkred",
    corner_radius=10
    )
    boton_cerrar.pack(pady=10)

def mostrar_menu_ordenar():
    # Menú de ordenar de ventas
    app.withdraw()
    ventana_ordenar = ctk.CTkToplevel(app)
    ventana_ordenar.title("Ordenar ventas realizadas")
    ventana_ordenar.geometry("500x400")
    ventana_ordenar.resizable(False, False)
    
    label_titulo = ctk.CTkLabel(ventana_ordenar, text="Ordenar ventas", font=("Arial", 25))
    label_titulo.pack(pady=20)
    
    frame_ordenar = ctk.CTkFrame(ventana_ordenar)
    frame_ordenar.pack(pady=20)
    
    listar_cantidad = ctk.CTkButton(
    master=frame_ordenar,
    text="Ordenar por cantidad de las ventas realizadas",
    command=lambda:ejecutar_con_hilo(ventas_ordenar.mostrar_listar_cantidad),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    listar_cantidad.pack(side="top", padx=10, pady=5)
    
    listar_nombre = ctk.CTkButton(
    master=frame_ordenar,
    text="Ordenar alfabéticamente por nombre del producto",
    command=lambda:ejecutar_con_hilo(ventas_ordenar.mostrar_listar_nombre),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    listar_nombre.pack(side="top", padx=10, pady=5)
    
    listar_codigo = ctk.CTkButton(
    master=frame_ordenar,
    text="Ordenar por código del producto",
    command=lambda:ejecutar_con_hilo(ventas_ordenar.mostrar_listar_codigo),
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
    )
    listar_codigo.pack(side="top", padx=10, pady=5)
    
    def cerrar_y_mostrar(ventana_nueva, ventana_anterior):
       ventana_nueva.destroy()
       ventana_anterior.deiconify()
    
    boton_cerrar = ctk.CTkButton(
    ventana_ordenar, 
    text="Cerrar", 
    command=lambda:cerrar_y_mostrar(ventana_ordenar, app),
    width=150,
    height=40,
    fg_color="Red",
    text_color="white",
    hover_color="Darkred",
    corner_radius=10
    )
    boton_cerrar.pack(pady=10)

frame_botones = ctk.CTkFrame(app)
frame_botones.pack(pady=20)

button_productos = ctk.CTkButton(
    master=frame_botones,
    text="Gestionar Productos",
    command=mostrar_menu_producto,
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
)
button_productos.pack(side="left", padx=10)

button_ventas = ctk.CTkButton(
    master=frame_botones,
    text="Gestionar Ventas",
    command=mostrar_menu_venta,
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
)
button_ventas.pack(side="left", padx=10)

button_ordenar = ctk.CTkButton(
    master=frame_botones,
    text="Ordenar Ventas",
    command=mostrar_menu_ordenar,
    width=150,
    height=40,
    fg_color="blue",
    text_color="white",
    hover_color="green",
    corner_radius=10
)
button_ordenar.pack(side="left", padx=10)

button_salir = ctk.CTkButton(
    master=app,
    text="Salir",
    command=app.destroy,
    width=150,
    height=40,
    fg_color="red",
    text_color="white",
    hover_color="darkred",
    corner_radius=10
)
button_salir.pack(pady=20)

app.mainloop()
