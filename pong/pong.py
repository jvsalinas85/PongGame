'''Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para 
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los 
jugadores.También puedes definir una serie de asignaciones de teclas para establecer los 
controles del usuario para las paletas de los jugadores izquierda y derecha

referencia https://realpython.com/beginners-guide-python-turtle/'''

import turtle
import time

# Puntaje inicial de los jugadores
puntaje_izquierda = 0
puntaje_derecha = 0

# Crear objetos para mostrar el puntaje en la ventana
puntaje_display = turtle.Turtle()
puntaje_display.speed(0)
puntaje_display.color("white")
puntaje_display.penup()
puntaje_display.hideturtle()
puntaje_display.goto(0, 260)
puntaje_display.write("Jugador Izquierda: 0  Jugador Derecha: 0", align="center", font=("Courier", 24, "normal"))

# Función para actualizar el puntaje
def actualizar_puntaje():
    puntaje_display.clear()
    puntaje_display.write(f"Jugador Izquierda: {puntaje_izquierda}  Jugador Derecha: {puntaje_derecha}", align="center", font=("Courier", 24, "normal"))


# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)

# Paleta izquierda
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)
paleta_izquierda.shape("square")
paleta_izquierda.color("red")
paleta_izquierda.shapesize(stretch_wid=6, stretch_len=2)
paleta_izquierda.penup()
paleta_izquierda.goto(-350, 0)

# Paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("blue")
paleta_derecha.shapesize(stretch_wid=6, stretch_len=2)
paleta_derecha.penup()
paleta_derecha.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(10)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 6
pelota.dy = -6

# Funciones de movimiento de las paletas
def paleta_izquierda_arriba():
    y = paleta_izquierda.ycor()
    y += 40
    paleta_izquierda.sety(y)

def paleta_izquierda_abajo():
    y = paleta_izquierda.ycor()
    y -= 40
    paleta_izquierda.sety(y)

def paleta_derecha_arriba():
    y = paleta_derecha.ycor()
    y += 40
    paleta_derecha.sety(y)

def paleta_derecha_abajo():
    y = paleta_derecha.ycor()
    y -= 40
    paleta_derecha.sety(y)

# Asignaciones de teclas
ventana.listen()
ventana.onkeypress(paleta_izquierda_arriba, "w")
ventana.onkeypress(paleta_izquierda_abajo, "s")
ventana.onkeypress(paleta_derecha_arriba, "Up")
ventana.onkeypress(paleta_derecha_abajo, "Down")

# Función para reiniciar el juego después de anotar un punto
def reiniciar_juego():
 
    # Restablecer la posición de las paletas y la pelota
    paleta_izquierda.goto(-350, 0)
    paleta_derecha.goto(350, 0)
    pelota.goto(0, 0)
    time.sleep(1)

# Bucle principal del juego
while True:
    ventana.update()

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Rebotar la pelota en los bordes superior e inferior
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
    
     # Verificar si la pelota se sale de los bordes laterales
    if pelota.xcor() > 390:
        pelota.goto(0, 0)  # Reposicionar la pelota en el centro
        pelota.dx *= -1  # Cambiar la dirección de la pelota
        puntaje_izquierda += 1  # Puntuación para el jugador izquierdo
        actualizar_puntaje()
        reiniciar_juego()

    if pelota.xcor() < -390:
        pelota.goto(0, 0)  # Reposicionar la pelota en el centro
        pelota.dx *= -1  # Cambiar la dirección de la pelota
        puntaje_derecha += 1  # Puntuación para el jugador derecho
        actualizar_puntaje()
        reiniciar_juego()

    # Rebotar la pelota en las paletas
    if (pelota.dx > 0) and (350 > pelota.xcor() > 340) and (paleta_derecha.ycor() + 50 > pelota.ycor() > paleta_derecha.ycor() - 50):
        pelota.setx(340)
        pelota.dx *= -1


    if (pelota.dx < 0) and (-350 < pelota.xcor() < -340) and (paleta_izquierda.ycor() + 50 > pelota.ycor() > paleta_izquierda.ycor() - 50):
        pelota.setx(-340)
        pelota.dx *= -1
  

