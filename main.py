from src.simulated_annealing  import (
    simulated_annealing,
    stations,
    needed_states

)
import matplotlib.pyplot as plt

def main():

    best, best_eval, history = simulated_annealing(stations, needed_states, 2000, 10)

    for _ in range(5):
        _, _, history = simulated_annealing(stations, needed_states, 2000, 10)
        plt.plot(history[:200])

    plt.xlabel("Iteración")
    plt.ylabel("Coste")
    plt.title("Variabilidad entre ejecuciones")
    plt.show()


if __name__ == "__main__":
    main()