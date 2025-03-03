import { useState, useEffect } from "react";

export default function Home() {
  const [year, setYear] = useState("2024");
  const [league, setLeague] = useState("Ligue 1");
  const [rankings, setRankings] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:8000/api/rankings?year=${year}&league=${league.replace(/ /g, '')}`)
      .then((res) => res.json())
      .then((data) => setRankings(data))
      .catch((err) => console.error("Erreur lors du chargement :", err));
  }, [year, league]);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-2">
      <div className="items-center flex space-x-10 p-0">
        <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-4xl dark:text-white">Classement  {league} - Saison {year}/{parseInt(year)+1}</h1>
        <select className="p-3 border rounded" onChange={(e) => setYear(e.target.value)}>
            <option value="2024">2024</option>
            <option value="2023">2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
            <option value="2017">2017</option>
            <option value="2016">2016</option>
            <option value="2015">2015</option>
            <option value="2014">2014</option>
            <option value="2013">2013</option>
            <option value="2012">2012</option>
            <option value="2011">2011</option>
            <option value="2010">2010</option>
            <option value="2009">2009</option>
            <option value="2008">2008</option>
            <option value="2007">2007</option>
            <option value="2006">2006</option>
            <option value="2005">2005</option>
            <option value="2004">2004</option>
            <option value="2003">2003</option>
            <option value="2002">2002</option>
            <option value="2001">2001</option>
            <option value="2000">2000</option>
        </select>
      </div>
      
      <div className="flex flex-row items-center flex space-x-10 justify-center bg-gray-100 p-4">
        <img src={'/Flags.svg#france'} alt="My Image" width={70} height={35} onClick={(e) => setLeague("Ligue 1")}/>
        <img src={'/Flags.svg#england'} alt="My Image" width={70} height={35} onClick={(e) => setLeague("Premier League")}/>
        <img src={'/Flags.svg#italy'} alt="My Image" width={70} height={35} onClick={(e) => setLeague("Serie A")}/>
        <img src={'/Flags.svg#spain'} alt="My Image" width={70} height={35} onClick={(e) => setLeague("Liga")}/>
        <img src={'/Flags.svg#germany'} alt="My Image" width={70} height={35} onClick={(e) => setLeague("Bundesliga")}/>
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
                <td className="border p-2 flex space-x-2 items-center font-bold">{<img src={`/${team.Teams.replace(/ /g, '')}.svg`} alt={`${team.Teams} logo`} width={15} height={5}/> }{<span>{team.Teams}</span>}</td>
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
  );
}
