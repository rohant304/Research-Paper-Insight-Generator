import streamlit as st

from src.dataset_loader import load_dataset
from src.pdf_loader import extract_text_from_url
from src.text_processor import clean_text
from src.insight_generator import generate_insights


st.title("Research Paper Insight Generator")

df = load_dataset()

paper = st.selectbox(
    "Select Research Paper",
    df["Title"].tolist()
)

if st.button("Analyze Research Paper"):

    try:
        selected = df[df["Title"] == paper].iloc[0]

        with st.spinner("Downloading and reading paper..."):
            text = extract_text_from_url(selected["PDF_URL"])
            text = clean_text(text)

        with st.spinner("Generating insights..."):
            insights = generate_insights(text)

        st.header("Research Paper Insights")

        st.subheader("Abstract")
        st.write(insights["Abstract"])

        st.subheader("Methodology")
        st.write(insights["Methodology"])

        st.subheader("Findings")
        st.write(insights["Findings"])

        st.subheader("Conclusion")
        st.write(insights["Conclusion"])

    except Exception as e:
        st.error(f"Something went wrong: {e}")