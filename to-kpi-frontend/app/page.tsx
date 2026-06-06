'use client';

import { useState } from 'react';

export default function Home() {
  const [jdText, setJdText] = useState('');
  const [kpiData, setKpiData] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleAnalyze = async () => {
    setIsLoading(true);
    setKpiData(null);
    
    try {
      const response = await fetch('http://127.0.0.1:8000/api/analyze-jd', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: jdText }),
      });
      
      const data = await response.json();
      setKpiData(data);
      
    } catch (error) {
      console.error('エラー:', error);
      alert('通信に失敗しました。バックエンドが起動しているか確認してください。');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="p-8 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">To KPI</h1>
      
      <textarea
        className="w-full h-40 p-3 border rounded mb-4"
        placeholder="企業の募集要項（JD）をここにコピペ..."
        value={jdText}
        onChange={(e) => setJdText(e.target.value)}
      />
      
      <button
        onClick={handleAnalyze}
        disabled={isLoading || !jdText}
        className="bg-blue-600 text-white px-6 py-2 rounded disabled:bg-gray-400"
      >
        {isLoading ? 'AIが分析中...' : 'KPIに変換する'}
      </button>

      {kpiData && (
        <div className="mt-8 p-6 bg-gray-50 border rounded shadow-sm">
          <h2 className="text-xl font-bold mb-4">あなたのアクションプラン（KPI）</h2>
          <pre className="whitespace-pre-wrap bg-white p-4 border rounded overflow-x-auto text-sm">
            {JSON.stringify(kpiData, null, 2)}
          </pre>
        </div>
      )}
    </main>
  );
}
