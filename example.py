from TableConsole import Table

a = Table()
a.addColumn("ID", 5)
a.addColumn("ARTICULO", 30)
a.addColumn("MONEDA", 6)
a.addColumn("PRECIO", 10)

# Primer fila
a.addRow(["1256", "Televisor LED", "USD", "800"])
# Segunda fila
a.addRow(["1257", "Heladera", "USD", "950"])
# Tercera fila
a.addRow(["1258", "Computadora", "USD", "450"])
a.make()
