
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

    # convert list objects to string in data
    str_data = ''.join(str(x) for x in data)
    print(str_data)
    # print today's high, 52 weeks high, today's low, 52 weeks low


    # i = 2
    # while i <= 5:
    #     print((str(data[i])).strip('$\xa0'))
    #     i = i + 1



    # i = 2
    # for item in data:
    #     print(item)
    #     i = i + 1
                # cols = [str.text.strip() for str in cols]
                # print(cols)
                # data.append([str for str in cols if str])
                # print(data)
                # print(cols)
            # print(rows[2].find_all('td'))
            # print('\n')
            # cols = rows.find_all('td')
            # print(cols)
        # for row in rows:
        #     bolds = row.find_all('b')
        #     print(bolds)
        # print('\n\n\n\n\n')


    # data = []
    # for row in rows:
    #     cols = row.find_all('td')
    #     cols = [str.text.strip() for str in cols]
    #     data.append([str for str in cols if str])
    #
    # for x in data:
    #     print(x)
