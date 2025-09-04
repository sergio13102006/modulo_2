import random
def juego(con_jugador,cont_maquina):
    while con_jugador<3 or cont_maquina<3:
        print(f"\n----- PUNTAJE -----\nTU={con_jugador}  ENEMIGO={cont_maquina}")
        eleccion=str(input("ELIGE RAPIDO!\n🤛= Piedra\n✋=Papel\n✌️=tijera\nTU ELECCIÓN:"))
        opciones=["🤛","✋","✌️" ]
        if eleccion not in opciones:
            print("Opción no válida. Por favor, elige uno de los emojis permitidos.")
        eleccion_maquina = random.choice(opciones)
        print(f"\nELECCIÓN DE TU ENEMIGO {eleccion_maquina}")
        if eleccion==eleccion_maquina:
            print("EMPATEE!!")
        elif (eleccion == "✋" and eleccion_maquina == "🤛") or \
             (eleccion == "🤛" and eleccion_maquina == "✌️") or \
             (eleccion == "✌️" and eleccion_maquina == "✋"):
            con_jugador+=1
            print("¡El jugador gana! +1 punto")
        elif (eleccion_maquina == "✋" and eleccion == "🤛") or \
             (eleccion_maquina == "🤛" and eleccion == "✌️") or \
             (eleccion_maquina == "✌️" and eleccion == "✋"):
            cont_maquina+=1
            print("¡Tu enemigo gana! +1 punto")
        if con_jugador == 3:
         print("\n¡FELICIDADES! ¡HAS GANADO EL JUEGO!")
         break
        if cont_maquina == 3:
          print("\n¡LA MÁQUINA HA GANADO EL JUEGO!")
          break
if __name__ == "__main__":
    juego(0,0)