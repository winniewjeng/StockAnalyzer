
import requests
import bs4

if __name__ == "__main__":
    symb = input("stock symbol: ").lower()

    # https://www.nasdaq.com/symbol/aapl
    r = requests.get('https://www.nasdaq.com/symbol/{}'.format(symb))
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all("table")
    # # print(table)
    data = []
    for table in tables:
        rows = table.find_all('td')
        if len(rows) is 6:
            for row in rows:
                cols = row.find_all('b')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])
                # print(str(data).strip('[\'I'))

    list = ['today_hi', 'today_low', 'year_hi', 'year_low']

    i = 2
    j = 0
    # convert list objects to string in data
    while i <= 5:
        # data2 = ((str(data[i])).strip('[\'$\\xa0\']'))
        list[j] = list[j] + " $" + (str(data[i])).strip('[\'$\\xa0\']')
        # print((str(data[i])).strip('[\'$\\xa0\']'))
        # print('\n\n')
        i = i + 1
        j = j + 1

    # print today's high, 52 weeks high, today's low, 52 weeks low
    # print(list)
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])