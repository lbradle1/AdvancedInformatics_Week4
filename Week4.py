```{python}
mtcars = r.mtcars
mtcars.head()
```

```{python}
mtcars.groupby(['cyl'])['mpg'].mean()
```

And the other one:

```{python}
mtcars.groupby(['cyl', 'gear'])['mpg'].mean()
```

```{python}
import sqlite3 # Built into the Python language!
con = sqlite3.connect("mtcars_from_pandas.sqlite3")
# Add our data frame to the mtcars table in the database
mtcars.to_sql("mtcars", con)
con.close()
```

```{r}
list.files(pattern="*.sqlite3")
```

#Read back in

```{python}
import pandas as pd
con = sqlite3.connect("mtcars_from_pandas.sqlite3")
df = pd.read_sql("select * from mtcars", con)
df.head()
```

```{python}
df = pd.read_sql("select cyl, avg(mpg) from mtcars group by cyl", con)
df.head()
```

```{python}
df = pd.read_sql("select cyl, gear, avg(mpg) from mtcars group by cyl, gear", con)
df.head()
```

{python}
import seaborn as sns
import matplotlib.pyplot as plt
g = sns.FacetGrid(r.mtcars2, col="cyl")
g.map(sns.scatterplot,"wt","mpg")
