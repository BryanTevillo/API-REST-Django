import logo from "./logo.svg";
import "./App.css";
import PizzaList from "./pizzerias/pizzeriaslist";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img
          src="https://images.hola.com/imagenes/cocina/recetas/20220208204252/pizza-pepperoni-mozzarella/1-48-890/pepperoni-pizza-abob-t.jpg"
          className="App-logo"
          alt="logo"
        />
        <p>"Aplicación web para amantes de la pizza"</p>
        <h1
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          My pizza vs My pizza App
        </h1>
        <PizzaList />
      </header>
    </div>
  );
}

export default App;
