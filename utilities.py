# version 1.0

from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv
import random

# List of User-Agents - select at random when scraping to prevent some websites from blocking our requests
user_agents_list = [
'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
]

def scrape_movies():
    """
    Scraps the top-250 movie titles, ratings and popularity scores from the website 'https://www.imdb.com/chart/top/' and stores them into a csv file
    """
    response = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    # Iterate over each movie url from the website
    for movie in soup.select('.lister-list tr'):
        movie_url = 'https://www.imdb.com' + movie.select_one('.titleColumn a')['href']
        movie_response = requests.get(movie_url, headers={'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': random.choice(user_agents_list)})
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

        # [1] - Scrap through labels to find Titles

        # Title
        title = movie_soup.find('h1').text
        
        # [2] - Scrap through labels to find Rating info
        rating_0 = movie_soup.find('div', attrs={'data-testid': 'hero-rating-bar__aggregate-rating__score'})

        # Rating
        rating = rating_0.span.text
        
        # [3] - Scrap through labels to find Popularity info
        popularity_0 = movie_soup.find_all('div', attrs={'data-testid': 'hero-rating-bar__popularity__score'})

        # Popularity
        for p_0 in popularity_0:
            if p_0.text != None:
                popularity = p_0.text
                break        
        
        # Append to list of movies
        movies.append([title, rating, popularity])

    # Write the movie information to a CSV file with UTF-8 encoding
    with open('staging/movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow(movie)

def scrape_titles():
    """
    Scraps the top 250 movie titles from the website 'https://www.imdb.com/chart/top/' and stores them into a csv file
    """
    response = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    # Iterate over each movie url from the website
    for movie in soup.select('.lister-list tr'):
        movie_url = 'https://www.imdb.com' + movie.select_one('.titleColumn a')['href']
        movie_response = requests.get(movie_url, headers={'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': random.choice(user_agents_list)})
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

        # 1 - Scrap through labels to find Title info

        # Title
        title = movie_soup.find('h1').text
        
        # Append to list of titles
        movies.append([title])

    # Write the movie information to a CSV file with UTF-8 encoding
    with open('staging/titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow(movie)

def scrape_ratings():
    """
    Scraps the top 250 movie ratings from the website 'https://www.imdb.com/chart/top/' and stores them into a csv file
    """
    response = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    # Iterate over each movie url from the website
    for movie in soup.select('.lister-list tr'):
        movie_url = 'https://www.imdb.com' + movie.select_one('.titleColumn a')['href']
        movie_response = requests.get(movie_url, headers={'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': random.choice(user_agents_list)})
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

        # 2 - Scrap through labels to find Rating info
        rating_0 = movie_soup.find('div', attrs={'data-testid': 'hero-rating-bar__aggregate-rating__score'})

        # Rating
        rating = rating_0.span.text
        
        # Append to list of titles
        movies.append([rating])

    # Write the movie information to a CSV file with UTF-8 encoding
    with open('staging/ratings.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow(movie)
            
def scrape_popularity():
    """
    Scraps the top 250 movie popularity ranks from the website 'https://www.imdb.com/chart/top/' and stores them into a csv file
    """
    response = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    # Iterate over each movie url from the website
    for movie in soup.select('.lister-list tr'):
        movie_url = 'https://www.imdb.com' + movie.select_one('.titleColumn a')['href']
        movie_response = requests.get(movie_url, headers={'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': random.choice(user_agents_list)})
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

        # 3 - Scrap through labels to find Popularity info
        popularity_0 = movie_soup.find_all('div', attrs={'data-testid': 'hero-rating-bar__popularity__score'})

        # Popularity
        for p_0 in popularity_0:
            if p_0.text != None:
                popularity = p_0.text
                break
        
        # Append to list of titles
        movies.append([popularity])

    # Write the movie information to a CSV file with UTF-8 encoding
    with open('staging/popularity.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow(movie)
            
def scrape_genres():
    """
    Scraps the top 250 movie genres from the website 'https://www.imdb.com/chart/top/' and stores them into a csv file
    """
    response = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    # Iterate over each movie url from the website
    for movie in soup.select('.lister-list tr'):
        movie_url = 'https://www.imdb.com' + movie.select_one('.titleColumn a')['href']
        movie_response = requests.get(movie_url, headers={'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': random.choice(user_agents_list)})
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

        # 4 - Scrap through labels to find Genres info
        genres_0 = movie_soup.find('div', class_='ipc-chip-list__scroller')
        genres_1 = genres_0.find_all('span', class_='ipc-chip__text')

        # Genres
        genres = [genre.text for genre in genres_1]
        
        # Append to list of titles
        movies.append([genres])

    # Write the movie information to a CSV file with UTF-8 encoding
    with open('staging/genres.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow(movie)

def scrape_actors():
    """
    Scraps the top 250 movie actors from the website 'https://www.imdb.com/chart/top/' and stores them into a csv file
    """
    response = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    # Iterate over each movie url from the website
    for movie in soup.select('.lister-list tr'):
        movie_url = 'https://www.imdb.com' + movie.select_one('.titleColumn a')['href']
        movie_response = requests.get(movie_url, headers={'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': random.choice(user_agents_list)})
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

        # 5 - Scrap through labels to find Actors info
        actors_0 = movie_soup.find_all('a', attrs={'data-testid': 'title-cast-item__actor'})

        # Actors
        actors = [a.text for a in actors_0]
        
        # Append to list of titles
        movies.append([actors])

    # Write the movie information to a CSV file with UTF-8 encoding
    with open('staging/actors.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow(movie)
            
def scrape_writers():
    """
    Scraps the top 250 movie writers from the website 'https://www.imdb.com/chart/top/' and stores them into a csv file
    """
    response = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    # Iterate over each movie url from the website
    for movie in soup.select('.lister-list tr'):
        movie_url = 'https://www.imdb.com' + movie.select_one('.titleColumn a')['href']
        movie_response = requests.get(movie_url, headers={'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': random.choice(user_agents_list)})
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

        # 6 - Scrap through labels to find Writers info
        writers_0 = movie_soup.find_all('li', class_='ipc-metadata-list__item')

        # Writers
        for w_0 in writers_0:
            if w_0.find('span') != None:
                if 'Writer' in w_0.find('span').text:
                    writers = [w.text for w in w_0.find_all('a')]
                    break
        
        # Append to list of titles
        movies.append([writers])

    # Write the movie information to a CSV file with UTF-8 encoding
    with open('staging/writers.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow(movie)
            
def scrape_directors():
    """
    Scraps the top 250 movie directors from the website 'https://www.imdb.com/chart/top/' and stores them into a csv file
    """
    response = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    # Iterate over each movie url from the website
    for movie in soup.select('.lister-list tr'):
        movie_url = 'https://www.imdb.com' + movie.select_one('.titleColumn a')['href']
        movie_response = requests.get(movie_url, headers={'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': random.choice(user_agents_list)})
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

        # 7 - Scrap through labels to find Directors info
        directors_0 = movie_soup.find_all('li', class_='ipc-metadata-list__item')

        # Directors
        for d_0 in directors_0:
            if d_0.find('span') != None:
                if 'Director' in d_0.find('span').text:
                    directors = [d.text for d in d_0.find_all('a')]
                    break
        
        # Append to list of titles
        movies.append([directors])

    # Write the movie information to a CSV file with UTF-8 encoding
    with open('staging/directors.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow(movie)
            
def scrape_reviews():
    """
    Scraps two reviews from the top 250 movie ranks in the website 'https://www.imdb.com/chart/top/' and stores them into a csv file
    """
    response = requests.get('https://www.imdb.com/chart/top/')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    # Iterate over each movie url from the website
    for movie in soup.select('.lister-list tr'):
        movie_url = 'https://www.imdb.com' + movie.select_one('.titleColumn a')['href']
        movie_response = requests.get(movie_url, headers={'Accept-Language': 'en-US,en;q=0.8', 'User-Agent': random.choice(user_agents_list)})
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')
        
        # Scrap through labels to find Reviews info
        reviews_0 = movie_soup.find('div', class_='ipc-overflowText ipc-overflowText--listCard ipc-overflowText--height-long ipc-overflowText--long ipc-overflowText--click ipc-overflowText--base')

        # Reviews
        reviews = [r.text for r in reviews_0 if r.text != '']  # One review
        
        # Append to list of titles
        movies.append([reviews])
        
    # Write the movie information to a CSV file with UTF-8 encoding
    with open('staging/reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for movie in movies:
            writer.writerow(movie)