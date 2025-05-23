import streamlit as st
import sys
import os
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from summarizer import summarize_text
from arxiv_scraper import search_arxiv
from keywords import extract_keywords

st.set_page_config(page_title='AstroInk', layout='wide')

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f8f9fa;
    }
    h1 {
        text-align: center;
        color: #343a40;
    }
    p {
        text-align: center;
        font-size: 1.2em;
    }
    footer {
        text-align: center;
        font-size: 0.8em;
        color: #6c757d;
        padding-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("AstroInk")
st.markdown("**A faster way to search for astrophysical research papers from arXiv**")


# Sidebar controls
st.sidebar.markdown(
    """
    <div style="text-align">
        <img src="https://info.arxiv.org/brand/images/brand-logo-black.jpg" width="300">
    </div>
    """,
    unsafe_allow_html=True
) # To center the image
st.sidebar.title("Search Options")
query = st.sidebar.text_input("Enter a topic or keyword:", "M-dwarf exoplanets")

# Sidebar Filter Options
st.sidebar.title("Filter Options")
year_filter = st.sidebar.number_input("Show papers from the chosen year and later:", value=2020, min_value=1960, max_value=2100)
max_results = st.sidebar.slider("Number of Papers", 1, 15, 3)
summary_length = st.sidebar.selectbox("Summary Length", ["Short", "Medium", "Long"], index=1)
length_map = {"Short": 2, "Medium": 4, "Long": 6}

# --- Main Search Execution ---
if st.sidebar.button("Search"):
    with st.spinner("Searching arXiv..."):
        papers = search_arxiv(query, max_results=max_results)

    if not papers:
        st.warning("No results found. Try a different topic!")
    else:       
        # Sort papers by most recent
        papers = sorted(papers, key=lambda x: x['published'], reverse=True)

        # Filter papers based on user-selected year
        papers = [paper for paper in papers if paper['published'].year >= year_filter]

        # Display papers normally
        summary_texts = []
        
        for idx, paper in enumerate(papers):
            # BADGES
            col1, col2, col3 = st.columns(3)
        
            abstract_length = len(paper['summary'].split())
            num_authors = len(paper['authors'])
            year_published = paper['published'].year
        
            special_paper = False
            # Title with inline "New" badge if needed
            if year_published >= 2024:
                st.markdown(f"### {idx+1}. [{paper['title']}]({paper['url']}) &nbsp; <span style='background-color: #e0f7fa; color: #007BFF; padding: 3px 8px; border-radius: 8px; font-size: 0.8em;'>NEW</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"### {idx+1}. [{paper['title']}]({paper['url']})")

            st.markdown(f"**Authors:** {', '.join(paper['authors'])}")
            st.markdown(f"**Published:** {paper['published'].date()}")

            summary = summarize_text(paper['summary'], num_sentences=length_map[summary_length])

            # Summary
            st.markdown("**Summary:**")
            st.write(summary)
            
            summary_texts.append(f"Title: {paper['title']}\nSummary: {summary}\n")
            
            # Extract and show keywords
            keywords = extract_keywords(paper['summary'])
            st.markdown("**Keywords:** " + ", ".join(f"`{kw}`" for kw in keywords))
            
            # PDF Download link
            paper_id = paper['url'].split('/')[-1]  # Get the arXiv ID part
            pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"

            # Fetch the PDF file
            response = requests.get(pdf_url)

            if response.status_code == 200:
                st.download_button(
                    label="Download PDF",
                    data=response.content,
                    file_name=f"{paper_id}.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("Failed to fetch the PDF.")
                
            # Citation block
            st.markdown("**Citation (BibTeX):**")
            st.code(paper['citation'], language='bibtex')

            # Individual BibTeX download
            st.download_button(
                label="Download BibTeX",
                data=paper['citation'],
                file_name=f"{paper['title'][:50].replace(' ', '_')}.bib",
                mime="text/plain"
            )

            st.markdown("---")
            
        # Export all summaries
        if summary_texts:
            full_export = "\n\n".join(summary_texts)
            st.sidebar.download_button(
                label="Download All Summaries",
                data=full_export,
                file_name="astroink_summaries.txt",
                mime="text/plain"
            )
            
        # Export all citations
        if papers:
            all_citations = "\n\n".join(paper['citation'] for paper in papers)
            st.sidebar.download_button(
                label="Download All Citations (.bib)",
                data=all_citations,
                file_name="astroink_citations.bib",
                mime="text/plain"
            )
            
# About Section
st.sidebar.title("About AstroInk")
st.sidebar.info(
    """
    AstroInk helps users quickly search for, summarize, and cite astrophysical research papers from arXiv.
    """
)
