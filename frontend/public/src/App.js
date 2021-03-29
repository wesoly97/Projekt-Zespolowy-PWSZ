import './App.css';
import {BrowserRouter as Router, Route} from "react-router-dom";
import Test from "./pages/Test";
function App() {
  
  return (
    <Router>
    <Route path="/test" exact render={(props) => <Test/>} />
  
</Router>
  );
}

export default App;
