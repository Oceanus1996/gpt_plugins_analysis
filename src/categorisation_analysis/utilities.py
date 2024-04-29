import pandas as pd
import numpy as np


def query_classification(query, description, categories):
    return query({
        "inputs": description,
        "parameters": {"candidate_labels": list(categories.values())},
    })


def categorise_data(file_path, categorise, output_file, temp_file, categories):
    index = 0
    save_interval = 25
    results = {}
    df = pd.read_excel(file_path)
    num_categorised = 0
    plugins = dict(zip(df['title'], df['description']))
    for title, description in plugins.items():
        num_categorised += 1
        print(num_categorised)
        category = categorise(description, categories)
        results[title] = {
            'description': description,
            'category': category
        }
        # to keep track of how many plugins have been categorised
        print("\n")
        index += 1
    # print(results)
    # save intervals of data
        if index % save_interval == 0:
            try:
                # Add a new column 'category' with the results to the DataFrame
                df['category'] = [results[title]['category'] if title in results else None
                                  for title in df['title']]
                df.to_excel(temp_file, index=False)
            except Exception as e:
                print(e)
                pass

    # Save once entire file is categorised
    df['category'] = [results[title]['category'] for title in df['title']]
    df.to_excel(output_file, index=False)


def filter_category(file_path, category, output_file):
    df = pd.read_excel(file_path)

    filtered_data = df[df['category'] == category]
    filtered_data.to_excel(output_file, index=False)


def get_column(file_path, column_name):
    df = pd.read_excel(file_path)
    values = df[column_name].tolist()
    return (values)


def calculate_zscore(scores):
    # Calculate mean and standard deviation
    mean_group = np.mean(scores)
    std_dev_group = np.std(scores)

    # Z-score normalization
    z_scores_group = [(score - mean_group) /
                      std_dev_group for score in scores]
    return z_scores_group


def merge_excel_files(file1_path, file2_path, merge_column, source_column, output_file):
    # Read the Excel files into pandas DataFrames
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    # Merge the DataFrames based on the merge column
    merged_df = pd.merge(
        df1, df2[[merge_column, source_column]], on=merge_column, how='left')
    merged_df.to_excel(output_file, index=False)
