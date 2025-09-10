# ejercicio_4.py
import random

def juego(con_jugador, cont_maquina, max_rondas=None):
    rondas = 0
    while con_jugador < 3 and cont_maquina < 3:
        rondas += 1
        if max_rondas and rondas > max_rondas:
            break

        print(f"\n----- PUNTAJE -----\nTU = {con_jugador}  ENEMIGO = {cont_maquina}")
        eleccion = input("ELIGE RÁPIDO!\n🤛 = Piedra\n✋ = Papel\n✌️ = Tijera\nTU ELECCIÓN: ").strip()
        opciones = ["🤛", "✋", "✌️"]

        if eleccion not in opciones:
            print("FAILED: Solo puedes elegir 🤛, ✋ o ✌️.")
            continue

        eleccion_maquina = random.choice(opciones)
        print(f"\nELECCIÓN DE TU ENEMIGO: {eleccion_maquina}")

        if eleccion == eleccion_maquina:
            print("EMPATEE!!")
        elif (eleccion == "✋" and eleccion_maquina == "🤛") or \
             (eleccion == "🤛" and eleccion_maquina == "✌️") or \
             (eleccion == "✌️" and eleccion_maquina == "✋"):
            con_jugador += 1
            print("¡El jugador gana! +1 punto")
        else:
            cont_maquina += 1
            print("¡Tu enemigo gana! +1 punto")

        if con_jugador == 3:
            print("\n¡FELICIDADES! ¡HAS GANADO EL JUEGO!")
            break
        if cont_maquina == 3:
            print("\n💀 ¡LA MÁQUINA HA GANADO EL JUEGO! 💀")
            break


if __name__ == "__main__":
    juego(0, 0)
