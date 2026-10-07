import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from pathlib import Path

base = Path(__file__).resolve().parent
charts = base / "charts"
charts.mkdir(exist_ok=True)

iris = load_iris(as_frame=True)
df = iris.frame.rename(columns={
    "sepal length (cm)": "Sepal Length (cm)",
    "sepal width (cm)": "Sepal Width (cm)",
    "petal length (cm)": "Petal Length (cm)",
    "petal width (cm)": "Petal Width (cm)",
    "target": "Target"
})
df["Species"] = df["Target"].map(dict(enumerate(iris.target_names)))
df = df[["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)", "Species"]]

summary = df.groupby("Species", sort=False).agg(
    Average_Sepal_Length=("Sepal Length (cm)", "mean"),
    Average_Sepal_Width=("Sepal Width (cm)", "mean"),
    Average_Petal_Length=("Petal Length (cm)", "mean"),
    Average_Petal_Width=("Petal Width (cm)", "mean"),
    Count=("Species", "size")
).reset_index()

plt.figure()
plt.bar(summary["Species"], summary["Average_Petal_Length"])
plt.title("Average Petal Length by Iris Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.tight_layout()
plt.savefig(charts / "01_average_petal_length_bar.png", dpi=180)
plt.close()

plt.figure()
plt.plot(summary["Species"], summary["Average_Sepal_Length"], marker="o")
plt.title("Average Sepal Length by Iris Species")
plt.xlabel("Species")
plt.ylabel("Average Sepal Length (cm)")
plt.tight_layout()
plt.savefig(charts / "02_average_sepal_length_line.png", dpi=180)
plt.close()

plt.figure()
plt.pie(summary["Count"], labels=summary["Species"], autopct="%1.1f%%", startangle=90)
plt.title("Iris Dataset Distribution by Species")
plt.tight_layout()
plt.savefig(charts / "03_species_distribution_pie.png", dpi=180)
plt.close()

plt.figure()
plt.bar(summary["Species"], summary["Average_Petal_Width"])
plt.title("Average Petal Width by Iris Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Width (cm)")
plt.tight_layout()
plt.savefig(charts / "04_average_petal_width_bar.png", dpi=180)
plt.close()

print("Task 7 charts generated successfully.")
