import { useState, useEffect } from "react";

export default function Home() {
  const [year, setYear] = useState("2024");
  const [league, setLeague] = useState("Ligue 1");
  const [rankings, setRankings] = useState([]);
  const [selectedTeam,setSelectedTeam] = useState(null);
  const [recentMatches, setRecentMatches] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:8000/api/rankings?year=${year}&league=${league.replace(/ /g, '')}`)
      .then((res) => res.json())
      .then((data) => setRankings(data))
      .catch((err) => console.error("Erreur lors du chargement :", err));
  }, [year, league]);

  const fetchRecentMatches = (team) => {
    fetch(`http://localhost:8000/api/recentmatches?team=${team}&league=${league.replace(/ /g, '')}&season=${parseInt(year)}`)
      .then((res) => res.json())
      .then((data) => setRecentMatches(data))
      .catch((err) => console.error("Erreur lors du chargement des matchs :", err));
  };


  const handleTeamClick = (team) => {
    setSelectedTeam(team);
    fetchRecentMatches(team.Teams);
  };

  return (
    <div className="min-h-screen flex flex-row items-center justify-center bg-gray-100 p-2">
      <div className="flex flex-col items-center">
        <div className="items-center flex space-x-10 p-0">
          <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-4xl dark:text-white">Classement  {league} - Saison {year}/{parseInt(year)+1}</h1>
          <select className="p-3 border rounded" onChange={(e) => setYear(e.target.value)}>
              {[...Array(25)].map((_, i) => {
                const season = 2024 - i;
                return <option key={season} value={season}>{season}</option>;
              })}
            </select>
        </div>
        
        <div className="flex flex-row items-center flex space-x-10 justify-center bg-gray-100 p-4">
            {[
              { name: "Ligue 1", flag: "france" },
              { name: "Premier League", flag: "england" },
              { name: "Serie A", flag: "italy" },
              { name: "Liga", flag: "spain" },
              { name: "Bundesliga", flag: "germany" },
            ].map((l) => (
              <img
                key={l.name}
                src={`/Flags.svg#${l.flag}`}
                alt={l.name}
                width={70}
                height={35}
                className={`cursor-pointer ${league === l.name ? "border-2" : ""}`}
                onClick={() => setLeague(l.name)}
              />
            ))}
          </div>

        <table className="table-auto border-collapse border border-gray-400">
          <thead>
            <tr className="bg-gray-300">
              <th className="border p-2">Équipe</th>
              <th className="border p-2">Points</th>
              <th className="border p-2">Buts marqués</th>
              <th className="border p-2">Buts encaissés</th>
              <th className="border p-2">Goal average</th>
            </tr>
          </thead>
          <tbody>
            {rankings.length > 0 ? (
              rankings.map((team, index) => (
                <tr key={index} className="bg-white">
                  <td className="border p-2 flex space-x-2 items-center font-bold cursor-pointer" onClick={() => handleTeamClick(team)}>{<img src={`/${team.Teams.replace(/ /g, '')}.svg`} alt={`${team.Teams} logo`} width={15} height={5}/> }{<span>{team.Teams}</span>}</td>
                  <td className="border p-2">{team.Points}</td>
                  <td className="border p-2">{team.ScoredGoals}</td>
                  <td className="border p-2">{team.TakenGoals}</td>
                  <td className="border p-2">{team.GoalAverage}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="3" className="border p-2 text-center">Chargement...</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
      {/* Détails de l'équipe sélectionnée */}
      {/* Détails de l'équipe sélectionnée */}
      {selectedTeam && (
        <div className="w-1/3 p-4 bg-white shadow-lg rounded-lg border border-gray-300 transition-all duration-300">
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-bold mb-2">{selectedTeam.Teams}</h2>
            <img className="" src={`/${selectedTeam.Teams.replace(/ /g, '')}.svg`} alt={`${selectedTeam.Teams} logo`} width={100} height={100}/>
          </div>
          <h3 className="text-xl font-bold mt-4">5 Derniers Matchs</h3>
          <div className="flex space-x-1">
            {recentMatches.map((match,i) => {
            const isHomeTeam = match.HomeTeam === selectedTeam.Teams;
            const isAwayTeam = match.AwayTeam === selectedTeam.Teams;
            let result = "";

            if (match.FTR == "D") {
              return (<span className="bg-orange-500 text-white rounded-md px-2 py-1 text-sm">D</span>)
            }
              else if ((isHomeTeam && match.FTR == "H") | (isAwayTeam && match.FTR == "A") ) {
                return(<span className="bg-green-500 text-white rounded-md px-2 py-1 text-sm">V</span>) 
              }
                else if ((isHomeTeam && match.FTR == "A") | (isAwayTeam && match.FTR == "H") ) {
                  return(<span className="bg-red-500 text-white rounded-md px-2 py-1 text-sm">L</span>)
                }

            })}
          </div>

          {recentMatches.length > 0 ? (
            <ul className="mt-2">
              {recentMatches.map((match, i) => (
                <li key={i} className="border-b py-1 flex justify-between">
                  <span className="w-1/4 flex space-x-2 items-center font-bold">{<img src={`/${match.HomeTeam.replace(/ /g, '')}.svg`} alt={`${match.HomeTeam} logo`} width={20} height={10}/> }{<span>{match.HomeTeam}</span>}</span>
                  <span className="w-1/8 text-center">{match.FTHG}</span>
                  <span className="w-1/8 text-center">{match.FTAG}</span>
                  <span className="w-1/4 flex space-x-2 items-center font-bold">{<img src={`/${match.AwayTeam.replace(/ /g, '')}.svg`} alt={`${match.AwayTeam} logo`} width={20} height={10}/> }{<span>{match.AwayTeam}</span>}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="text-gray-500">Chargement des derniers matchs...</p>
          )}

          <button
            className="mt-4 bg-red-500 text-white px-4 py-2 rounded hover:bg-red-700"
            onClick={() => setSelectedTeam(null)}
          >
            Fermer
          </button>
        </div>
      )}

    </div>
  );
}
