import pandas as pd
import numpy as np

# used for zero shot classification


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
    # Check if it's time to save the data
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


def filter_incorrect(file_path):
    df = pd.read_excel(file_path)
    # print(df.columns)

    # Filter entries where 'incorrect' equals 1
    filtered_data = df[df['status'] == 1.0]
    # Save the filtered data to a new Excel file
    filtered_data.to_excel('incorrect_entries.xlsx', index=False)


def filter_category(file_path, category, output_file):
    df = pd.read_excel(file_path)
    # print(df.columns)

    # Filter entries where 'incorrect' equals 1
    filtered_data = df[df['category'] == category]
    # print(filtered_data)
    # Save the filtered data to a new Excel file
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


def merge_excel_files(file1_path, file2_path, merge_column, source_column):
    # Read the Excel files into pandas DataFrames
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    # Merge the DataFrames based on the merge column
    merged_df = pd.merge(
        df1, df2[[merge_column, source_column]], on=merge_column, how='left')
    merged_df.to_excel('broken.xlsx', index=False)


categories = {
    'Books': 'provide extensive interactivity for content that is traditionally offered in printed form such as books. ',
    'Business': 'assist with running a business or provide a means to collaborate, advertise, edit, or share content.',
    '*Career': 'facilitating career advancement, aiding in resume building, cover letter creation, job search, and skill development for job seekers or those undergoing career changes.',
    '*Document Management': 'enabling extraction, analysis, and interaction with diverse document formats like PDFs,spreadsheets and Google Drive files, enhancing productivity and accessibility through efficient organization and content querying which can include chat.',
    'Developer Tools': 'provide tools for coding, app development, management, and distribution.',
    'Education': 'provide an interactive learning experience on a specific skill or subject.',
    'Entertainment': 'are interactive and designed to entertain and inform the user, and which contain audio, visual, or other content. Includes movies.',
    'Finance': 'perform financial transactions or assist the user with business or personal financial matters.',
    'Food & Drink': 'provide recommendations, instruction, or critique related to the preparation, consumption, or review of food or beverages.',
    'Games': 'provide single or multiplayer interactive activities for entertainment purposes. (Game)',
    'Graphics & Design': 'provide tools for art, design, diagrams, charts and graphics creation.',
    'Health & Fitness': 'related to healthy living, including stress management, fitness, and recreational activities.',
    'Lifestyle': 'relating to a general-interest subject matter or service.',
    'Medical': 'focused on medical education, information management, or health reference for patients or healthcare professionals.',
    'Music': 'are for discovering, listening to, recording, performing, or composing music, and that are interactive in nature.',
    'Navigation': 'provide information to help a user travel to a physical location.',
    'News': 'provide information about current events or developments in areas of interest.',
    'Photo & Video': 'assist in creating, editing, managing, storing, or sharing photos and videos.',
    'Productivity': 'make a specific process or task more organized or efficient.',
    'Reference': 'assist the user in accessing or retrieving information.',
    'Shopping': 'support the purchase of consumer goods or materially enhance the shopping experience.',
    # often confused for photo and video category
    'Social Networking': 'connect people by means of text, voice, photo, or video.',
    'Sports': 'related to professional, amateur, collegiate, or recreational sporting activities.',
    'Travel': 'assist the user with any aspect of travel, such as planning, purchasing, or tracking.',
    'Utilities': 'enable the user to solve a problem or complete a specific task.',
    '*Web': 'facilitate browsing, search, extraction, and analysis of online content, empowering users to navigate, interact and communicate with web-based information, services, and resources effectively.',
    'Weather': 'provide forecasts, alerts, and information related to weather conditions.'
}

categories_20 = {
    'Business': 'assist with running a business or provide a means to collaborate, advertise, edit, or share content.',
    '*Career': 'facilitating career advancement, aiding in resume building, cover letter creation, job search, and skill development for job seekers or those undergoing career changes.',
    '*Document Management': 'enabling extraction, analysis, and interaction with diverse document formats like PDFs,spreadsheets and Google Drive files, enhancing productivity and accessibility through efficient organization and content querying which can include chat.',
    'Developer Tools': 'provide tools for coding, app development, management, and distribution.',
    'Education': 'provide an interactive learning experience on a specific skill or subject.',
    'Entertainment': 'are interactive and designed to entertain and inform the user, and which contain audio, visual, or other content. Includes movies.',
    'Finance': 'perform financial transactions or assist the user with business or personal financial matters.',
    'Graphics & Design': 'provide tools for art, design, diagrams, charts and graphics creation.',
    'Lifestyle': 'relating to a general-interest subject matter or service.',
    'Medical': 'focused on medical education, information management, or health reference for patients or healthcare professionals.',
    'Navigation': 'provide information to help a user travel to a physical location.',
    'News': 'provide information about current events or developments in areas of interest.',
    'Photo & Video': 'assist in creating, editing, managing, storing, or sharing photos and videos.',
    'Productivity': 'make a specific process or task more organized or efficient.',
    'Reference': 'assist the user in accessing or retrieving information.',
    'Shopping': 'support the purchase of consumer goods or materially enhance the shopping experience.',
    'Social Networking': 'connect people by means of text, voice, photo, or video.',
    'Travel': 'assist the user with any aspect of travel, such as planning, purchasing, or tracking.',
    'Utilities': 'enable the user to solve a problem or complete a specific task.',
    'Weather': 'provide forecasts, alerts, and information related to weather conditions.'
}

# Find min and max scores in Group
# min_score = min(output['scores'])
# max_score = max(output['scores'])

# # Normalize scores for Group
# normalized_scores = [
#     (score - min_score) / (max_score - min_score) for score in output['scores']]
# category_score = {label: score for label, score in zip(
#     output['labels'], normalized_scores)}
