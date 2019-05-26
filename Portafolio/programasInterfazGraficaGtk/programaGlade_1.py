import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def imprimir(button):
    etiqueta = Constructor.get_object("label1")
    etiqueta.set_text("Hola Mundo")


def borrar(button):
    etiqueta = Constructor.get_object("label1")
    etiqueta.set_text("")


Constructor = Gtk.Builder()
Constructor.add_from_file("programa_1.glade")

handlers = {
    "evento_salir": Gtk.main_quit,
    "evento_imprimir": imprimir,
    "evento_borrar": borrar
}


Constructor.connect_signals(handlers)
ventana = Constructor.get_object("ventana_principal")
ventana.show_all()
Gtk.main()
