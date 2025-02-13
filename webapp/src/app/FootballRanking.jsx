import { useState, useEffect } from "react";

export default function Home() {
  const [year, setYear] = useState("2023");
  const [league, setLeague] = useState("premier_league");
  const [rankings, setRankings] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:8000/api/rankings?year=${year}&league=${league}`)
      .then((res) => res.json())
      .then((data) => setRankings(data))
      .catch((err) => console.error("Erreur lors du chargement :", err));
  }, [year, league]);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-5">
      <h1 className="text-3xl font-bold mb-5">Classements de Football</h1>

      <div className="flex space-x-4 mb-5">
        <select className="p-2 border rounded" onChange={(e) => setYear(e.target.value)}>
          <option value="2023">2023</option>
          <option value="2022">2022</option>
          <option value="2021">2021</option>
        </select>

        <select className="p-2 border rounded" onChange={(e) => setLeague(e.target.value)}>
          <option value="premier_league">Premier League</option>
          <option value="la_liga">La Liga</option>
          <option value="serie_a">Serie A</option>
        </select>
      </div>

      <table className="table-auto border-collapse border border-gray-400">
        <thead>
          <tr className="bg-gray-300">
            <th className="border p-2">Position</th>
            <th className="border p-2">Équipe</th>
            <th className="border p-2">Points</th>
          </tr>
        </thead>
        <tbody>
          {rankings.length > 0 ? (
            rankings.map((team, index) => (
              <tr key={index} className="bg-white">
                <td className="border p-2">{team.Position}</td>
                <td className="border p-2">{team.Team}</td>
                <td className="border p-2">{team.Points}</td>
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
