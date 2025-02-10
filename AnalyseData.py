import pandas as pd
import os 

class AnalyzeFootballData:
    def __init__(self,download_path:str):
        self.path = download_path
        self.leagues = {
            "PremierLeague":"english-premier-league",
            "Ligue1" : "french-ligue-1",
            "Bundesliga":"german-bundesliga",
            "SerieA":"italian-serie-a",
            "Liga":"spanish-la-liga"
        }
        self.ongoingseason = "2024-2025"
    
    def compute_ranking(self,league:str,year:int):
        '''
        Calculate ranking from results
        Input : League name and starting year of the season
        Output : DataFrame of the results
        '''
        season_df = pd.read_csv(os.path.join(self.path,league,f"season{year}-{year+1}.csv"))
        teams = list(season_df["HomeTeam"].drop_duplicates())
        scores = {team : 0 for team in teams}

        for i in range (len(season_df)):
            match = season_df.iloc[i]
            home_team,away_team = match["HomeTeam"],match["AwayTeam"]
            result = match["FTR"]
            if result == "H":
                scores[home_team]+=3
            elif result == "A":
                scores[away_team]+=3
            else:
                scores[away_team]+=1
                scores[home_team]+=1
            
        scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1],reverse=True)}

        final_ranking = pd.DataFrame()
        final_ranking["Team"] = list(scores.keys())
        final_ranking["Score"] = list(scores.values())
        return final_ranking

    def compute_win_lose_history(self,league:str):
        '''
        Create a list of results for each team
        Input : League name
        Output : Dictionnary <team_name,win_lose_history> 
        '''
        #TODO

    def compute_WDL_streaks(self,WDL_history:dict):
        '''
        From the WinDrawLoss history, compute the max wins, draws and loses streaks
        Input : WinDrawLoss history (from previous function)
        Output : Dict of the max streaks
        '''
        #TODO

    def compute_current_streaks(self,league:str):
        '''
        Compute current results streaks for each team in actual season
        Input : League name
        Output : Dict of the actual streaks
        '''
        #TODO


if __name__ == "__main__":
    analysis = AnalyzeFootballData("FootballData")