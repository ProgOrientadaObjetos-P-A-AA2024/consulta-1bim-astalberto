coordenadas_ciudades = {
    "New York": (40.7128, -74.0060),
    "Tokyo": (35.6895, 139.6917),
    "Paris": (48.8566, 2.3522),
    "Sydney": (-33.8688, 151.2093),
    "Rio de Janeiro": (-22.9068, -43.1729)
}

# Mostrar las coordenadas de cada ciudad
for ciudad, coordenadas in coordenadas_ciudades.items():
    latitud, longitud = coordenadas
    print(f"Las coordenadas de {ciudad} son:")
    print(f"Latitud: {latitud}, Longitud: {longitud}")