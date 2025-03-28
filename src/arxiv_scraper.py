import arxiv

def search_arxiv(query, max_results=5):
    results = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []
    for result in results.results():
        paper = {
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "summary": result.summary,
            "published": result.published,
            "url": result.entry_id,
            "citation": f"@article{{{result.entry_id.split('/')[-1]}," +
                        f"\n  title={{ {result.title} }}," +
                        f"\n  author={{ {' and '.join([author.name for author in result.authors])} }}," +
                        f"\n  journal={{ arXiv preprint }}," +
                        f"\n  year={{ {result.published.year} }}\n}}"
        }
        papers.append(paper)

    return papers
