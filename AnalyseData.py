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

    def compute_actual_teams(self,league:str):
        '''
        Check ongoing season teams
        Input : League name
        Output : List of teams name
        '''
        #TODO

    def compute_ranking(self,league:str,year:int):
        '''
        Calculate ranking from results
        Input : League name and starting year of the season
        Output : DataFrame of the results
        '''
        #TODO

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