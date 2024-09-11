from typing import List


def generate_response(user_message: str) -> str:

    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing well. How can I assist you?",
        "what is your name": "I'm a chatbot created to help you!",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
        "thank you": "My pleasure!",
        "what time is it": "I'm not sure about the exact time. Please check your device.",
        "what is the weather like": "I don't have access to real-time weather information. Please check a weather website.",
        "what is your purpose": "I'm here to assist you with information and answer your questions.",
        "how can you help me": "I can provide information, answer questions, and chat with you about various topics.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "what is the capital of france": "The capital of France is Paris.",
        "who is the president of the united states": "As of now, the President of the United States is Joe Biden.",
        "how old are you": "I'm a computer program, so I don't have an age!",
        "what is your favorite color": "I don't have personal preferences, but I can help you find information about colors.",
        "can you help me with math": "Yes, I can help with basic math problems. What do you need help with?",
        "what is 2 plus 2": "2 plus 2 equals 4.",
        "who created you": "I was created by a team of developers to assist users like you.",
        "what is the meaning of life": "That's a deep question. Many people have different answers to this. Some say it's about finding happiness and purpose.",
        "what is love": "Love is a complex and deep emotion that involves affection, care, and connection.",
        "tell me a fact": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
        "how does a computer work": "A computer processes data using its hardware components and software. It performs calculations and tasks based on programmed instructions.",
        "what is artificial intelligence": "Artificial intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn.",
        "can you play music": "I can't play music, but I can help you find music online.",
        "what is your favorite book": "I don't have personal preferences, but I can suggest popular books if you'd like.",
        "what is the largest planet": "The largest planet in our solar system is Jupiter.",
        "what is the smallest country": "The smallest country in the world is Vatican City.",
        "who won the last world cup": "The winner of the last FIFA World Cup was France in 2018.",
        "what is the fastest animal": "The fastest animal on land is the cheetah, which can reach speeds of up to 60-70 miles per hour.",
        "how far is the moon": "The average distance from Earth to the Moon is about 238,855 miles (384,400 kilometers).",
        "what is the tallest mountain": "The tallest mountain in the world is Mount Everest.",
        "who wrote 'To Kill a Mockingbird'": "The book 'To Kill a Mockingbird' was written by Harper Lee.",
        "what is 10 divided by 2": "10 divided by 2 equals 5.",
        "what is the speed of light": "The speed of light is approximately 299,792 kilometers per second (about 186,282 miles per second).",
        "can you tell me a riddle": "Sure! What has keys but can't open locks? A piano.",
        "what is the longest river": "The longest river in the world is the Nile River.",
        "who is the founder of Microsoft": "The founder of Microsoft is Bill Gates.",
        "how many continents are there": "There are seven continents: Africa, Antarctica, Asia, Europe, North America, Australia (Oceania), and South America.",
        "what is the largest ocean": "The largest ocean in the world is the Pacific Ocean.",
        "who painted the Mona Lisa": "The Mona Lisa was painted by Leonardo da Vinci.",
        "what is the boiling point of water": "The boiling point of water is 100 degrees Celsius (212 degrees Fahrenheit) at sea level.",
        "can you speak other languages": "I can understand and respond in several languages. Which one would you like to use?",
        "what is the best programming language": "There isn't a single 'best' programming language. It depends on what you're trying to achieve. Popular ones include Python, JavaScript, and Java.",
        "what is a black hole": "A black hole is a region of space where the gravitational pull is so strong that not even light can escape from it.",
        "what is quantum computing": "Quantum computing is a type of computing that uses quantum bits (qubits) to perform calculations at speeds unattainable by classical computers.",
        "who is the author of '1984'": "The author of the novel '1984' is George Orwell.",
        "what is 5 times 6": "5 times 6 equals 30.",
        "what is the largest desert": "The largest desert in the world is the Antarctic Desert.",
        "who was the first person on the moon": "The first person to walk on the moon was Neil Armstrong.",
        "how do plants make food": "Plants make food through a process called photosynthesis, where they use sunlight to convert carbon dioxide and water into glucose and oxygen.",
        "what is the human brain made of": "The human brain is composed of neurons, glial cells, and various types of connective tissues and fluids.",
        "what is the distance to Mars": "The distance from Earth to Mars varies, but on average it is about 140 million miles (225 million kilometers).",
        "who is the author of 'Pride and Prejudice'": "The author of 'Pride and Prejudice' is Jane Austen.",
        "what is the currency of Japan": "The currency of Japan is the Japanese Yen (JPY).",
        "how does photosynthesis work": "Photosynthesis works by converting light energy into chemical energy, using sunlight to convert carbon dioxide and water into glucose and oxygen.",
        "what is the main ingredient in guacamole": "The main ingredient in guacamole is avocado.",
        "what is the largest animal on Earth": "The largest animal on Earth is the blue whale.",
        "who invented the telephone": "The telephone was invented by Alexander Graham Bell.",
        "what is the capital of Australia": "The capital of Australia is Canberra.",
        "how long does it take to travel around the world": "The time it takes to travel around the world varies depending on the mode of travel. For example, a non-stop flight can take around 24 hours, but traveling by other means can take significantly longer.",
        "what is the Great Wall of China": "The Great Wall of China is a series of fortifications built to protect Chinese states and empires from invasions.",
        "who wrote 'Moby Dick'": "The novel 'Moby Dick' was written by Herman Melville.",
        "what is the largest city in the world": "The largest city in the world by population is Tokyo, Japan.",
        "what is a solar eclipse": "A solar eclipse occurs when the Moon passes between the Earth and the Sun, blocking all or part of the Sun's light.",
        "how does the internet work": "The internet works by connecting millions of private, public, academic, business, and government networks to each other using a standardized protocol called TCP/IP.",
        "who is the author of 'The Catcher in the Rye'": "The author of 'The Catcher in the Rye' is J.D. Salinger.",
        "default": "I'm sorry, I didn't understand that."
    }

    user_message_lower = user_message.lower().strip()

    return responses.get(user_message_lower, responses["default"])


def generate_suggestions(text: str) -> List[str]:
    keywords_suggestions = {
        "hello": ["How can I assist you today?", "Do you need any information?", "Feel free to ask me anything!"],
        "bye": ["Do you need help with anything before you go?", "Take care!", "Have a wonderful day!"],
        "how are you": ["Would you like to chat more?", "How are you feeling today?", "What's on your mind?"],
        "what is the weather like": ["Would you like a weather app recommendation?", "Is it sunny where you are?", "Want to know tomorrow's forecast?"],
        "tell me a joke": ["Would you like to hear another joke?", "I can share fun facts too!", "Do you enjoy riddles?"],
        "tell me a fact": ["Want to hear more interesting facts?", "Do you enjoy learning new things?", "I can share more facts on different topics."],
        "can you help me with math": ["What math problem do you have?", "Need help with addition or subtraction?", "Let me know if you need any calculations."],
        "what is 2 plus 2": ["Would you like to try a harder problem?", "Math is fun, isn't it?", "I can help with more calculations!"],
        "what is love": ["Do you have any thoughts on love?", "It's a deep subject, isn't it?", "Love can be very different for everyone."],
        "default": ["Can you clarify?", "Tell me more about that.", "Why do you think so?", "What happened next?"]
    }

    user_message_lower = text.lower().strip()

    for keyword, suggestions in keywords_suggestions.items():
        if keyword in user_message_lower:
            return suggestions

    return keywords_suggestions["default"]
