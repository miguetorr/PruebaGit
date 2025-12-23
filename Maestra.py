import juego as Jg

# orden de atributos nombre, vida, ataque, defensa

pj1 = Jg.Personaje("Miguel", 10, 10, 8)
pj2 = Jg.Personaje("Andres", 10, 13, 8)

daño_generado= pj1.atacar(pj2)
vida_actualizada = pj2.recibir_daño(daño_generado)

print (f'El jugador {pj2.nombre} ha recibido {daño_generado} de daño y el jugador tiene {vida_actualizada} de vidad')