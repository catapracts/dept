import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
    const [inputValue, setInputValue] = useState('');
    const [storedValue, setStoredValue] = useState('');

    const handleChange = (event) => {
        setInputValue(event.target.value);
    };

    const handleAdd = async () => {
        const response = await fetch('/add', { // 프록시 경로 사용
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ value: inputValue }),
        });
        if (response.ok) {
            setInputValue('');
            fetchLatestValue();
        }
    };
    
    const fetchLatestValue = async () => {
        const response = await fetch('/get'); // 프록시 경로 사용
        if (response.ok) {
            const data = await response.json();
            setStoredValue(data.value);
        }
    };

    // 페이지 로딩 시 최신 값 한 번 불러오기
    useEffect(() => {
      fetchLatestValue();
  }, []);

    return (
        <div className="App">
            <header className="App-header">
                <h1>FastAPI + React Example</h1>
                <div className="input-section">
                    <input
                        type="text"
                        value={inputValue}
                        onChange={handleChange}
                        placeholder="Enter a value"
                    />
                    <button onClick={handleAdd}>Add</button>
                </div>
                <div className="value-section">
                    <button onClick={fetchLatestValue}>Get Latest Value</button>
                    {storedValue && (
                        <>
                            <h2>Latest Stored Value:</h2>
                            <p>{storedValue}</p>
                        </>
                    )}
                </div>
            </header>
        </div>
    );
}

export default App;
