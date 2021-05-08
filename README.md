# Snake
Juego de la víbora, utilizando las librerías turtle y freegames

Este código mostraba el típico juego de una serpiente que cada vez que come, aumentaba de tamaño. La practica solicitaba que de una lista de cinco colores, se eligieran de manera aleatoria y se colocaran en el cuerpo de la serpiente y la comida, también se solicitaba que la comida cambiara de posición en algún momento.

# Análiis

* Se revisó el comportamiento del programa y como es que diferentes funciones actuaban entre sí.
* Se localizó el área donde los colores se establecían al inicio del juego.
* Se localizó las funciones de movimiento para cambiar algunos valores de vectores de posición.

## Ricardo:

1. Importé nuevamente random para que me ayudara a que ciertas variables que involucraban choice funcionaran.
2. Creé una lista de cinco colores.
3. Coloqué dos variables, una referente al color de la serpiente y otra al color de la comida, ambas les coloqué un comando choice para que de manera aleatoria eligieran un color.
4. Coloqué un condicional para que no repitan los colores entre el cuerpo y la comida.
5. Modifiqué algunas líneas de "for body in snake:" donde establecían algunos colores, esta modificación, ayuda a que se proyecten los cambios realizados.

        import random

        colores = [
             'yellow','black','blue',
             'purple','orange'
             ]
        serpienteCuerpo = random.choice(colores)
        comidaSerpiente = random.choice(colores)
        
        if comidaSerpiente == serpienteCuerpo:
            comidaSerpiente = random.choice(colores)

        for body in snake:
            square(body.x, body.y, 9, serpienteCuerpo)

        square(food.x, food.y, 9, comidaSerpiente)
        update()
        ontimer(move, 100)
        
