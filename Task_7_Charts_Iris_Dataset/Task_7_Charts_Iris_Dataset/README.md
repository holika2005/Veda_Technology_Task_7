# Task 7 — First Chart Story: Turning Numbers into a Narrative

## Objective
Build 3–4 simple, clearly labeled charts from a small dataset, with each chart answering one specific question and a short narrative connecting the results.

## Dataset
- **Dataset:** Iris Dataset
- **Rows:** 150
- **Species:** Setosa, Versicolor, Virginica
- **Source used:** the standard Iris dataset available through the Python environment.
- No external dataset was added.

## Tools Used
- **Python**
- **Matplotlib** for the four chart images
- **Excel** workbook for the final data, summary, takeaways, and charts
- Google Sheets was not required.

## Charts and Questions

### 1. Bar Chart — Average Petal Length by Iris Species
**Question:** Which species has the largest average petal length?

**Takeaway:** Virginica has the largest average petal length, making it clearly distinct from the other two species.

### 2. Line Chart — Average Sepal Length by Iris Species
**Question:** How does average sepal length vary by species?

**Takeaway:** Average sepal length rises from Setosa to Versicolor and is highest for Virginica.

### 3. Pie Chart — Iris Dataset Distribution by Species
**Question:** How is the dataset distributed across species?

**Takeaway:** The dataset is evenly balanced, with each species contributing 50 observations (33.3%).

### 4. Bar Chart — Average Petal Width by Iris Species
**Question:** Which species has the largest average petal width?

**Takeaway:** Virginica has the largest average petal width, reinforcing the stronger petal-size pattern in the data.

## Overall Narrative
The Iris dataset is evenly balanced across the three species, so comparisons are not affected by different group sizes. The charts show a consistent pattern: Virginica has the largest average petal measurements and the highest average sepal length, while Setosa is generally at the lower end of the size measures. The visual story therefore highlights clear differences between species while keeping the analysis simple and easy to interpret.

## Chart Selection Logic
- **Bar charts** are used to compare category-level averages directly.
- **Line chart** is used to show the change in average sepal length across the three species categories.
- **Pie chart** is used because there are only three slices and the question is specifically about dataset composition.
- All charts have descriptive titles and labeled axes where applicable.

## Interview Questions

### When would you choose a bar chart over a line chart?
A bar chart is better when comparing separate categories or groups. A line chart is most useful when showing a continuous trend or ordered progression.

### Why are pie charts often discouraged in professional reporting?
Pie charts become difficult to compare when there are many slices or when values are close together. Bars usually make precise comparisons easier. A pie chart is most suitable for a small number of clearly distinct parts of a whole.

## Files
- `iris_dataset.csv` — dataset used for the analysis
- `Task_7_Iris_Charts.xlsx` — Excel workbook containing data, summary, takeaways, and charts
- `charts/` — four chart images generated with Matplotlib
- `analysis.py` — reproducible Python analysis/chart script
- `deployment/DEPLOYMENT.md` — submission/deployment note
- `deployment/ROLLBACK.md` — simple rollback/versioning note
