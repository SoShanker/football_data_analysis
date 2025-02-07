import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

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

        # league_id = self.leagues[league]
        # req = requests.get(f"https://datahub.io/core/{league_id}",headers=self.headers)
        # soup = BeautifulSoup(req.content, 'html.parser')

        # try:
        #     season_str = f"{str(season)[2:]}{str(season+1)[2:]}"
        #     csv_link = [s for s in soup.findAll('tr', {'class': 'even:bg-gray-50'}) if s.find("a",{"href":f"#season-{season_str}"})][0].find("a",{"target":"_blank"})["href"]
        #     if not csv_link.startswith('http'):
        #             csv_link = 'https://datahub.io' + csv_link
        #     # Now download the CSV as before
        #     csv_response = requests.get(csv_link)
        #     if csv_response.status_code == 200:
        #         league_path = os.path.join(self.path, league)
        #         os.makedirs(league_path, exist_ok=True)
                
        #         file_path = os.path.join(league_path, f'season{season}-{season+1}.csv')
        #         with open(file_path, 'wb') as file:
        #             file.write(csv_response.content)
        #         print(f'CSV file downloaded successfully: {file_path}')
        #     else:
        #         print(f"Échec du téléchargement: {csv_link}")
        # except Exception as e:
        #     print(f"Erreur lors de la récupération du fichier pour {league} {season}: {e}")
            

    def download_all_data_since_2000(self):
        for league in self.leagues:
            print(f"Téléchargement pour {league}")
            for year in range(2000, 2025):
                print(f"Saison {year}-{year+1}")
                self.download_file(league, year)
            self.create_global_file(league)

    def update_ongoing_season(self, ongoing_season=2024):
        for league in self.leagues:
            print(f"Mise à jour pour {league}, saison {ongoing_season}-{ongoing_season+1}")
            self.download_file(league, ongoing_season)
            self.create_global_file(league)

    def create_global_file(self,league):
        path = self.path + f"/{league}"
        # Create a line that will separate each season 
        columns = ["Date","HomeTeam","AwayTeam","FTR","FTHG","FTAG","HTHG","HTAG"]
        endofseasondf = pd.DataFrame(columns=columns)
        entry = pd.DataFrame.from_dict({
            "Date":["End of season"],
            "HomeTeam":[None],
            "AwayTeam":[None],
            "FTR":[None],
            "FTHG":[None],
            "FTAG":[None],
            "HTHG":[None],
            "HTAG":[None]
        })
        endofseasondf = pd.concat([endofseasondf, entry], ignore_index=True)

        seasons = pd.DataFrame(columns=columns)
        for file in os.listdir(path):
            data = pd.read_csv(path +f"/{file}")
            data_light = data[columns]
            seasons = pd.concat([seasons,data_light,endofseasondf])

        seasons.to_csv(path+"/Allseasons.csv")


if __name__ == "__main__":
    downloader = BulkDownload("FootballData")
    downloader.download_all_data_since_2000()

    