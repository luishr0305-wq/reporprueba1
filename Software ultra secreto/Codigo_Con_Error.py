# inventario.py

def actualizar_stock(actual, vendido):
    """
    Actualiza el stock asegurando que no sea negativo.
    """
    if vendido < 0:
        raise ValueError("La cantidad vendida no puede ser negativa.")
        
    resultado = actual - vendido
    
    if resultado < 0:
        print("Error: Venta excede el stock disponible.")
        return actual  # Retorna el valor original si no hay stock
    
    return resultado

# Pruebas del código
stock_actual = 5
cantidad_vendida = 10

nuevo_stock = actualizar_stock(stock_actual, cantidad_vendida)
print(f"Stock resultante: {nuevo_stock}")