import pandas as pd
def f():
    with open(r'C:\Users\jayaramkapil\Downloads\Crowdfunding.csv') as file:
        reader = csv.reader(file)
        sites = list(reader)
        flat_list = [item for sublist in sites for item in sublist]

    f.out = []

    for page in flat_list:
        open_page = urllib.request.urlopen(page)
        Soup = BeautifulSoup(open_page, 'html.parser')

        for div in Soup.findAll('div', {'id': 'title', 'class': 'element'}):
            try:
                a = div.findAll('a')[0]
                Title = a.text.strip()
            except:
                a = None
                Title = None
        for div in Soup.findAll('div', {'id': 'abstract', 'class': 'element'}):
            try:
                a = div.findAll('p')[0]
                Abstract = a.text.strip()
            except:
                a = None
                Abstract = None
        for div in Soup.findAll('div', {'id': 'authors', 'class': 'element'}):
            try:
                a = div.findAll('p')[0]
                Authors = a.text.strip()
            except:
                a = None
                Authors = None
        for div in Soup.findAll('div', {'id': 'recommended_citation', 'class': 'element'}):
            try:
                a = div.findAll('p')[0]
                Recommended_Citation = a.text.strip()
            except:
                a = None
                Recommended_Citation = None

        for div in Soup.findAll('div', {'id': 'doi', 'class': 'element'}):
            try:
                a = div.findAll('p')[0]
                DOI = a.text.strip()
            except:
                a = None
                DOI = None

        f.out.append([Title, Abstract, Authors, Recommended_Citation, DOI])
    my_df = pd.DataFrame(f.out, columns=['Title', 'Abstract', 'Auhtors', 'Recommended Citation', 'DOI'])
    my_df.to_csv('my_csv.csv', index=False, header=False)


f()