from quantum_life import QuantumLifeForm

creature = QuantumLifeForm("Q-Bot")
for _ in range(10):
    creature.run("simulated environment")
