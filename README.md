<h1 align="center">AstroInk 🪐</h1>
<p align="center">A faster way to search for astrophysical research papers from <a href="https://arxiv.org/">arXiv</a></p>

<p align="center">
  <img src="astroink.png">
</p>

# What is AstroInk?
AstroInk is a Python-based tool designed to streamline the process of finding, summarizing, and citing astrophysical research papers from arXiv, an open-access repository featuring the latest scientific publications. Users can input a topic or keyword (such as "transits" or "stellar variability"), and the tool automatically queries the arXiv API to retrieve the most relevant papers. It then parses each paper's metadata, including the title, authors, abstract, publication source, and publication date. AstroInk uses a simple rule-based summarization method, which extracts the first few sentences from each abstract using Python’s ```re``` (regular expressions) module. It also auto-generates BibTeX citations, ready to be dropped into research documents.

AstroInk is particularly useful for students and early-career researchers who are often overwhelmed by the sheer volume of new papers published daily. Instead of skimming through dozens of abstracts or manually formatting citations, users can quickly gain insights into current research topic trends and compile bibliographies within seconds. Its modular design allows for flexible use wuith a graphical interface (currently deployed via Streamlit). By combining astrophysical literature search with summarization and citation support, AstroInk helps bridge the gap between information overload and efficient scientific discovery.

# Quickstart
Try AstroInk instantly without installing anything by visiting the public [Streamlit app](https://astroinkapp.streamlit.app/).
















