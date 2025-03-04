from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import pymysql

conexion = pymysql.connect(host='localhost', user = 'root', passwd = '', db='ferreteria')
cur = conexion.cursor()

def mostrar_agregar_producto():
    
    ventana_agregar = ctk.CTkToplevel()
    ventana_agregar.title("Agregar producto")
    ventana_agregar.geometry("500x400")
    ventana_agregar.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_agregar, text="Agregar nuevo producto", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_agregar = ctk.CTkFrame(ventana_agregar)
    frame_agregar.pack(pady=20)
    
    Nombre = ctk.CTkLabel(frame_agregar, text="Nombre:", font=("Arial", 16))
    Nombre.grid(row=0, column=0, padx=10, pady=5, sticky="w") 
    Obtener_Nombre = ctk.CTkEntry(frame_agregar, width=300)
    Obtener_Nombre.grid(row=0, column=1, padx=10, pady=5)
    
    Categoria = ctk.CTkLabel(frame_agregar, text="Categoría:", font=("Arial", 16))
    Categoria.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Obtener_Categoria = ctk.CTkEntry(frame_agregar, width=300)
    Obtener_Categoria.grid(row=1, column=1, padx=10, pady=5)
    
    Precio = ctk.CTkLabel(frame_agregar, text="Precio:", font=("Arial", 16))
    Precio.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Obtener_Precio = ctk.CTkEntry(frame_agregar, width=300)
    Obtener_Precio.grid(row=2, column=1, padx=10, pady=5)
    
    Stock = ctk.CTkLabel(frame_agregar, text="Stock:", font=("Arial", 16))
    Stock.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Obtener_Stock = ctk.CTkEntry(frame_agregar, width=300)
    Obtener_Stock.grid(row=3, column=1, padx=10, pady=5)
    
    def agregar():
        nombre = Obtener_Nombre.get()
        categoria = Obtener_Categoria.get()
        precio = Obtener_Precio.get()
        stock = Obtener_Stock.get()
        
        sql = "INSERT INTO producto (NombreProducto, Categoria, Precio, Stock) VALUES (%s, %s, %s, %s)"
        valores = (nombre, categoria, precio, stock)
        cur.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Mensaje", "El producto se registró correctamente")
        
    boton_aceptar = ctk.CTkButton(
        ventana_agregar, 
        text="Aceptar", 
        command=agregar,
        width=150,
        height=40,
        fg_color="Green",
        text_color="white",
        hover_color="Darkgreen",
        corner_radius=10
    )
    boton_aceptar.pack(pady=10)
    
    boton_cerrar = ctk.CTkButton(
        ventana_agregar, 
        text="Cerrar", 
        command=ventana_agregar.destroy,
        width=150,
        height=40,
        fg_color="Red",
        text_color="white",
        hover_color="Darkred",
        corner_radius=10
    )
    boton_cerrar.pack(pady=10)
    
def mostrar_eliminar_producto():
    
    ventana_eliminar = ctk.CTkToplevel()
    ventana_eliminar.title("Eliminar producto")
    ventana_eliminar.geometry("500x400")
    ventana_eliminar.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_eliminar, text="Eliminar producto", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_eliminar = ctk.CTkFrame(ventana_eliminar)
    frame_eliminar.pack(pady=20)
    
    Codigo = ctk.CTkLabel(frame_eliminar, text="Código del producto:", font=("Arial", 16))
    Codigo.grid(row=0, column=0, padx=10, pady=5, sticky="w") 
    Obtener_Codigo = ctk.CTkEntry(frame_eliminar, width=100)
    Obtener_Codigo.grid(row=0, column=1, padx=10, pady=5)

    def eliminar():
        
        cod_producto = Obtener_Codigo.get()
        
        sql = "DELETE FROM producto WHERE CodigoProducto = %s"
        valores = (cod_producto,)
        cur.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Mensaje", "El producto se eliminó correctamente")
        
    boton_aceptar = ctk.CTkButton(
        ventana_eliminar, 
        text="Aceptar", 
        command=eliminar,
        width=150,
        height=40,
        fg_color="Green",
        text_color="white",
        hover_color="Darkgreen",
        corner_radius=10
    )
    boton_aceptar.pack(pady=10)
    
    boton_cerrar = ctk.CTkButton(
        ventana_eliminar, 
        text="Cerrar", 
        command=ventana_eliminar.destroy,
        width=150,
        height=40,
        fg_color="Red",
        text_color="white",
        hover_color="Darkred",
        corner_radius=10
    )
    boton_cerrar.pack(pady=10)
    
def mostrar_listar_producto():
    
    ventana_listar = ctk.CTkToplevel()
    ventana_listar.title("Listar Productos")
    ventana_listar.geometry("500x500")
    ventana_listar.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_listar, text="Lista de Productos", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_tabla = ctk.CTkFrame(ventana_listar)
    frame_tabla.pack(pady=20, padx=20, fill="both", expand=True)
    
    columnas = ("Código", "Nombre", "Categoría", "Precio", "Stock")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor="center")
        
    sql = "SELECT * FROM producto"
    cur.execute(sql)
            
    productos = cur.fetchall()
        
    for producto in productos:
        tabla.insert("", "end", values=producto)

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

def mostrar_actualizar_stock():
    
    ventana_stock = ctk.CTkToplevel()
    ventana_stock.title("Actualizar stock de producto")
    ventana_stock.geometry("500x400")
    ventana_stock.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_stock, text="Actualizar stock de producto", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_stock = ctk.CTkFrame(ventana_stock)
    frame_stock.pack(pady=20)
    
    Codigo = ctk.CTkLabel(frame_stock, text="Código del producto:", font=("Arial", 16))
    Codigo.grid(row=0, column=0, padx=10, pady=5, sticky="w") 
    Obtener_Codigo = ctk.CTkEntry(frame_stock, width=100)
    Obtener_Codigo.grid(row=0, column=1, padx=10, pady=5)
    
    Stock = ctk.CTkLabel(frame_stock, text="Valor del nuevo stock:", font=("Arial", 16))
    Stock.grid(row=1, column=0, padx=10, pady=5, sticky="w") 
    Obtener_Stock = ctk.CTkEntry(frame_stock, width=100)
    Obtener_Stock.grid(row=1, column=1, padx=10, pady=5)

    def actualizar():
        
        cod_producto = Obtener_Codigo.get()
        valor = Obtener_Stock.get()
        
        sql = "UPDATE producto SET Stock = %s WHERE CodigoProducto = %s"
        valores = (valor,cod_producto)
        cur.execute(sql,valores)
        conexion.commit
        messagebox.showinfo("Mensaje", "El actualizó el stock correctamente")
        
    boton_aceptar = ctk.CTkButton(
        ventana_stock, 
        text="Aceptar", 
        command=actualizar,
        width=150,
        height=40,
        fg_color="Green",
        text_color="white",
        hover_color="Darkgreen",
        corner_radius=10
    )
    boton_aceptar.pack(pady=10)
    
    boton_cerrar = ctk.CTkButton(
        ventana_stock, 
        text="Cerrar", 
        command=ventana_stock.destroy,
        width=150,
        height=40,
        fg_color="Red",
        text_color="white",
        hover_color="Darkred",
        corner_radius=10
    )
    boton_cerrar.pack(pady=10)
    
