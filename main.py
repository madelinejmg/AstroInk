from src.arxiv_scraper import search_arxiv
from src.summarizer import summarize_text
from src.citation_formatter import format_bibtex

def main():
    query = input("Enter your search topic: ")
    results = search_arxiv(query)

    for paper in results:
        print("\nTitle:", paper["title"])
        print("Authors:", ", ".join(paper["authors"]))
        print("Summary:", summarize_text(paper["summary"]))
        print("Citation (BibTeX):\n", format_bibtex(paper))
        print("Link:", paper["url"])
        print("-" * 50)

if __name__ == "__main__":
    main()
