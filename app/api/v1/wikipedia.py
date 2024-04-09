import logging
import requests
from fastapi import APIRouter
from app.models.wikepedia import WikipediaPage, WikipediaSearchResult
from typing import List, Optional
from bs4 import BeautifulSoup

WIKEPEDIA_URL = "https://en.wikipedia.org/w/api.php"

router = APIRouter()

@router.get('/pages', response_model=List[WikipediaSearchResult])
def wikipedia_search(query: str, max_results: int = 100):
    search_results = []
    session = requests.Session()
    continue_fetch = True
    total_hits = 0
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': query
    }
    while continue_fetch:
        logging.info(f"Requesting search results from {WIKEPEDIA_URL} with query parameters: {params}...")
        response = session.get(url=WIKEPEDIA_URL, params=params)
        data = response.json()
        # Results are served 10 at a time
        if len(search_results) < max_results - 10 and 'continue' in data:
            params['sroffset'] =  data['continue']['sroffset']
        else:
            continue_fetch = False       
        if 'searchinfo' in data['query']:
            total_hits = data['query']['searchinfo']['totalhits']
        if 'search' in data['query']:
            for hit in data['query']['search']:
                search_results.append(
                    WikipediaSearchResult(
                        pageid=hit['pageid'],
                        title=hit['title'],
                        snippet=hit['snippet'],
                        wordcount=hit['wordcount'],
                        size=hit['size'],
                        timestamp=hit['timestamp']                 
                    )
                )
    logging.info(f"Api claims totalhits = {total_hits} - received {len(search_results)} items")
    return search_results

@router.get('/pages/{pageid}', response_model=Optional[WikipediaPage])
def wikipedia_retrieve_page_text(pageid: int):
    session = requests.Session()
    params = {
        'action': 'parse',
        'format': 'json',
        'pageid': pageid
    }
    logging.info(f"Requesting page from {WIKEPEDIA_URL} with query parameters: {params}...")
    response = session.get(url=WIKEPEDIA_URL, params=params)
    data = response.json()
    if 'parse' in data:
        soup = BeautifulSoup(data['parse']['text']['*'], 'html.parser')
        return WikipediaPage(pageid=pageid, title=data['parse']['title'], text=soup.get_text())