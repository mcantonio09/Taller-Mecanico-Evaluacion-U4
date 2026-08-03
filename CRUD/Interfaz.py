import sys
import os

# 1. Obtenemos la ruta absoluta de la carpeta principal del proyecto (un nivel arriba de /CRUD)
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 2. Agregamos esa ruta al "Path" del sistema para que Python busque ahí
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

# 3. Ahora sí, importamos desde la carpeta 'exceptions' el archivo 'excepciones.py'
from exceptions.excepciones import CostoInvalidoError, ServicioNoEncontradoError

import tkinter as tk
from tkinter import ttk, messagebox
from ControladorServicios import ControladorServicios

class InterfazTkinter:
    """
    Clase responsable de la Vista (GUI).
    Interactúa exclusivamente con el ControladorServicios.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Taller Mecánico")
        self.root.geometry("750x500")
        
        # Instanciamos el controlador
        self.controlador = ControladorServicios()
        self.id_seleccionado = None

        self._crear_widgets()
        self._configurar_tabla()
        self.cargar_datos()

    def _crear_widgets(self):
        # Marco de entrada de datos
        frame_inputs = ttk.LabelFrame(self.root, text="Datos del Servicio", padding=10)
        frame_inputs.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_inputs, text="Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_cliente = ttk.Entry(frame_inputs, width=30)
        self.entry_cliente.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_inputs, text="Vehículo:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_vehiculo = ttk.Entry(frame_inputs, width=30)
        self.entry_vehiculo.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_inputs, text="Tipo de Servicio:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_tipo = ttk.Entry(frame_inputs, width=30)
        self.entry_tipo.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_inputs, text="Costo ($):").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_costo = ttk.Entry(frame_inputs, width=30)
        self.entry_costo.grid(row=1, column=3, padx=5, pady=5)

        # Marco de botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_botones, text="Registrar", command=self.registrar).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Actualizar", command=self.actualizar).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Limpiar Campos", command=self.limpiar_campos).pack(side="right", padx=5)

    def _configurar_tabla(self):
        # Configuración del Treeview (Tabla)
        columnas = ("ID", "Cliente", "Vehículo", "Servicio", "Costo")
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings")
        
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=120, anchor="center")
            
        self.tabla.column("ID", width=50) # Columna ID más pequeña
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Evento al hacer clic en una fila
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)

    def cargar_datos(self):
        """Limpia la tabla y la vuelve a llenar con los datos de la BD."""
        # Limpiar registros actuales
        for row in self.tabla.get_children():
            self.tabla.delete(row)
            
        # Solicitar datos al controlador
        servicios = self.controlador.obtener_servicios()
        for s in servicios:
            self.tabla.insert("", "end", values=(s.id_servicio, s.cliente, s.vehiculo, s.tipo_servicio, s.costo))

    def registrar(self):
        """Intenta registrar un servicio capturando posibles errores de negocio."""
        try:
            # Aquí aplicamos manejo de excepciones en la capa visual
            self.controlador.registrar_servicio(
                self.entry_cliente.get(),
                self.entry_vehiculo.get(),
                self.entry_tipo.get(),
                self.entry_costo.get()
            )
            messagebox.showinfo("Éxito", "Servicio registrado correctamente.")
            self.cargar_datos()
            self.limpiar_campos()
            
        except CostoInvalidoError as e:
            messagebox.showerror("Error de Validación", str(e))
        except ValueError as e:
            messagebox.showerror("Error de Entrada", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

    def seleccionar_fila(self, event):
        """Rellena los Entry con los datos de la fila seleccionada."""
        item_seleccionado = self.tabla.focus()
        if item_seleccionado:
            valores = self.tabla.item(item_seleccionado, 'values')
            self.id_seleccionado = valores[0]
            
            self.limpiar_campos()
            self.entry_cliente.insert(0, valores[1])
            self.entry_vehiculo.insert(0, valores[2])
            self.entry_tipo.insert(0, valores[3])
            self.entry_costo.insert(0, valores[4])

    def actualizar(self):
        if not self.id_seleccionado:
            messagebox.showwarning("Atención", "Seleccione un servicio de la tabla para actualizar.")
            return

        try:
            self.controlador.actualizar_servicio(
                self.id_seleccionado,
                self.entry_cliente.get(),
                self.entry_vehiculo.get(),
                self.entry_tipo.get(),
                self.entry_costo.get()
            )
            messagebox.showinfo("Éxito", "Servicio actualizado.")
            self.cargar_datos()
            self.limpiar_campos()
            
        except CostoInvalidoError as e:
            messagebox.showerror("Error de Validación", str(e))
        except ServicioNoEncontradoError as e:
            messagebox.showerror("Error de Base de Datos", str(e))

    def eliminar(self):
        if not self.id_seleccionado:
            messagebox.showwarning("Atención", "Seleccione un servicio para eliminar.")
            return
            
        confirmacion = messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar este registro?")
        if confirmacion:
            try:
                self.controlador.eliminar_servicio(self.id_seleccionado)
                messagebox.showinfo("Éxito", "Servicio eliminado.")
                self.cargar_datos()
                self.limpiar_campos()
            except ServicioNoEncontradoError as e:
                messagebox.showerror("Error", str(e))

    def limpiar_campos(self):
        self.id_seleccionado = None
        self.entry_cliente.delete(0, tk.END)
        self.entry_vehiculo.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.entry_costo.delete(0, tk.END)