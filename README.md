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

<h1>src</h1>
<br>

**categorisation_analysis**
<br>

```categorise_plugins.py``` : Run this file to assign plugins with an appropriate category. This file takes an excel file with plugin information as an input and run the information through a zero-shot classification model along with a list of categories to determine the most suitable category. The description of each plugin and its assigned category will be printed on the console during execution,execution results are stored in an excel file. 

```find_country.py``` : Utilize a NLP model to identify GPE(geopolitical entities) and NORP (Nationalities or religious or political groups) within plugin descriptions to determine if a plugin is sepcific to geographical regions. Report the counts of identified entities.

```search_gpts``` : Automated script to use plugin names as search terms on the GPTs Hunter website (https://www.gptshunter.com/) to determine if a plugin has a corresponding GPT. Search results are screenshotted and stored in a folder.

```utilities.py``` : File for utilities functions such as filtering a specific category, get a column from an excel file as a python list, and merging excel files based on common attributes. 

<h1>dataset</h1>
<br>

**plugins_scrape** : A folder containing Excel files listing all plugins on the plugin store and their associated information collected daily from 20/11/2023 to 19/3/2024.
<br>

```plugin_categories.xlsx``` : An Excel file containing plugins and their assigned categories. An overview tally of each category is calculated at the end of the file. This file utilizes the plugin scrape version of 10/1/2024.

