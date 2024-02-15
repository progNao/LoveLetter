import React from 'react';
import 'bulma/css/bulma.min.css';
import { Card } from 'react-bulma-components';
import { outputInterface } from '../interface';

class Display extends React.Component<outputInterface> {
  render(): React.ReactNode {
    const props = this.props;
    console.log(props)
    const msg = props.message.split(',');
    const list = [];
    for (const item of msg) {
      list.push(<li style={{ listStyleType: `'>'` }}>{ item }</li>)
    }
    return (
      <div>
        <Card style={{width: 350, margin: 'auto', height: 450, overflow: 'auto'}} backgroundColor='primary'>
          <Card.Content textSize={5} backgroundColor='primary' textColor='white'>
            <ul>{ list }</ul>
          </Card.Content>
        </Card>
      </div>
    )
  };
}
export default Display;