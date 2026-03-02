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