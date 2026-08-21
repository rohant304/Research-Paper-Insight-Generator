import pandas as pd


def load_dataset():

    file_path = "data/arxiv_llm_research_papers.csv"

    df = pd.read_csv(file_path)

    return df


def get_paper(index=0):

    df = load_dataset()

    paper = df.iloc[index]

    return {
        "title": paper["Title"],
        "abstract": paper["Abstract"],
        "authors": paper["Authors"],
        "category": paper["Primary_Category"],
        "pdf_url": paper["PDF_URL"]
    }