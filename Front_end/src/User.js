import React from 'react';
import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';
import {useMutation } from 'react-apollo';

const QUERY_USERS = gql`
  query {
    peers {
      id
      name
      
    }
}
`;
export function UserInfo() {
  // Polling: provides near-real-time synchronization with
  // your server by causing a query to execute periodically
  // at a specified interval
  const { data, loading } = useQuery(
    QUERY_USERS, {
      pollInterval: 500 // refetch the result every 0.5 second
    }
  );
  
  // should handle loading status
  if (loading) return <p>Loading...</p>;
   
  return data.peers.map(({ id, name}) => (
    <div key={id}>
      <p>
        Peer - {id}: {name} 
      </p>
    </div>
  ));
}

const CREATE_PEER = gql/*`
  mutation createPeer($name: String!){
    createPeer (name: $name){
      peer{
        id
        name
      }
      
  }
}
`*/
`mutation createPeer($name:String!){
  createPeer(input: {
    name: "Tom Hans"
  }) {
    ok
    peer {
      id
      name
    }
  }
}`
;
export function CreatePeer() {
  let inputName;
  const [createPeer, { data }  ] = useMutation(CREATE_PEER);
  return (
    <div>
      <form
        onSubmit={e => {
          e.preventDefault();
          createPeer({ variables: {
            name: inputName.value,
            
        } });
        inputName.value = '';
        window.location.reload();
      }}
      style = {{ marginTop: '2em', marginBottom: '2em' }}
     >
     <label>Name: </label>
     <input
       ref={node => {
         inputName = node;
       }}
       style={{ marginRight: '1em' }}
     />
     
     
     <button type="submit" style={{ cursor: 'pointer' }}>Add a User</button>
    </form>
   </div>
  );}
