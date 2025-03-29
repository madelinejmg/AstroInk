import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from arxiv_scraper import search_arxiv
from summarizer import summarize_text

st.set_page_config(page_title='AstroInk', layout='wide')

st.title("AstroInk")
st.markdown("**A faster way to search for astrophysical research papers from arXiv..**")

# Sidebar controls
st.sidebar.title("Search Options")
query = st.sidebar.text_input("Enter a topic or keyword:", "M-dwarf exoplanets")
max_results = st.sidebar.slider("Number of Papers", 1, 10, 3)
summary_length = st.sidebar.selectbox("Summary Length", ["Short", "Medium", "Long"], index=1)
length_map = {"Short": 2, "Medium": 4, "Long": 6}

# Execute search
if st.sidebar.button("Search"):
    with st.spinner("Searching arXiv..."):
        papers = search_arxiv(query, max_results=max_results)

    if not papers:
        st.warning("No results found. Try a different topic!")
    else:
        summary_texts = []
        st.success(f"Found {len(papers)} papers for '{query}'")

        for idx, paper in enumerate(papers):
            st.markdown(f"### {idx+1}. [{paper['title']}]({paper['url']})")
            st.markdown(f"**Authors:** {', '.join(paper['authors'])}")
            st.markdown(f"**Published:** {paper['published'].date()}")

            summary = summarize_text(paper['summary'], num_sentences=length_map[summary_length])
            st.markdown("**Summary:**")
            st.write(summary)
            summary_texts.append(f"Title: {paper['title']}\nSummary: {summary}\n")

            st.markdown("**Citation (BibTeX):**")
            st.code(paper['citation'], language='bibtex')

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
