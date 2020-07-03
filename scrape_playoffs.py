from pandas import DataFrame
from bs4 import BeautifulSoup
from urllib.request import urlopen

def scrape_playoff_series(write_csv = False):
    '''
    Scrape playoff series data from basketball-reference.com/playoffs/series.html

    Parameters
    ----------
    write_csv: bool, default False
        Specifies whether the scraped data is output to playoff_series.csv.

    '''
    url = 'https://www.basketball-reference.com/playoffs/series.html'
    html = urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

    table = soup('table', {'id': 'playoffs_series'})[0]
    # Omit first header row and repeat headers which appear throughout table
    tr =table('tr', class_=lambda x: x not in ['over_header', 'thead'])

    # First row in tr is the headers
    headers = [i.text for i in tr[0]('th')]
    body = [[i.text for i in row] for row in tr[1:]]

    df = DataFrame(data = body, columns = headers)
    if write_csv:
        df.to_csv('playoff_series.csv', index=False)

    return df
