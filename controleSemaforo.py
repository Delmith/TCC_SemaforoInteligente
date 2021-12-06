import os
import traci

# -------------- CARREGAMENTO DOS DADOS ----------------
escolha = int(input("Com \"-gui\"? (1)Sim (0)Não"))
gui = "sumo-gui" if escolha == 1 else "sumo"

escolha = int(input("Qual simulação? (1) map_0.sumocfg (2) map_38.sumocfg (3) map_69.sumocfg"))
sumocfg = "map_0.sumocfg" if escolha == 1 else "map_38.sumocfg" if escolha == 2 else "map_69.sumocfg"
# ------------------------------------------------------

# -------------- INICIAÇÃO DO TRACI ----------------
sumoCmd = [gui, "-c", sumocfg, '--duration-log.statistics']
traci.start(sumoCmd)
# ------------------------------------------------------

# -------------- CARREGAMENTO LISTAS PISTAS -----------------

pistas = ["gneE0_0", "gneE0_1", "gneE2_0", "gneE2_1", "gneE9_0", "gneE9_1", "gneE11_0"]
numeroVeiculos = []

congest = -10
pistaConAntiga = ""
balanco = 0

os.system("cls")
traci.trafficlight.setProgram("gneJ1", "1")

# ------------------------------------------------------

# -------------- EXECUÇÃO DA SIMULAÇÃO COM OS DADOS CARREGADOS ----------------
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    for index, id in enumerate(pistas):
        numeroVeiculos.append(traci.lane.getLastStepHaltingNumber(id))

    pistaConNova = pistas[numeroVeiculos.index(max(numeroVeiculos))]

    if congest + 0.5 < (max(numeroVeiculos) + balanco) or congest == 0:
        balanco = 0

        if pistaConNova != pistaConAntiga :

            if traci.trafficlight.getPhase("gneJ1") < 5 :
                traci.trafficlight.setPhase("gneJ1", traci.trafficlight.getPhase("gneJ1") + 1)

            while traci.trafficlight.getPhase("gneJ1") == 1 or traci.trafficlight.getPhase("gneJ1") == 3 or traci.trafficlight.getPhase("gneJ1") == 5:
                traci.simulationStep()

            if pistaConNova == "gneE0_0" or pistaConNova == "gneE0_1" or pistaConNova == "gneE2_0" or pistaConNova == "gneE2_1":
                traci.trafficlight.setPhase("gneJ1", 0)
            else:
                if pistaConNova == "gneE9_0" or pistaConNova == "gneE9_1" :
                    traci.trafficlight.setPhase("gneJ1", 2)
                else:
                    if pistaConNova == "gneE11_0" :
                        traci.trafficlight.setPhase("gneJ1", 4)

        pistaConAntiga = pistaConNova
        congest = max(numeroVeiculos)

    balanco += 0.01
    numeroVeiculos.clear()

# -------------------------------------------------------
print("Arquivo testado: ", sumocfg, "\n")

traci.close()