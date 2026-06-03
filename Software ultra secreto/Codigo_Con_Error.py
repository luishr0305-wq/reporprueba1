# inventario.py

def actualizar_stock(actual, vendido):
    # ERROR: Permite stock negativo, lo cual es una falla lógica
    resultado = actual - vendido
    return resultado

# Prueba de falla
print(f"Stock restante: {actualizar_stock(5, 10)}")