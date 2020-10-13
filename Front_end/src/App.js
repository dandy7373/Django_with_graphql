import React from 'react';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';
import { UserInfo,CreatePeer } from './User'



const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql/', // your GraphQL Server 
});
const App = () => (
  <ApolloProvider client={client}>
    <div style={{
      backgroundColor: '#00000008',
      display: 'flex',
      justifyContent:'center',
      alignItems:'center',
      height: '100vh',
      flexDirection: 'column',
    }}>
      <h2>Welcome! Your Peers</h2>
      
      <UserInfo/>
    </div>
  </ApolloProvider>
);
export default App;


/*import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/

