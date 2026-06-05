// app/page.tsx (フェーズ1)
'use client'; // ← これを書くことで「ユーザーのブラウザ上で動くコンポーネント」になる

import { useState } from 'react';

export default function Home() {
  // jdText: 現在の入力内容 / setJdText: 入力内容を更新する関数
  const [jdText, setJdText] = useState('');

  return (
    <main className="p-8 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">To KPI - 募集要項をアクションに変える</h1>
      
      <textarea
        className="w-full h-40 p-3 border rounded mb-4"
        placeholder="企業の募集要項（JD）をここにコピペ..."
        value={jdText}
        // 文字が入力されるたびに、setJdTextが走って変数を上書きする
        onChange={(e) => setJdText(e.target.value)}
      />
      
      {/* 入力した文字がリアルタイムに下に表示されるか体感してみてください */}
      <div className="p-4 bg-gray-100 rounded">
        <p className="font-bold">現在の入力内容（リアルタイム確認）:</p>
        <p>{jdText}</p>
      </div>
    </main>
  );
}
