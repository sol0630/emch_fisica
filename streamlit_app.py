import streamlit as st
import random

# Función para generar un ejercicio de cinemática
def generar_ejercicio():
    velocidad_inicial = random.randint(10, 100)  # m/s
    tiempo = random.randint(1, 10)  # segundos
    aceleracion = random.randint(1, 10)  # m/s^2
    
    # Calcular la velocidad final usando la fórmula v = u + a*t
    velocidad_final = velocidad_inicial + aceleracion * tiempo
    
    # Devolver los valores del ejercicio y la respuesta correcta
    return velocidad_inicial, aceleracion, tiempo, velocidad_final

# Generar un ejercicio
st.title('Generador de Ejercicios de Cinemática')
st.write('A continuación se te dará un ejercicio de cinemática, introduce la respuesta para verificar si es correcta.')

# Mostrar el ejercicio en pantalla
velocidad_inicial, aceleracion, tiempo, velocidad_correcta = generar_ejercicio()

st.write(f"Velocidad inicial (u): {velocidad_inicial} m/s")
st.write(f"Aceleración (a): {aceleracion} m/s²")
st.write(f"Tiempo (t): {tiempo} s")

# Input del usuario
respuesta_usuario = st.number_input('Introduce la velocidad final (v) en m/s:', value=0)

# Botón para verificar la respuesta
if st.button('Verificar respuesta'):
    if respuesta_usuario == velocidad_correcta:
        st.success('¡Correcto! La respuesta es correcta.')
    else:
        st.error(f'Incorrecto. La velocidad final correcta es {velocidad_correcta} m/s.')

