import React from 'react';

function RemainingOvers({ props }) {
  const { totalOvers, ball } = props;
  const totalBalls = totalOvers * 6;
  const remaining = totalBalls - ball;

  const overs = parseInt(remaining / 6);
  const balls = remaining % 6;

  return (
    <h2>Remaining Overs: {overs}.{balls}</h2>
  );
}

export default RemainingOvers;
