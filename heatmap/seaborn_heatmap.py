import seaborn as sns
import pandas as pd

data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
sns.heatmap(data)

# Output:
# A heatmap visualization of the data
