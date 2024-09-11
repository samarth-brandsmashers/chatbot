import React, { useEffect, useState } from 'react';
import styles from "../styles/Chatbot.module.css";
import { Avatar, Button, IconButton, MenuItem, TextField } from '@mui/material';
import { CiSettings } from "react-icons/ci";
import { AiOutlineSend } from "react-icons/ai";
import axios from 'axios';

interface Message {
  id: number;
  text: string;
  user_id: number;
  suggestions?: string[];
}

const Chatbot = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState("");
  const [session_id] = useState("123");


  useEffect(() => {
    axios.get<Message[]>(`http://localhost:8000/messages/?session_id=${session_id}`)
      .then((response) => setMessages(response.data))
      .catch((error) => console.error("Error fetching messages:", error));
  }, [session_id]);


  const handleSendMessage = () => {
    const userMessage = { text: inputValue, user_id: 1 };

    if (inputValue.trim() == '') {
      alert("Please enter a message")
      return;
    }

    axios.post<Message>(`http://localhost:8000/messages/?session_id=${session_id}`, userMessage)
      .then((response) => {
        setMessages((prevMessages) => [...prevMessages, response.data]);
        setInputValue("");

        // Fetch updated messages with bot's response
        axios.get<Message[]>(`http://localhost:8000/messages/?session_id=${session_id}`)
          .then((response) => setMessages(response.data))
          .catch((error) => console.error("Error fetching messages:", error));
      })
      .catch((error) => console.error("Error sending message:", error));
  };


  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };


  const suggestionHandel = (suggestion: string) => {
    setInputValue(suggestion)
  }


  return (
    <div className={styles.container}>
      <div className={styles.chatContainer}>
        <div className={styles.chatHeader}>
          <Avatar
            alt="Ava"
            src="https://i.pravatar.cc/300"
            sx={{ width: 50, height: 50 }}
          />
          <h3>Hey👋, I'm Ava</h3>
          <p>Ask me anything or pick a place to start</p>
        </div>

        <div className={styles.chatBody}>
          {messages.map((message) => (
            <div key={message.id} className={message.user_id === 1 ? styles.chatReply : styles.chatMessage}>
              {message.user_id !== 1 && <Avatar
                alt={message.user_id === 1 ? "User" : "Ava"}
                src={message.user_id === 1 ? "https://i.pravatar.cc/50" : "https://i.pravatar.cc/300"}
                sx={{ width: message.user_id === 1 ? 36 : 40, height: message.user_id === 1 ? 36 : 40 }}
              />}
              <div className={styles.messageBubble}>
                <span>{message.text}</span>
              </div>
            </div>
          ))}
        </div>


        <div className={styles.chatActions}>
          {messages.length > 0 && messages[messages.length - 1].suggestions?.map((suggestion, index) =>
            <Button className={styles.chatAction} onClick={() => suggestionHandel(suggestion)} key={index} variant="outlined">{suggestion}</Button>)
          }
        </div>

        {/* Bottom input section */}
        <div className={styles.chatInputSection}>
          <div>
            <Avatar
              alt="User"
              src="https://i.pravatar.cc/50"
              sx={{ width: 36, height: 36, border: '2px solid #D0E0F0', backgroundColor: '#D0E0F0' }}
            />
            <TextField
              className={styles.chatInput}
              placeholder="Your question"
              variant="standard"
              value={inputValue}
              onChange={handleInputChange}
            />
          </div>
          <div>
            <TextField
              select
              className={styles.chatContextSelect}
              defaultValue="Onboarding"
              variant="standard"
            >
              <MenuItem value="Onboarding">Onboarding</MenuItem>
              <MenuItem value="Support">Support</MenuItem>
              <MenuItem value="Sales">Sales</MenuItem>
            </TextField>
            <span>
              <IconButton>
                <CiSettings />
              </IconButton>
              <IconButton onClick={handleSendMessage}>
                <AiOutlineSend />
              </IconButton>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;
