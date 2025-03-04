from tkinter import ttk
import customtkinter as ctk
import pymysql

conexion = pymysql.connect(host='localhost', user = 'root', passwd = '', db='ferreteria')
cur = conexion.cursor()

def mostrar_listar_cantidad():
    
    ventana_listar = ctk.CTkToplevel()
    ventana_listar.title("Listar ventas por cantidad")
    ventana_listar.geometry("600x600")
    ventana_listar.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_listar, text="Lista de Ventas - Orden por cantidad de productos", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_tabla = ctk.CTkFrame(ventana_listar)
    frame_tabla.pack(pady=20, padx=20, fill="both", expand=True)
    
    columnas = ("Código", "Nombre", "Cantidad", "Fecha de venta", "Precio total")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor="center")
        
        sql = "SELECT p.CodigoProducto, q.NombreProducto, p.Cantidad, p.FechaVenta, p.Total FROM venta p JOIN producto q ON p.CodigoProducto = q.CodigoProducto ORDER BY p.Cantidad ASC"
        cur.execute(sql)
        
        ventas = cur.fetchall()
        
    for venta in ventas:
        tabla.insert("", "end", values=venta)

    tabla.pack(fill="both", expand=True)

    boton_cerrar = ctk.CTkButton(
        ventana_listar, 
        text="Cerrar", 
        command=ventana_listar.destroy,
        width=150,
        height=40,
        fg_color="Red",
        text_color="white",
        hover_color="Darkred",
        corner_radius=10
    )
    boton_cerrar.pack(pady=10)

def mostrar_listar_nombre():
    
    ventana_listar = ctk.CTkToplevel()
    ventana_listar.title("Listar ventas por nombre")
    ventana_listar.geometry("600x600")
    ventana_listar.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_listar, text="Lista de Ventas - Orden por nombre de producto", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_tabla = ctk.CTkFrame(ventana_listar)
    frame_tabla.pack(pady=20, padx=20, fill="both", expand=True)
    
    columnas = ("Código", "Nombre", "Cantidad", "Fecha de venta", "Precio total")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor="center")
        
    sql = "SELECT p.CodigoProducto, q.NombreProducto, p.Cantidad, p.FechaVenta, p.Total FROM venta p JOIN producto q ON p.CodigoProducto = q.CodigoProducto ORDER BY q.NombreProducto ASC"
    cur.execute(sql)
        
    ventas = cur.fetchall()
        
    for venta in ventas:
        tabla.insert("", "end", values=venta)

    tabla.pack(fill="both", expand=True)

    boton_cerrar = ctk.CTkButton(
        ventana_listar, 
        text="Cerrar", 
        command=ventana_listar.destroy,
        width=150,
        height=40,
        fg_color="Red",
        text_color="white",
        hover_color="Darkred",
        corner_radius=10
    )
    boton_cerrar.pack(pady=10)

def mostrar_listar_codigo():
    
    ventana_listar = ctk.CTkToplevel()
    ventana_listar.title("Listar ventas por nombre")
    ventana_listar.geometry("600x600")
    ventana_listar.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_listar, text="Lista de Ventas - Orden por nombre de producto", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_tabla = ctk.CTkFrame(ventana_listar)
    frame_tabla.pack(pady=20, padx=20, fill="both", expand=True)
    
    columnas = ("Código", "Nombre", "Cantidad", "Fecha de venta", "Precio total")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor="center")
        
    sql = "SELECT p.CodigoProducto, q.NombreProducto, p.Cantidad, p.FechaVenta, p.Total FROM venta p JOIN producto q ON p.CodigoProducto = q.CodigoProducto ORDER BY p.CodigoProducto ASC"
    cur.execute(sql)
        
    ventas = cur.fetchall()
        
    for venta in ventas:
        tabla.insert("", "end", values=venta)

    tabla.pack(fill="both", expand=True)

    boton_cerrar = ctk.CTkButton(
        ventana_listar, 
        text="Cerrar", 
        command=ventana_listar.destroy,
        width=150,
        height=40,
        fg_color="Red",
        text_color="white",
        hover_color="Darkred",
        corner_radius=10
    )
    boton_cerrar.pack(pady=10)


