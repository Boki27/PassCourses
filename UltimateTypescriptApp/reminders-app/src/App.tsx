import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import RemiderList from './components/RemindersList';
import Reminder from './models/Reminder';
import ReminderService from './services/reminder';
import NewReminder from './components/NewReminder';

function App() {
  const [reminders, setReminders] = useState<Reminder[]>([]);

  useEffect(() => {
      loadReminders();
    }, []
  );

  const loadReminders = async () => {
    const srwReminders = await ReminderService.getReminders();
    setReminders(srwReminders);
  }

  const removeReminder = (id: number) => {
    const updatedRemindersList = reminders.filter(reminder => reminder.id !== id);
    setReminders(updatedRemindersList);
  }

  const addReminder = async (title: string) => {
    const newReminder = await ReminderService.addReminder(title);
    setReminders([newReminder, ...reminders]);
  }

  return (
    <div className="App">
      <NewReminder onAddReminder={addReminder}/>
      <RemiderList items={reminders} onRemoveReminder={removeReminder}/>
    </div>
  );
}

export default App;
