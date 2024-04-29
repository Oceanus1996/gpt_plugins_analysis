import requests
import pandas as pd
from utilities import categorise_data, filter_category, calculate_zscore, get_column
import numpy as np
import time

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
headers = {"Authorization": "Bearer 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"}

test_categories = ['Books', 'Business', 'Career', 'Document Management',
                   'Developer & Code', 'Education', 'Entertainment', 'Finance', 'Food & Drink', 'Games', 'Graphics & Design', 'Health & Fitness', 'Lifestyle',
                   'Medical', 'Music', 'Navigation', 'News', 'Photo & Video', 'Productivity', 'Reference', 'Shopping', 'Social Networking',
                   'Sports', 'Travel', 'Utilities', 'Weather']

categories = ['Books', 'Business', 'Career & Jobs', 'Charts & Diagrams', 'Document Management',
              'Developer & Code', 'Education & Learning', 'Entertainment & Game', 'Finance & Trading', 'Travel & Lifestyle', 'Health & Medical', 'Audio & Music', 'News', 'Image & Video', 'Data & Research', 'Crypto & NFTs', 'Shopping & Deals', 'Law', 'Plugin Tips', 'Weather & Climate']


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def query_classification(description, categories):
    return query({
        "inputs": description,
        "parameters": {"candidate_labels": categories},
    })


def classify(description, categories):
    batch_size = 10
    results = {}

    # Loop through categories in batches
    for i in range(0, len(categories), batch_size):
        # Splitting categories into batches
        batch_categories = categories[i:i + batch_size]
        try:
            # calculate score for current batch with ML model
            output = query_classification(description, batch_categories)
            category_score = {label: score for label, score in zip(
                output['labels'], output['scores'])}

            # print(output)
        except Exception as e:
            print("Incorrect output in classify:", output)
            time.sleep(30)
            return

        results = {**results, **category_score}
        # print(category_score)
    results = dict(
        sorted(results.items(), key=lambda item: item[1], reverse=True))
    # print(results)
    top10 = list(results.items())[:10]
    keys = [item[0] for item in top10]
    # print(keys)
    max_category = (classify_top10(description, keys))
    # find category with max score
    # max_category = max(results, key=results.get)
    # print(max_category, results[max_category])
    print(description)
    print(max_category)
    return max_category


def classify_top10(description, top10):
    results = {}
    try:
        output = query_classification(description, top10)
        category_score = {label: score for label, score in zip(
            output['labels'], output['scores'])}
    except Exception as e:
        print("Incorrect output:", output)
        time.sleep(30)
        return

    results = category_score
    # print(category_score)
    results = dict(
        sorted(results.items(), key=lambda item: item[1], reverse=True))
    print(results)

    # find category with max score
    max_category = max(results, key=results.get)
    return max_category


classify("Text to smart-contract. Describe a process to generate a smart-contract and deploy to any blockchain.",
         categories)
categorise_data('plugins_scrape/plugin_2024-03-19.xlsx', classify,
                'categorisation_result.xlsx', 'categorisation_partial.xlsx', categories)
