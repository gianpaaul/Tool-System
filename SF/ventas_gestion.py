from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import pymysql

conexion = pymysql.connect(host='localhost', user = 'root', passwd = '', db='ferreteria')
cur = conexion.cursor()

def mostrar_agregar_venta():
    
    ventana_agregar = ctk.CTkToplevel()
    ventana_agregar.title("Agregar venta")
    ventana_agregar.geometry("500x400")
    ventana_agregar.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_agregar, text="Agregar nueva venta", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_agregar = ctk.CTkFrame(ventana_agregar)
    frame_agregar.pack(pady=20)
    
    codigo = ctk.CTkLabel(frame_agregar, text="Código de producto:", font=("Arial", 16))
    codigo.grid(row=0, column=0, padx=10, pady=5, sticky="w") 
    Obtener_codigo = ctk.CTkEntry(frame_agregar, width=100)
    Obtener_codigo.grid(row=0, column=1, padx=10, pady=5)
    
    cantidad = ctk.CTkLabel(frame_agregar, text="Cantidad:", font=("Arial", 16))
    cantidad.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Obtener_cantidad = ctk.CTkEntry(frame_agregar, width=100)
    Obtener_cantidad.grid(row=1, column=1, padx=10, pady=5)
    
    fecha = ctk.CTkLabel(frame_agregar, text="Fecha:", font=("Arial", 16))
    fecha.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Obtener_fecha = ctk.CTkEntry(frame_agregar, width=100)
    Obtener_fecha.grid(row=2, column=1, padx=10, pady=5)
 
    def agregar():
        try:
            codigo = Obtener_codigo.get()
            cantidad = Obtener_cantidad.get()
            fecha = Obtener_fecha.get()
            cantidad = int(cantidad) 
            cur.execute("SELECT Precio, Stock FROM producto WHERE CodigoProducto = %s", (codigo,))
            producto = cur.fetchone()  
            if producto: 
                precio_producto = int(producto[0])  
                stock_producto = int(producto[1])  
                if stock_producto != 0 and stock_producto - cantidad >= 0:
                    total = cantidad * precio_producto
                    sql = "INSERT INTO venta (CodigoProducto, Cantidad, FechaVenta, Total) VALUES (%s, %s, %s, %s)"
                    venta = (codigo, cantidad, fecha, total)
                    cur.execute(sql, venta)
                    conexion.commit()
                    sql = "UPDATE producto SET Stock = %s WHERE CodigoProducto = %s"
                    nuevo_stock = stock_producto - cantidad
                    cur.execute(sql, (nuevo_stock, codigo))
                    conexion.commit()
                    messagebox.showinfo("Mensaje", "La venta se registró correctamente")
                else:
                    messagebox.showwarning("Advertencia", "¡No se puede realizar la venta, el stock está agotado o no es lo suficiente!")
            else:
                messagebox.showwarning("Advertencia", "¡Producto no encontrado!")
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero válido.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
  
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
    
def mostrar_eliminar_venta():
    
    ventana_eliminar = ctk.CTkToplevel()
    ventana_eliminar.title("Eliminar venta")
    ventana_eliminar.geometry("500x400")
    ventana_eliminar.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_eliminar, text="Eliminar venta", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_eliminar = ctk.CTkFrame(ventana_eliminar)
    frame_eliminar.pack(pady=20)
    
    codigo = ctk.CTkLabel(frame_eliminar, text="ID de la venta:", font=("Arial", 16))
    codigo.grid(row=0, column=0, padx=10, pady=5, sticky="w") 
    Obtener_codigo = ctk.CTkEntry(frame_eliminar, width=100)
    Obtener_codigo.grid(row=0, column=1, padx=10, pady=5)

    def eliminar():
        
        id_venta = Obtener_codigo.get()
        
        cur.execute("SELECT q.CodigoProducto, p.Cantidad, q.Stock FROM venta p JOIN producto q ON p.CodigoProducto = q.CodigoProducto WHERE IdVenta = "+id_venta)
        venta = cur.fetchone()
        codigo = venta[0]
        cantidad = int(venta[1])
        stock = int(venta[2])
        nuevo_stock = stock + cantidad
            
        sql = "UPDATE producto SET Stock = %s WHERE CodigoProducto = %s"
        valores = (nuevo_stock, codigo)
        cur.execute(sql, valores)
        conexion.commit()
            
        sql = "DELETE FROM venta WHERE IdVenta = %s"
        valores = (id_venta,)
        cur.execute(sql, valores)
        conexion.commit()
        
        messagebox.showinfo("Mensaje", "La venta se eliminó correctamente")
        
        
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
    
def mostrar_listar_venta():
    
    ventana_listar = ctk.CTkToplevel()
    ventana_listar.title("Listar Ventas")
    ventana_listar.geometry("500x500")
    ventana_listar.resizable(False, False)
    
    titulo = ctk.CTkLabel(ventana_listar, text="Lista de Ventas", font=("Arial", 22))
    titulo.pack(pady=20)
    
    frame_tabla = ctk.CTkFrame(ventana_listar)
    frame_tabla.pack(pady=20, padx=20, fill="both", expand=True)
    
    columnas = ("ID", "Código del producto", "Cantidad", "Fecha", "Total")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100, anchor="center")
        
    sql = "SELECT * FROM venta"
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
