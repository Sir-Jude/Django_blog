// Components
const NavBar = () => {
  return (
    <nav>
      <div class="nav-wrapper">
        <a href="#" class="brand-logo">
          DCI IMDB
        </a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
          <li>
            <a href="sass.html">Sass</a>
          </li>
          <li>
            <a href="badges.html">Components</a>
          </li>
          <li>
            <a href="collapsible.html">JavaScript</a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

// Entrypoint for components
const App = () => {
  return (
    <div>
      <NavBar />
      <div className="container">
        <input placeholder="search movie database" />
        <button>Search</button>
      </div>
    </div>
  );
};

ReactDOM.render(<App />, document.querySelector("#root"));
