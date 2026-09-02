import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("Iris.csv")

species = iris["Species"].value_counts()

fig, ax = plt.subplots(3, 2, figsize=(12, 12))

ax[0, 0].plot(iris["SepalLengthCm"].head(20))
ax[0, 0].set_title("Sepal Length - Line Plot")
ax[0, 0].set_xlabel("Sample")
ax[0, 0].set_ylabel("Sepal Length (cm)")

ax[0, 1].scatter(iris["SepalLengthCm"], iris["PetalLengthCm"])
ax[0, 1].set_title("Sepal Length vs Petal Length")
ax[0, 1].set_xlabel("Sepal Length (cm)")
ax[0, 1].set_ylabel("Petal Length (cm)")

ax[1, 0].bar(species.index, species.values)
ax[1, 0].set_title("Flowers by Species")
ax[1, 0].set_xlabel("Species")
ax[1, 0].set_ylabel("Number of Flowers")

ax[1, 1].hist(iris["SepalLengthCm"], bins=10)
ax[1, 1].set_title("Sepal Length Distribution")
ax[1, 1].set_xlabel("Sepal Length (cm)")
ax[1, 1].set_ylabel("Frequency")

ax[2, 0].pie(
    species.values,
    labels=species.index,
    autopct="%1.1f%%"
)
ax[2, 0].set_title("Iris Species Distribution")

ax[2, 1].scatter(
    iris["SepalWidthCm"],
    iris["PetalWidthCm"]
)
ax[2, 1].set_title("Sepal Width vs Petal Width")
ax[2, 1].set_xlabel("Sepal Width (cm)")
ax[2, 1].set_ylabel("Petal Width (cm)")

plt.tight_layout()

plt.show()