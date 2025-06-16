import React, { useState } from 'react';

const Cricket = () => {
  const [runs, setRuns] = useState(0);
  const [wickets, setWickets] = useState(0);
  const [balls, setBalls] = useState(0);

  const ballsPerOver = 6; 
  const maxOvers = 20;
  const maxBalls = ballsPerOver * maxOvers; 
  const maxWickets = 10;

  const isAllOut = wickets >= maxWickets;
  const isOverComplete = balls >= maxBalls;
  
  let matchOver;
if (isAllOut) {
  matchOver = true;
} else {
  matchOver = isOverComplete;
};

  const addRuns = (run) => {
    if (matchOver) return;

    setRuns(runs + run);
    updateBall();
  };

  const addWicket = () => {
    if (matchOver) return;

    const newWickets = wickets + 1;
    setWickets(newWickets);
    updateBall();

    if (newWickets >= maxWickets) {
      alert('All Out!');
    }
  };

  const updateBall = () => {
    const newBalls = balls + 1;
    setBalls(newBalls);

    if (newBalls >= maxBalls && isAllOut) {
      alert('Overs Complete!');
    }
  };

  const getOvers = () => {
    const over = (balls / ballsPerOver);
    const ball = balls % ballsPerOver;
    return over + '.' + ball;
  };

  const getRemaining = () => {
    const remBalls = maxBalls - balls;
    const remOvers = (remBalls / ballsPerOver);
    const remBall = remBalls % ballsPerOver;
    return remOvers + '.' + remBall;
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1> Match Score </h1>
      <h2>Score: {runs}/{wickets}</h2>
      <h3>Overs: {getOvers()} / 20</h3>
      <h4>Remaining: {getRemaining()} overs</h4>

      {!matchOver && (
        <div style={{ margin: '20px ' }}>
          <button onClick={() => addRuns(6)}>Six</button>
          <button onClick={() => addRuns(4)}>Four</button>
          <button onClick={() => addRuns(2)}>Two</button>
          <button onClick={() => addRuns(3)}>Three</button>
          <button onClick={() => addRuns(1)}>One</button>
          <button onClick={addWicket}>Wicket</button>
        </div>
      )}
    </div>
  );
};

export default Cricket;
