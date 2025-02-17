import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

from Variables import *
class BulkDownload:
    def __init__(self, download_path):
        self.path = download_path
        self.leagues = {
            "PremierLeague":"english-premier-league",
            "Ligue1" : "french-ligue-1",
            "Bundesliga":"german-bundesliga",
            "SerieA":"italian-serie-a",
            "Liga":"spanish-la-liga"
        }
        self.ongoing_season = 2024
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

    def download_file(self, league, season):
        if league not in self.leagues:
            print(f"Ligue inconnue: {league}")
            return
        
        league_id = self.leagues[league]
        season_str = f"{str(season)[2:]}{str(season+1)[2:]}"
        csv_response = requests.get(f"https://datahub.io/core/{league_id}/_r/-/season-{season_str}.csv")
        if csv_response.status_code == 200:
            league_path = os.path.join(self.path, league)
            os.makedirs(league_path, exist_ok=True)
            
            file_path = os.path.join(league_path, f'season{season}-{season+1}.csv')
            with open(file_path, 'wb') as file:
                file.write(csv_response.content)
            print(f'CSV file downloaded successfully: {file_path}')
        else:
            print(f"Échec du téléchargement: {league} - {season}")
            

    def download_all_data_since_2000(self):
        for league in self.leagues:
            print(f"Téléchargement pour {league}")
            for year in range(2000, 2025):
                print(f"Saison {year}-{year+1}")
                self.download_file(league, year)
                self.unique_names(league,year)

    def update_ongoing_season(self):
        for league in self.leagues:
            print(f"Mise à jour pour {league}, saison {self.ongoing_season}-{self.ongoing_season+1}")
            self.download_file(league, self.ongoing_season)
            self.unique_names(league,self.ongoing_season)

    def unique_names(self,league:str,year:int):
        def replace_names(l):
            return l.replace(UNIQUE_NAMES)

        file_path = os.path.join(self.path, league,f'season{year}-{year+1}.csv')
        file = pd.read_csv(file_path)
        file["HomeTeam"].apply(replace_names)
        file["AwayTeam"].apply(replace_names)
        file.to_csv(file_path)

if __name__ == "__main__":
    downloader = BulkDownload("FootballData")
    #If it's the first launch, run 
    downloader.download_all_data_since_2000()
    #Else update only
    # downloader.update_ongoing_season()

    