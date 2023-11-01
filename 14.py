
import matplotlib.pyplot as plt

# Create a list of animal names
animal_names = ["Peregrine falcon", "Golden eagle", "White-throated needletail swift", "Eurasian hobby", "Frigatebird", "Spur-winged goose", "Cheetah", "Sailfish", "Pronghorn antelope", "Marlin"]

# Create a list of animal speeds
animal_speeds = [389, 240, 169, 160, 153, 142, 120, 112, 88.5, 80.5]

# Create a line chart of the animal speeds
plt.figure(figsize=(24, 6))
plt.plot(animal_names, animal_speeds)
plt.title("Speeds of the fastest animals in the world (km/h)")
plt.xlabel("Animal", labelpad=18)
plt.ylabel("Speed (km/h)")

# Display the chart
plt.show()