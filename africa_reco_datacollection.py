import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# non_african_cities = [
#     "Bangkok", "Paris", "London", "Dubai", "Singapore", "Kuala Lumpur",
#     "New York City", "Istanbul", "Tokyo", "Seoul", "Antalya", "Phuket",
#     "Mecca", "Hong Kong", "Milan", "Palma de Mallorca", "Barcelona", 
#     "Pattaya", "Osaka", "Vienna", "Rome", "Riyadh", "Guangzhou", "Taipei",
#     "Medina", "Prague", "Shanghai", "Los Angeles", "Amsterdam", "Miami",
#     "Las Vegas", "Denpasar", "Ho Chi Minh City", "Sydney", "Berlin",
#     "Madrid", "Athens", "Moscow", "Cancún", "Orlando", "Toronto", "Beijing",
#     "Lisbon", "Florence", "Dublin", "Saint Petersburg", "Brussels", "Jakarta",
#     "Mexico City", "Rio de Janeiro", "Santiago", "Lima", "Bogota", "Caracas",
#     "Montevideo", "Buenos Aires", "Hanoi"
# ]



city_names = [
    "Bangkok", "Paris", "London", "Dubai", "Singapore", "Kuala Lumpur",
    "New York City", "Istanbul", "Tokyo", "Seoul", "Antalya", "Phuket",
    "Mecca", "Hong Kong", "Milan", "Palma de Mallorca", "Barcelona", 
    "Pattaya", "Osaka", "Vienna", "Rome", "Riyadh", "Guangzhou", "Taipei",
    "Medina", "Prague", "Shanghai", "Los Angeles", "Amsterdam", "Miami",
    "Las Vegas", "Denpasar", "Ho Chi Minh City", "Sydney", "Berlin",
    "Madrid", "Athens", "Moscow", "Cancún", "Orlando", "Toronto", "Beijing",
    "Lisbon", "Florence", "Dublin", "Saint Petersburg", "Brussels", "Jakarta",
    "Mexico City", "Rio de Janeiro", "Santiago", "Lima", "Bogota", "Caracas",
    "Montevideo", "Buenos Aires", "Hanoi",
    "Cairo", "Nairobi", "Cape Town", "Lagos", "Marrakech", "Tunis",
    "Algiers", "Harare", "Maputo", "Abidjan", "Dar es Salaam", "Addis Ababa",
    "Kampala", "Dakar", "Accra", "Luanda", "Bamako", "Freetown", "Kigali",
    "Kinshasa", "Libreville", "Lilongwe", "Windhoek", "Port Louis", 
    "Victoria, Seychelles", "Pretoria", "Lusaka", "Gaborone", "Nouakchott", 
    "Monrovia", "N'Djamena", "Mogadishu", "Djibouti City", "Malabo", 
    "São Tomé", "Praia", "Banjul", "Bissau", "Conakry", "Lomé", 
    "Ouagadougou", "Yaoundé", "Rabat"
]



criteria = [
    "Cuisine",
    "Accessibility",
    "Cultural Experience",
    "Shopping",
    "Festivals and Events",
    "Natural Scenery",
    "Urban Scenery"
]


# Wikipediaから都市情報を取得する関数
def get_wikipedia_content(title):
    url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', class_='mw-content-ltr mw-parser-output').get_text()
        return content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {title}: {e}")
        return ""

# 評価を推測する関数
def estimate_ratings(content):
    # 各評価基準に対するキーワード
    keywords = {
        "Cuisine": ["food", "cuisine", "dining", "restaurant", "delicious", "local dishes", "street food", "gourmet", "culinary", "eat", "eating", "meals"],
        "Accessibility": ["accessible", "access", "transport", "transportation", "reach", "reachable", "easy to get to", "public transport", "airport", "connectivity", "connected", "bus", "train", "metro", "transit", "tram", "subway", "commute", "commuting", "traveled"],
        "Cultural Experience": ["culture", "cultural", "heritage", "historic", "historical", "ancient", "landmark", "monument", "history", "archaeological", "traditional", "traditions", "custom", "customs", "historically", "heritage site", "culturally"],
        "Shopping": ["shopping", "market", "markets", "souvenir", "souvenirs", "shop", "shops", "mall", "malls", "retail", "retailers", "boutiques", "outlets", "purchase", "purchasing", "buy", "buying"],
        "Festivals and Events": ["festival", "festivals", "event", "events", "celebration", "celebrate", "celebrating", "parade", "annual", "yearly", "traditional", "concert", "concerts", "fair", "fairs", "festivities", "happening"],
        "Natural Scenery": ["nature", "natural", "scenic", "scenery", "landscape", "landscapes", "outdoors", "outdoor", "park", "parks", "reserve", "reserves", "wildlife", "natural beauty", "mountains", "mountain", "rivers", "river", "forest", "forests", "countryside"],
        "Urban Scenery": ["cityscape", "skyline", "urban", "architecture", "buildings", "modern", "skyscrapers", "skyscraper", "streets", "street", "cityscapes", "metropolitan", "urban beauty", "downtown"]
    }

    ratings = {}
    for criterion, words in keywords.items():
        score = sum(content.lower().count(word) for word in words)  # キーワードの出現回数でスコアを計算
        ratings[criterion] = score  # スコアを1-10にスケール

    return ratings

# データフレームの作成
data = []
for city in city_names:
    content = get_wikipedia_content(city)
    if content:
        ratings = estimate_ratings(content)
        ratings["City"] = city
        data.append(ratings)

df = pd.DataFrame(data, columns=["City"] + criteria)
# df.to_csv('sightseeing_places_ratings.csv')　download as csv file
# print(df.head())
