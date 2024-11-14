import './App.css';
import './bootstrap.min.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Header from './components/Header';
import Home from './pages/Home'
import IssueBook from './pages/IssueBook'
import ReturnBook from './pages/ReturnBook'



function App() {
  return (
    <Router className="App">
    <Header />
    <Routes>
      
      <Route path ="/" element ={<Home />} exact />
      <Route path ="/issue" element ={<IssueBook />}  />
      <Route path ="/return" element ={<ReturnBook />}  />
     

      </Routes>



    </Router>
  );
}

export default App;
