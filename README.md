<h1 align="center">AstroInk 🪐</h1>
<p align="center">A faster way to search for astrophysical research papers from ![arXiv](https://arxiv.org/)</p>

![logo](astroink.png)

# What is AstroInk?
AstroInk is a Python-based tool designed to streamline the process of finding, summarizing, and citing astrophysical research papers from arXiv, an open-access repository featuring the latest scientific publications. Users can input a topic or keyword (such as "transits" or "stellar variability"), and the tool automatically queries the arXiv API to retrieve the most relevant papers. It then parses each paper's metadata, including the title, authors, abstract, publication source, and publication date. Using a natural language processing (NLP) model, AstroInk generates concise, accessible summaries of the abstracts. It also auto-generates citations in formats like BibTeX or APA, ready to be dropped into research documents.

AstroInk is particularly useful for students and early-career researchers who are often overwhelmed by the sheer volume of new papers published daily. Instead of skimming through dozens of abstracts or manually formatting citations, users can quickly gain insights into current research topic trends and compile bibliographies within seconds. Its modular design allows for flexible use: through a command line, Jupyter Notebook, or a graphical interface (currently deployed via Streamlit). By combining astrophysical literature search with summarization and citation support, AstroInk helps bridge the gap between information overload and efficient scientific discovery.

# Getting Started
**Note:** If you prefer, you can try AstroInk instantly without installing anything by visiting the public [Streamlit app](https://astroinkapp.streamlit.app/).
Local installation is optional for users who want to run the app on their own machines.


### Option 1 (Recommended):
1. Try it instantly online → Launch [AstroInk App](https://astroinkapp.streamlit.app/).


### Option 2 (Install locally by following the steps below):
1. To run AstroInk locally:

```shell
git clone https://github.com/yourusername/AstroInk.git
cd AstroInk
```

2. Install the required Python packages:

```shell
pip install -r requirements.txt
```

3. Launch the Streamlit app:

```shell
streamlit run app.py
```

4. Navigate to ```http://localhost:8501``` in your web browser to use AstroInk.






















