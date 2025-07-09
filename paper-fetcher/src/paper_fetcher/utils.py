def format_paper_data(paper):
    # Format the paper data for display
    return f"Title: {paper['title']}\nAuthors: {', '.join(paper['authors'])}\nAbstract: {paper['abstract']}\n"

def log_error(error_message):
    # Log the error encountered during fetching
    with open('error.log', 'a') as log_file:
        log_file.write(f"Error: {error_message}\n")