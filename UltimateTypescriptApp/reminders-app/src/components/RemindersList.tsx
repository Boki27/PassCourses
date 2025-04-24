import React from 'react';
import Reminder from '../models/Reminder';

interface RemiderListProps {
  items: Reminder[],
  onRemoveReminder: (id: number) => void;
}

function RemiderList({items, onRemoveReminder}: RemiderListProps) {
  return (
    <ul className='list-group'>
      {items.map(item =>
        <li className='list-group-item' key={item.id}>
          {item.title}
          <button onClick={() => onRemoveReminder(item.id)}className="btn btn-outline-danger mx-2 rounded-pill">Delete</button>
        </li>
      )}
    </ul>
  )
}

export default RemiderList;