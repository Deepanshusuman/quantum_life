from quantum_life import QuantumLifeForm

# Create a lifeform
bot = QuantumLifeForm("Q-Bot")

# Run the simulation for 10 cycles
for _ in range(10):
    bot.run("simulated environment")
