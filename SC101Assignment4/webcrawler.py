"""
File: webcrawler.py
Name: Jessie
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        # ----- Write your code below this line ----- #

        tags = soup.find_all('td')
        data = []
        for tag in tags:
            text = tag.text.strip()
            data.append(text)

        total_male = 0
        total_female = 0

        for i in range(0, len(data), 5):
            if i + 4 < len(data):
                male_count = int(data[i + 2].replace(',', ''))
                female_count = int(data[i + 4].replace(',', ''))
                total_male += male_count
                total_female += female_count

        print(f'Male Number: {total_male}')
        print(f'Female Number: {total_female}')


if __name__ == '__main__':
    main()
