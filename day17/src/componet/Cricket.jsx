import React, { useState } from 'react';
import RemainingOvers from './RemainingOvers'; 

const Cricket = ({ props }) => {
  const { totalOvers } = props;
  const [runs, setRuns] = useState(0);
  const [wickets, setWickets] = useState(0);
  const [ball, setBall] = useState(0);

  const totalBalls = totalOvers * 6;
  const remainingBalls = totalBalls - ball;

  let allOut = 0;
if (wickets == 10) {
  allOut = 1;
}
;
  let allOvers = 0;
if (ball == totalBalls) {
  allOvers = 1;
}

  const gameEnded = allOut + allOvers;

  const over = parseInt(ball / 6);
  const currentBall = ball % 6; 

  const remainingOver = parseInt(remainingBalls / 6);
  const remainingBall = remainingBalls % 6;

  const handleScore = (score) => {
    const play= (1 - gameEnded);
    setRuns(runs + (play * score));
    setBall(ball + play);
  };

  const handleWicket = () => {
    
    const play = (1 - gameEnded);
    setWickets(wickets + play);
    setBall(ball + play);
   
  };

  return (
    <div>
      <h2>Score: {runs}/{wickets}</h2>
     
      <h2>Overs: {over}.{currentBall}</h2>
      

      <RemainingOvers props={{ totalOvers: totalOvers, ball: ball }} />

      {gameEnded == 0 && 
        <div style={{ margin: '20px' }}>
          <button onClick={() => handleScore(6)}>Six</button>
          <button onClick={() => handleScore(4)}>Four</button>
          <button onClick={() => handleScore(3)}>Three</button>
          <button onClick={() => handleScore(2)}>Two</button>
          <button onClick={() => handleScore(1)}>One</button>
          <button onClick={() => handleWicket()}>Wicket</button>
        </div>
      
      
     };
      
    </div>
  );
};

export default Cricket;
