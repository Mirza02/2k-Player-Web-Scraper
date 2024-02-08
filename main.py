import re
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

def DodajUTabelu(url, output_file):
    driver_path = '~/Downloads/chromedriver'

    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url)
    #driver.implicitly_wait(5)
    page_source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page_source, 'html.parser')

    players = soup.find('tbody')

    names_raw = players.find_all(class_="entry-font")
    names = [name.get_text() for name in names_raw]

    # Find all attribute boxes
    regex = re.compile('.*attribute-box.*')
    ratings_raw = players.find_all("span", {"class": regex})
    ratings = [int(rating.get_text()) for rating in ratings_raw]

    # print(ratings)
    ratings_pp = np.array(ratings)
    # print(type(ratings_pp))
    ratings_matrix = ratings_pp.reshape(len(names), 3)
    # print(ratings_matrix)
    ovrs = [x[0] for x in ratings_matrix]

    players_info = pd.DataFrame(
        {
            'Player': names,
            'OVR': ovrs
        }
    )

    players_info.to_csv(output_file, mode='a', header=False, index=False)

    print("Data appended successfully.")


def main():
    output_file = "qll_time_data.csv"
    DodajUTabelu("https://www.2kratings.com/teams/all-time-washington-wizards", output_file)

    output_file = "qll_time_data.csv"
    driver_path = '~/Downloads/chromedriver'


    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://www.2kratings.com/all-time-teams")
    #driver.implicitly_wait(5)
    page_source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page_source, 'html.parser')

    table = soup.find("tbody")
    rows = table.find_all("tr")
    for row in rows:
        link = row.find("a")
        if link:
            link_url = link.get("href")
            DodajUTabelu(link_url, output_file)


    #DodajUTabelu("https://www.2kratings.com/teams/atlanta-hawks", output_file)
    #DodajUTabelu("https://www.2kratings.com/teams/boston-celtics", output_file)
    #DodajUTabelu("https://www.2kratings.com/teams/brooklyn-nets", output_file)
    #DodajUTabelu("https://www.2kratings.com/teams/charlotte-hornets", output_file)
    #DodajUTabelu("https://www.2kratings.com/teams/chicago-bulls", output_file)
    #DodajUTabelu("https://www.2kratings.com/teams/cleveland-cavaliers", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/dallas-mavericks", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/denver-nuggets", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/detroit-pistons", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/golden-state-warriors", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/houston-rockets", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/indiana-pacers", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/los-angeles-clippers", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/los-angeles-lakers", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/memphis-grizzlies", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/miami-heat", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/milwaukee-bucks", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/minnesota-timberwolves", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/new-orleans-pelicans", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/new-york-knicks", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/oklahoma-city-thunder", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/orlando-magic", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/philadelphia-76ers", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/phoenix-suns", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/portland-trail-blazers", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/sacramento-kings", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/san-antonio-spurs", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/toronto-raptors", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/utah-jazz", output_file)
    DodajUTabelu("https://www.2kratings.com/teams/washington-wizards", output_file)

if __name__ == '__main__':
    main()