import logo from './logo.svg';
import Cricket from './componet/Cricket';

function App(){
  const props = {
    totalOvers: 20
  };
  return(
    <div>
      <Cricket  props={props}/>
     </div>
  );
}
export default App;
