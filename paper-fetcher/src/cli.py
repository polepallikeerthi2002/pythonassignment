import argparse
from paper_fetcher.fetcher import Fetcher

def main():
    parser = argparse.ArgumentParser(description='Paper Fetcher CLI')
    parser.add_argument('--source', type=str, required=True, help='Source to fetch papers from')
    parser.add_argument('--count', type=int, default=10, help='Number of papers to fetch')
    
    args = parser.parse_args()
    
    fetcher = Fetcher()
    papers = fetcher.fetch_papers(args.source, args.count)
    
    for paper in papers:
        print(paper)

if __name__ == '__main__':
    main()