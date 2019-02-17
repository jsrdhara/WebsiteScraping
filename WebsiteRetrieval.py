def f():
    with open('informs_open_source.csv') as file:
        reader = csv.reader(file)
        sites = list(reader)
        flat_list = [item for sublist in sites for item in sublist]

    f_out = []
    f_authors = []

    for page in flat_list:
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
        driver.get(page)
        Titles = driver.find_elements_by_class_name("citation__title")[0].text
        Abstracts = driver.find_elements_by_class_name("hlFld-Abstract")[0].text
        Authors = driver.find_elements_by_class_name("entryAuthor")
        f_authors.append(Authors)
        f_out.append([Titles, Abstracts])
    auth = []
    for i in f_authors:
        o = []
        for name in i:
            if name.text not in o:
                if name.text != '':
                    o.append(name.text)
        auth.append(o)
    my_df = pd.DataFrame(f_out, columns=['Title', 'Abstract'])
    my_df['authors'] = auth
    my_df.to_csv('pubsonline_informs_opensource.csv', index=False, header=False)
    return (my_df)


f()