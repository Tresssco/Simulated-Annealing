import random,math


# USA states where we want to be listened
needed_states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
added_states = set(
    ["nm", "tx", "ok", "ks", "co", "ne", "sd", "wy", "nd", "ia", "mn", "mo", "ar", "la"]
)

needed_states.update(added_states)

# Radio stations and states covereds
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
stations["ksix"] = set(["nm", "tx", "ok"])
stations["kseven"] = set(["ok", "ks", "co"])
stations["keight"] = set(["ks", "co", "ne"])
stations["knine"] = set(["ne", "sd", "wy"])
stations["kten"] = set(["nd", "ia"])
stations["keleven"] = set(["mn", "mo", "ar"])
stations["ktwelve"] = set(["la"])
stations["kthirteen"] = set(["mo", "ar"])


# Definition of the objetive function
def objective_function(solution, stations, needed_states):

    covered = set()                         #Conjunto para guardar los estados que cubren las estaciones

    for station in solution:
        covered |= stations[station]        #Union para acumular en el set

    uncovered = needed_states - covered     #Calculo que estados faltan por cubrir

    # Penalize uncovered states with a value of 50
    return len(uncovered) * 50 + len(solution)


# Neighbor function: small random change
def get_neighbor(solution, all_stations):
    new_solution = solution.copy()

    #Se genera un número entre 0 y 1 y nos aseguramos de solamente de, en caso de ser menor a 0.5, eliminar solo 1 estación
    if random.random() < 0.5 and len(new_solution) > 1:        
        new_solution.remove(random.choice(list(new_solution)))
    else:
        new_solution.add(random.choice(list(all_stations)))

    return new_solution


# Simulated Annealing function
def simulated_annealing(stations, needed_states, n_iterations, temp):

    all_stations = list(stations.keys())        #Convertimos el diccionario de estaciones a una lista

    
    current = set(random.sample(all_stations, 3))   #Se eligen 3 estaciones al azar para empezar
    current_eval = objective_function(current, stations, needed_states)

    best = current.copy()
    best_eval = current_eval    #Guardamos la mejor solución (al principio la mejor es la inicial)

    history = []   
    for i in range(n_iterations):
        t = temp / float(i + 1)     #Temperatura actual, disminuye en cada iteración, esquema de enfriamiento hiperbólico.
       #t = temp * (0.95**i)        #Esquema de enfriamiento geométrico

        candidate = get_neighbor(current, all_stations)     #Generamos una solución vecina
        candidate_eval = objective_function(candidate, stations, needed_states) #La evaluamos

        delta = candidate_eval - current_eval   #Se mide cuanto empeora o mejora la nueva solución

        #Decisión de aceptar la nueva solución.
        #Delta < 0: La solución mejora
        #Delta > 0: La solución empeora. Se acepta con cierta probabilidad (OR). 
            # A mayor delta menor probabilidad. 
            # A mayor t mayor probabilidad.

        if delta < 0 or random.random() < math.exp(-delta / t):
            current = candidate
            current_eval = candidate_eval

            if candidate_eval < best_eval:
                best = candidate.copy()
                best_eval = candidate_eval

        history.append(best_eval)   

    return best, best_eval, history




