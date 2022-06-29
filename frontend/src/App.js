import React,{ Component } from 'react';
import './App.css';
import TodoForm from './components/TaskForm';
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends Component{
  render(){
    return(
      <div className="App">
        <TodoForm/>
      </div>
    )
  }
}

export default App;
