import requests
import bs4


def gen_all_links():
    return [f"https://www.rarepalmseeds.com/az/{letter}?limit=20000" for letter in "qwertyuiopasdfghjklzxcvbnm"]


def find_plants(link):
    all_links = []
    soup = bs4.BeautifulSoup(requests.get(link).text, "html.parser")
    for palm_list in soup.find_all("div", class_="product-list"):
        for palm_element in palm_list.find_all("div", class_="name"):
            links = [a['href'] for a in palm_element.find_all("a")]
            assert len(links) == 1
            all_links.append(links[0].split('?')[0])
    assert len(all_links) != 20000
    return all_links


def find_all_plants():
    all_plants = []
    for link in gen_all_links():
        print(f"Processing {link}")
        for plant in find_plants(link):
            all_plants.append(plant)
    return all_plants


def main():
    print(find_all_plants())


if __name__ == "__main__":
    main()
