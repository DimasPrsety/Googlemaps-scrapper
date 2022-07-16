# GoogleMapsScraper
A python based google maps scraper to scrape hotels and restaurants information. The program returns name and location of  nearest 8-12 hotels and restaurants using selenium.

To use the class initialize it with class name GoogleMapsScraper().

if you want to run selenium in headless mode initialize like this: GoogleMapsScraper(headless=True) .

Similarly if you do not want to fetch restaurants or hotels data just pass False as value in arguments e.g GoogleMapsScrapper(hotels=False) or GoogleMapsScrapper(restaurants=False) or GoogleMapsScrapper(hotels=False,restaurants=False).

Note that default value of headless is False and default values of restaurants and hotels is True.

Call function SearchMaps("Your location name") to start the seraching and scraping process.

Note that Your location should be a string and not a link.

Example:

    gs=GoogleMapsScraper(restaurants=True,hotels=True)

    p=gs.SearchMaps("wadi bani khalid")

    print(p)

The function returns a tuple having 2 lists. First list contains dictionaries of restaurants data (restaurant name as key and location link as value). The second list contains dictionaries of Hotels data (hotel name as key and location link as value).

Please let me know if in anyway program can be improved.
