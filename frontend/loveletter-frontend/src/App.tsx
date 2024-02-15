import React, { useState } from 'react';
import 'bulma/css/bulma.min.css'
import { Button, Card, Container } from 'react-bulma-components'
import Display from './components/Display';
import axios from 'axios';
import { outputInterface } from './interface';

const msg: any[] = []

function App() {
  const [message, setMessage] = useState<outputInterface[]>([]);

  React.useEffect(() => {
    start();
  // eslint-disable-next-line react-hooks/exhaustive-deps
    main();
  },[]);

  function main() {
    setTimeout(playerTurn, 3000);
  }

  async function start() {
    await axios.get("http://localhost:8000/")
      .then((response) => {
        const tmp: any[] = [];
        msg.push(response.data);
        setMessage(tmp);
      })
      .catch((err) => {
        console.log(err);
      });
  }

  async function playerTurn() {
    await axios.get("http://localhost:8000/player")
      .then((response) => {
        const tmp: any[] = [];
        msg.push(...response.data);
        setMessage(tmp);
      })
      .catch((err) => {
        console.log(err);
      });
  }

  return (
    <Container breakpoint={'mobile'} backgroundColor='light'>
      &nbsp;
      <Display message={msg.toString()}></Display>
      &nbsp;
      <div style={{textAlign: 'center'}}>
        <input style={{width: 370, margin: "10px"}} className="input is-primary" type="text" placeholder="> input command" />
      </div>
      <Card style={{width: 370, margin: 'auto', height: 120, whiteSpace: 'nowrap'}} backgroundColor='info'>
        <Card.Content>
          <Button size='medium' style={{ width: 130 }} m={3} color='primary'>execute</Button>
          <Button size='medium' style={{ width: 130 }} m={3} color='danger'>cancel</Button>
        </Card.Content>
      </Card>
    </Container>
  );
}

export default App;
