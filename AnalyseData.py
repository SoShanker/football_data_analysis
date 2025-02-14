import pandas as pd
import os 

from Variables import *
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
        #TODO Check Retraits de points - Exemple Nice a eu un point retiré en 2021-2022 en penalité
        '''
        Calculate ranking from results
        Input : League name and starting year of the season
        Output : DataFrame of the results
        '''
        season_df = pd.read_csv(os.path.join(self.path,league,f"season{year}-{year+1}.csv"))
        teams = list(season_df["HomeTeam"].drop_duplicates())
        scores = {team : {"Points":0,"ScoredGoals":0,"TakenGoals":0} for team in teams}

        for i in range (len(season_df)):
            match = season_df.iloc[i]
            home_team,away_team = match["HomeTeam"],match["AwayTeam"]
            scores[home_team]["ScoredGoals"] += match["FTHG"]
            scores[away_team]["TakenGoals"] += match["FTHG"]
            scores[home_team]["TakenGoals"] += match["FTAG"]
            scores[away_team]["ScoredGoals"] += match["FTAG"]
            result = match["FTR"]
            if result == "H":
                scores[home_team]["Points"]+=3
            elif result == "A":
                scores[away_team]["Points"]+=3
            else:
                scores[home_team]["Points"]+=1
                scores[away_team]["Points"]+=1

        for team in teams:
            if year in POINTS_SANCTION[league]:
                if team in POINTS_SANCTION[league][year]:
                    print(f"{team} had a penality of {POINTS_SANCTION[league][year][team]} in {year}")
                    scores[team]["Points"] += POINTS_SANCTION[league][year][team]

        final_ranking = pd.DataFrame.from_dict(scores,orient="index")
        final_ranking["Teams"] = list(scores.keys())
        final_ranking["GoalAverage"] = final_ranking["ScoredGoals"] - final_ranking["TakenGoals"]
        final_ranking.sort_values(by=["Points","GoalAverage"],inplace=True,ascending=False,ignore_index=True)

        #Ranking was a bit akward during COVID-19, so we have to invert lines
        if year == 2019 and league == "Ligue1":
            final_ranking.iloc[[4, 5]] = final_ranking.iloc[[5, 4]].copy().values
            final_ranking.iloc[[9, 10]] = final_ranking.iloc[[10, 9]].copy().values

        final_ranking.to_csv(os.path.join(self.path,league,f"ranking_{year}-{year+1}.csv"))
        print(f"{league} : Ranking for season {year}-{year+1} successfully generated.")

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
    #If it's the first time you launch it, use :
    for league in analysis.leagues:
        for year in range(2000,2025):
            analysis.compute_ranking(league,year)
    #Else
    # for league in analysis.leagues:
    #     analysis.compute_ranking(league,analysis.ongoingseason)