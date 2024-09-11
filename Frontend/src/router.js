import { createBrowserRouter } from 'react-router-dom';
import App from "./App"
import Chatbot from './screens/Chatbot.tsx';

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "chatbot",
    element: <Chatbot />,
  },
]);

export default router;
