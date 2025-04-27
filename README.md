![logo](astroink.png)
# AstroInk
A faster way to search for astrophysical research papers from [arXiv](https://arxiv.org/).


# What is AstroInk?
AstroInk is a Python-based tool designed to streamline the process of finding, summarizing, and citing astrophysical research papers from arXiv, an open-access repository featuring the latest scientific publications. Users can input a topic or keyword (such as "transits" or "stellar variability"), and the tool automatically queries the arXiv API to retrieve the most relevant papers. It then parses each paper's metadata, including the title, authors, abstract, publication source, and publication date. Using a natural language processing (NLP) model, AstroInk generates concise, accessible summaries of the abstracts. It also auto-generates citations in formats like BibTeX or APA, ready to be dropped into research documents.

AstroInk is particularly useful for students and early-career researchers who are often overwhelmed by the sheer volume of new papers published daily. Instead of skimming through dozens of abstracts or manually formatting citations, users can quickly gain insights into current research topic trends and compile bibliographies within seconds. Its modular design allows for flexible use: through a command line, Jupyter Notebook, or a graphical interface (currently deployed via Streamlit). By combining astrophysical literature search with summarization and citation support, AstroInk helps bridge the gap between information overload and efficient scientific discovery.

# Getting Started
1. To run AstroInk locally:

```
git clone https://github.com/yourusername/AstroInk.git
cd AstroInk
```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

3. Launch the Streamlit app:

```
streamlit run app.py
```

4. Navigate to ```http://localhost:8501``` in your web browser to use AstroInk.






















