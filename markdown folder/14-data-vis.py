# from pyexpat.errors import codes
# from turtle import color
# steps involves in data visualization
# step 1. import libraries

import seaborn as sns
import matplotlib.pyplot as plt
# step2. set a theme
sns.set_theme(style="ticks", color_codes=True)

# step 3.import data set
kashti = sns.load_dataset("titanic")
print(kashti)

# step4.plot basic graph with one variable (countplot)
# p = sns.countplot(x="sex", data= kashti)
# plt.show()

# step5. plot basic graph with 2 variables(countplot) with titles
p = sns.countplot(x="sex", data= kashti, hue="class")
p.set_title("first count_plot")
plt.show()

 
