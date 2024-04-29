```
├── README.md
├── LICENSE.md
├── INSTALL.md
├── src
│ ├── categorisation_analysis
│ │ ├── categorise_plugins.py
│ │ ├── find_country.py
│ │ ├── search_gpts.py
│ │ ├── utilities.py
├── dataset
│ ├── plugins_scrape
│ ├── plugin_categories.xlsx
```

Note: This tree includes only main files.

Description for each of the main files are as follows.

**src** 
<br>

**categorisation_analysis**
<br>

```categorise_plugins.py``` : Run this file to assign plugins with a appropriate category. This file takes an excel file with plugin information as an input and run the information through a zero-shot classification model along with a list of categories to determine the most suitable category. The description of each plugin and its assigned category will be printed on the console during execution,execution results are stored in an excel file. 

