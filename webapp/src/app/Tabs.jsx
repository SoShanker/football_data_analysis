import React, { useState } from 'react';
import FootballRanking from './FootballRanking'; // Import the Home component

function Tabs() {
  const [activeTab, setActiveTab] = useState(1);  // Initially, Tab 1 is active

  return (
    <div className="w-full mx-auto ">
      <div className="flex border-b-2">
        <div
          className={`tab px-4 py-2 cursor-pointer ${activeTab === 1 ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-500 hover:text-gray-700'}`}
          onClick={() => setActiveTab(1)}
        >
          Classements
        </div>
        <div
          className={`tab px-4 py-2 cursor-pointer ${activeTab === 2 ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-500 hover:text-gray-700'}`}
          onClick={() => setActiveTab(2)}
        >
          Matches and calendar
        </div>
        <div
          className={`tab px-4 py-2 cursor-pointer ${activeTab === 3 ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-500 hover:text-gray-700'}`}
          onClick={() => setActiveTab(3)}
        >
          Betting
        </div>
      </div>

      <div className="tab-content mt-8 p-2">
        {activeTab === 1 && (
          <div className="p-4">
            {/* Render the Home component in Tab 1 */}
            <FootballRanking />
          </div>
        )}
        {activeTab === 2 && (
          <div className="p-4 bg-green-100 rounded-md shadow-md">
            <h2 className="text-xl font-semibold">Content for Tab 2</h2>
            <p>Here the future matches for each team, statistics and stuff;</p>
          </div>
        )}
        {activeTab === 3 && (
          <div className="p-4 bg-red-100 rounded-md shadow-md">
            <h2 className="text-xl font-semibold">Content for Tab 3</h2>
            <p>Here the prediction about future matches</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Tabs;
