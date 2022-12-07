# this function scrapes the finance site of yahoo for changes in the top market indices
# and returns the result in a nested list
def getMarketIndex():
    import requests
    from bs4 import BeautifulSoup

    response = requests.get("https://finance.yahoo.com/world-indices/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAGm3ti0YOLUL19whXSav3UHvfXZVdnPRJolMjBNCZGFrTruxYMcBOQzrbZAUXs7EWPu2KPnbus-CAZGbAzjGixhL6--vPs2ODf8VmsQAKOCGY0c2YAU_x8Zl13wYb934kSvbqwda-WrKAZCZQcKXRERn2wfBKQTyNLpVE9UcxEGY")
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    result = soup.find("tbody")

    tags = result.find_all("tr")

    marketIndex = []
    for tag in tags:
        market = tag.find(class_="Va(m) Ta(start) Px(10px) Fz(s)")
        marketName = market.text

        change = tag.select('fin-streamer[data-field="regularMarketChangePercent"]')
        changeInPercent = change[0].text

        marketIndex.append([marketName, changeInPercent])

    return marketIndex
