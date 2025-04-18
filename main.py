# Name:
# Date:
# Assignment:

import labor
import pandas as pd
import matplotlib.pyplot as plt

result = labor.get_result()

years = []
emplys = []

for Lab in result:
    year = Lab["Time"]["Year"]
    emply = Lab["Data"]["Employed"]["White"]["Counts"]["All"]
    years.append(year)
    emplys.append(emply)

# Create a DataFrame using a dictionary of lists
df = pd.DataFrame({"Year": years,"emply": emplys})

print(df)

# Create a scatter plot
df.plot(kind="scatter", x="Year", y="emply")

# Save the plot to a file
plt.savefig("output.png")
