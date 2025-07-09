# papers/fetch_papers.py

from typing import List, Dict
import requests
from xml.etree import ElementTree
import csv

EMAIL = "your_email@example.com"
TOOL = "get-papers-list"
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
HEADERS = {"User-Agent": "get-papers-list/1.0"}

def fetch_papers(query: str, max_results: int = 100) -> List[Dict]:
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "tool": TOOL,
        "email": EMAIL
    }
    search_resp = requests.get(BASE_URL + "esearch.fcgi", params=search_params, headers=HEADERS, timeout=10)
    search_resp.raise_for_status()
    id_list = ElementTree.fromstring(search_resp.text).find("IdList")
    pmids = [id_elem.text for id_elem in id_list.findall("Id")]

    results = []
    for pmid in pmids:
        fetch_params = {
            "db": "pubmed",
            "id": pmid,
            "retmode": "xml",
            "tool": TOOL,
            "email": EMAIL
        }
        fetch_resp = requests.get(BASE_URL + "efetch.fcgi", params=fetch_params, headers=HEADERS, timeout=10)
        fetch_resp.raise_for_status()
        root = ElementTree.fromstring(fetch_resp.text)
        article = root.find(".//Article")
        if article is None:
            continue

        title = article.findtext("ArticleTitle", "")
        pub_date = root.findtext(".//PubDate/Year", "")

        non_academic = []
        company_affiliations = []
        emails = []

        for affil_elem in root.findall(".//AffiliationInfo/Affiliation"):
            affil = affil_elem.text or ""
            company_affiliations.append(affil)
            if any(x in affil.lower() for x in ["pharma", "biotech", "inc", "ltd", "corp", "gmbh"]):
                # Try to get author last name
                author_elem = affil_elem.find("../../LastName")
                if author_elem is not None:
                    non_academic.append(author_elem.text)
            if "@" in affil:
                emails.append(affil)

        results.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "NonAcademic Authors": "; ".join(non_academic),
            "Company Affiliations": "; ".join(company_affiliations),
            "Corresponding Author Email": "; ".join(emails)
        })

    return results

def save_to_csv(results: List[Dict], filename: str):
    if not results:
        print("No results to save.")
        return
    keys = results[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)
