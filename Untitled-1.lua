<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gazal's Prediction Game</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Gazal's First Year Predictions</h1>
            <p class="subtitle">Make your predictions about Gazal's milestones!</p>
        </header>

        <div class="game-container">
            <div class="question-container">
                <h2 id="question-number">Question <span id="current-day">1</span>/155</h2>
                <div id="question-text" class="question-text">What will Gazal's first word be?</div>
            </div>

            <div class="prediction-form">
                <input type="text" id="prediction-input" placeholder="Enter your prediction...">
                <button id="submit-prediction">Submit Prediction</button>
            </div>

            <div class="prediction-stats">
                <h3>Prediction Stats</h3>
                <div id="prediction-count" class="prediction-count">Total Predictions: 0</div>
                <div id="prediction-list" class="prediction-list">
                    <!-- Predictions will be listed here -->
                </div>
            </div>

            <div class="navigation">
                <button id="prev-question" disabled>Previous Question</button>
                <button id="next-question">Next Question</button>
            </div>
        </div>

        <footer>
            <p>Created with love for Gazal's first birthday! 💕</p>
        </footer>
    </div>

    <script src="questions.js"></script>
    <script src="app.js"></script>
</body>
</html>
// Main application logic for Gazal's Prediction Game

// Initialize game state
let currentQuestionIndex = 0;
let predictions = [];

// DOM elements
const questionNumberElement = document.getElementById('current-day');
const questionTextElement = document.getElementById('question-text');
const predictionInput = document.getElementById('prediction-input');
const submitButton = document.getElementById('submit-prediction');
const predictionCountElement = document.getElementById('prediction-count');
const predictionListElement = document.getElementById('prediction-list');
const prevButton = document.getElementById('prev-question');
const nextButton = document.getElementById('next-question');

// Initialize local storage
function initializeLocalStorage() {
if (!localStorage.getItem('gazalPredictions')) {
localStorage.setItem('gazalPredictions', JSON.stringify(Array(questions.length).fill([])));
}
predictions = JSON.parse(localStorage.getItem('gazalPredictions'));
}

// Display current question
function displayQuestion() {
questionNumberElement.textContent = currentQuestionIndex + 1;
questionTextElement.textContent = questions[currentQuestionIndex];

// Update navigation buttons
prevButton.disabled = currentQuestionIndex === 0;
nextButton.disabled = currentQuestionIndex === questions.length - 1;

// Display predictions for current question
displayPredictions();
}

// Display predictions for current question
function displayPredictions() {
const currentPredictions = predictions[currentQuestionIndex];
predictionListElement.innerHTML = '';

// Count predictions by value
const predictionCounts = {};
currentPredictions.forEach(prediction => {
predictionCounts[prediction] = (predictionCounts[prediction] || 0) + 1;
});

// Create sorted array of predictions
const sortedPredictions = Object.entries(predictionCounts)
.sort((a, b) => b[1] - a[1])
.map(([text, count]) => ({ text, count }));

// Display predictions
sortedPredictions.forEach(prediction => {
const predictionItem = document.createElement('div');
predictionItem.className = 'prediction-item';
predictionItem.innerHTML = `
<span class="prediction-text">${prediction.text}</span>
<span class="prediction-count-badge">${prediction.count}</span>
`;
predictionListElement.appendChild(predictionItem);
});

// Update total prediction count
predictionCountElement.textContent = `Total Predictions: ${currentPredictions.length}`;
}

// Add a new prediction
function addPrediction() {
const predictionText = predictionInput.value.trim();

if (predictionText) {
// Add prediction to array
predictions[currentQuestionIndex].push(predictionText);

// Save to local storage
localStorage.setItem('gazalPredictions', JSON.stringify(predictions));

// Clear input
predictionInput.value = '';

// Update display
displayPredictions();

// Add animation class to the newest prediction
setTimeout(() => {
const newestPrediction = predictionListElement.firstChild;
if (newestPrediction) {
newestPrediction.classList.add('new-prediction');
}
}, 10);
}
}

// Navigate to previous question
function goToPreviousQuestion() {
if (currentQuestionIndex > 0) {
currentQuestionIndex--;
displayQuestion();
}
}

// Navigate to next question
function goToNextQuestion() {
if (currentQuestionIndex < questions.length - 1) { currentQuestionIndex++; displayQuestion(); } } // Event listeners
    submitButton.addEventListener('click', addPrediction); predictionInput.addEventListener('keypress', (e)=> {
    if (e.key === 'Enter') {
    addPrediction();
    }
    });
    prevButton.addEventListener('click', goToPreviousQuestion);
    nextButton.addEventListener('click', goToNextQuestion);

    // Initialize game
    document.addEventListener('DOMContentLoaded', () => {
    initializeLocalStorage();
    displayQuestion();

    // Set up automatic question of the day
    const today = new Date();
    const startDate = new Date(today.getFullYear(), 0, 1); // January 1st of current year
    const dayOfYear = Math.floor((today - startDate) / (24 * 60 * 60 * 1000));

    // If we're within the first 155 days of the year, show that day's question
    if (dayOfYear < questions.length) { currentQuestionIndex=dayOfYear; displayQuestion(); } });
    / Questions database for Gazal's Prediction Game
const questions = [
    // First words and language development
    "What will Gazal's first word be?",
    "At what age will Gazal say her first word?",
    "How many words will Gazal know by her second birthday?",
    "Will Gazal be an early or late talker?",
    "What will be Gazal's favorite word to repeat?",
    "Will Gazal learn to say 'mama' or 'dada' first?",
    "When will Gazal first say her own name?",
    "Will Gazal be able to follow simple instructions by 18 months?",
    "When will Gazal start putting two words together?",
    "Will Gazal be multilingual? If so, which languages?",
    
    // Physical development
    "At what age will Gazal take her first steps?",
    "When will Gazal first stand without support?",
    "Will Gazal crawl before walking or skip crawling?",
    "At what age will Gazal be able to climb stairs?",
    "When will Gazal learn to jump with both feet?",
    "At what age will Gazal be able to kick a ball?",
    "When will Gazal first be able to feed herself with a spoon?",
    "At what age will Gazal be able to drink from a cup without spilling?",
    "When will Gazal start scribbling with crayons?",
    "At what age will Gazal be able to build a tower of blocks?",
    
    // Social and emotional development
    "Who will be Gazal's favorite person at age 2?",
    "What will be Gazal's first fear?",
    "Will Gazal be shy or outgoing with strangers?",
    "What will make Gazal laugh the hardest?",
    "How will Gazal show affection?",
    "Will Gazal have a favorite stuffed animal or comfort object?",
    "How will Gazal react to meeting other babies?",
    "Will Gazal be more independent or clingy?",
    "What will be Gazal's favorite way to be comforted when upset?",
    "How will Gazal express frustration?",
    
    // Sleep patterns
    "Will Gazal sleep through the night by 12 months?",
    "What will be Gazal's bedtime routine?",
    "Will Gazal be an early riser or sleep in?",
    "How many naps will Gazal take at 18 months?",
    "Will Gazal have a favorite sleeping position?",
    "Will Gazal use a pacifier to sleep?",
    "Will Gazal prefer to co-sleep or sleep independently?",
    "What will help Gazal fall asleep fastest?",
    "Will Gazal have a favorite lullaby?",
    "At what age will Gazal transition from a crib to a bed?",
    
    // Food and eating habits
    "What will be Gazal's favorite food at age 2?",
    "What food will Gazal strongly dislike?",
    "Will Gazal be a picky or adventurous eater?",
    "What will be Gazal's favorite fruit?",
    "What will be Gazal's favorite vegetable (if any)?",
    "Will Gazal prefer sweet or savory foods?",
    "At what age will Gazal feed herself independently?",
    "Will Gazal have any food allergies?",
    "What will be Gazal's favorite snack?",
    "Will Gazal enjoy trying new foods?",
    
    // Play and interests
    "What will be Gazal's favorite toy at 18 months?",
    "Will Gazal prefer indoor or outdoor play?",
    "What type of play will Gazal enjoy most (building, pretend, active)?",
    "Will Gazal show interest in music? How?",
    "What will be Gazal's favorite nursery rhyme or song?",
    "Will Gazal enjoy books? What kind?",
    "What will be Gazal's favorite book?",
    "Will Gazal enjoy water play?",
    "What will be Gazal's favorite playground activity?",
    "Will Gazal prefer playing alone or with others?",
    
    // Appearance and physical traits
    "What color will Gazal's eyes be at age 2?",
    "How long will Gazal's hair be at age 2?",
    "What hair color will Gazal have at age 2?",
    "Will Gazal's hair be straight, wavy, or curly?",
    "How tall will Gazal be at her second birthday?",
    "How much will Gazal weigh at her second birthday?",
    "Will Gazal look more like mom or dad?",
    "Will Gazal be right or left-handed?",
    "Will Gazal have dimples?",
    "How many teeth will Gazal have by age 2?",
    
    // Milestones and firsts
    "When will Gazal get her first tooth?",
    "What will be Gazal's first solid food?",
    "Where will Gazal take her first steps?",
    "What will be Gazal's reaction to her first birthday cake?",
    "What will be Gazal's first sign (if using baby sign language)?",
    "When will Gazal first recognize her name?",
    "What will be Gazal's first trip or vacation?",
    "When will Gazal first show recognition in a mirror?",
    "What will be Gazal's first major illness?",
    "When will Gazal first show empathy?",
    
    // Personality and temperament
    "Will Gazal be more serious or silly?",
    "Will Gazal be patient or impatient?",
    "Will Gazal be cautious or adventurous?",
    "Will Gazal be more logical or creative?",
    "Will Gazal be a leader or follower with other children?",
    "Will Gazal be more active or calm?",
    "Will Gazal be persistent or easily discouraged?",
    "Will Gazal be more focused or easily distracted?",
    "Will Gazal be adaptable to change or prefer routine?",
    "Will Gazal be more sensitive or resilient?",
    
    // Family relationships
    "Who will Gazal call for first when upset?",
    "Will Gazal have a stronger bond with mom or dad?",
    "How will Gazal interact with extended family members?",
    "Will Gazal be jealous of attention given to others?",
    "How will Gazal show love to family members?",
    "Will Gazal enjoy video calls with distant family?",
    "Will Gazal recognize family members in photos?",
    "How will Gazal react when parents leave the room?",
    "Will Gazal have a special relationship with a grandparent?",
    "How will Gazal greet family members after absences?",
    
    // Communication style
    "Will Gazal be more verbal or use more gestures?",
    "Will Gazal be loud or quiet?",
    "Will Gazal babble a lot before talking?",
    "Will Gazal use baby sign language?",
    "How many words will Gazal know at 18 months?",
    "Will Gazal be able to follow two-step instructions by age 2?",
    "Will Gazal be able to identify body parts when asked?",
    "Will Gazal speak clearly or be difficult to understand?",
    "Will Gazal enjoy singing?",
    "Will Gazal talk early or late compared to peers?",
    
    // Cognitive development
    "Will Gazal show strong memory skills?",
    "Will Gazal be good at puzzles?",
    "Will Gazal show interest in numbers or counting?",
    "Will Gazal recognize colors by age 2?",
    "Will Gazal be able to sort objects by shape or color?",
    "Will Gazal show interest in how things work?",
    "Will Gazal have a long or short attention span?",
    "Will Gazal be observant of details?",
    "Will Gazal show strong problem-solving skills?",
    "Will Gazal be interested in cause and effect?",
    
    // Behavior and discipline
    "What will be Gazal's first act of defiance?",
    "Will Gazal have tantrums? How often?",
    "What will calm Gazal down when upset?",
    "Will Gazal respond better to firm or gentle guidance?",
    "Will Gazal test boundaries frequently?",
    "Will Gazal be easily redirected?",
    "What behavior strategy will work best with Gazal?",
    "Will Gazal be stubborn or compliant?",
    "Will Gazal share willingly with others?",
    "How will Gazal respond to the word 'no'?",
    
    // Health and wellness
    "How many colds will Gazal have in her first two years?",
    "Will Gazal have any allergies? If so, to what?",
    "Will Gazal be a good patient at doctor visits?",
    "Will Gazal need any medical interventions?",
    "How will Gazal handle vaccinations?",
    "Will Gazal have sensitive skin?",
    "Will Gazal have any birthmarks?",
    "Will Gazal have any food sensitivities?",
    "Will Gazal be prone to diaper rash?",
    "Will Gazal be generally healthy or frequently ill?",
    
    // Future predictions
    "What career might Gazal be suited for based on early interests?",
    "What sport or activity might Gazal excel at?",
    "Will Gazal show early signs of artistic talent?",
    "Will Gazal show early signs of musical ability?",
    "Will Gazal show early signs of mathematical thinking?",
    "Will Gazal be more interested in people or things?",
    "What will be Gazal's favorite color at age 2?",
    "What will be Gazal's favorite animal at age 2?",
    "Will Gazal be more interested in nature or technology?",
    "What special talent might Gazal develop?"
];

// Ensure we have exactly 155 questions
if (questions.length < 155) {
    // Add generic questions if we don't have enough
    for (let i = questions.length; i < 155; i++) {
        questions.push(`What will be surprising about Gazal's development on day ${i+1}?`);
    }
} else if (questions.length > 155) {
    // Trim if we have too many
    questions.length = 155;}
    /* Main Styles for Gazal's Prediction Game */
:root {
    --primary-color: #ff9ed8;
    --secondary-color: #b5e8f7;
    --accent-color: #ffde59;
    --text-color: #333;
    --light-color: #ffffff;
    --border-radius: 12px;
    --box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Comic Sans MS', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    background-color: #f9f9f9;
    background-image: url('data:image/svg+xml;utf8,<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="20" r="5" fill="%23ffcce6" opacity="0.5"/><circle cx="60" cy="40" r="7" fill="%23b5e8f7" opacity="0.5"/><circle cx="80" cy="70" r="6" fill="%23ffde59" opacity="0.5"/></svg>');
    color: var(--text-color);
    line-height: 1.6;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

header {
    text-align: center;
    margin-bottom: 30px;
    padding: 20px;
    background-color: var(--primary-color);
    border-radius: var(--border-radius);
    box-shadow: var(--box-shadow);
    color: var(--light-color);
}

h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.subtitle {
    font-size: 1.2rem;
    font-weight: bold;
}

.game-container {
    background-color: var(--light-color);
    border-radius: var(--border-radius);
    box-shadow: var(--box-shadow);
    padding: 30px;
    margin-bottom: 30px;
}

.question-container {
    margin-bottom: 25px;
    text-align: center;
}

#question-number {
    color: var(--primary-color);
    margin-bottom: 15px;
    font-size: 1.5rem;
}

.question-text {
    font-size: 1.8rem;
    font-weight: bold;
    padding: 15px;
    background-color: var(--secondary-color);
    border-radius: var(--border-radius);
    margin-bottom: 20px;
}

.prediction-form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-bottom: 30px;
}

#prediction-input {
    padding: 12px 15px;
    border: 2px solid var(--secondary-color);
    border-radius: var(--border-radius);
    font-size: 1.1rem;
    outline: none;
    transition: border-color 0.3s;
}

#prediction-input:focus {
    border-color: var(--primary-color);
}

#submit-prediction {
    padding: 12px 20px;
    background-color: var(--accent-color);
    color: var(--text-color);
    border: none;
    border-radius: var(--border-radius);
    font-size: 1.1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.2s;
}

#submit-prediction:hover {
    background-color: #ffd633;
    transform: translateY(-2px);
}

#submit-prediction:active {
    transform: translateY(0);
}

.prediction-stats {
    background-color: #f8f8f8;
    border-radius: var(--border-radius);
    padding: 20px;
    margin-bottom: 25px;
}

.prediction-stats h3 {
    color: var(--primary-color);
    margin-bottom: 15px;
    text-align: center;
}

.prediction-count {
    font-weight: bold;
    margin-bottom: 15px;
    text-align: center;
}

.prediction-list {
    max-height: 200px;
    overflow-y: auto;
    border: 1px solid #eee;
    border-radius: 8px;
    padding: 10px;
    background-color: white;
}

.prediction-item {
    padding: 8px 12px;
    margin-bottom: 8px;
    background-color: #f0f0f0;
    border-radius: 6px;
    display: flex;
    justify-content: space-between;
}

.prediction-item:last-child {
    margin-bottom: 0;
}

.prediction-text {
    font-weight: bold;
}

.prediction-count-badge {
    background-color: var(--primary-color);
    color: white;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 0.9rem;
}

.navigation {
    display: flex;
    justify-content: space-between;
    gap: 15px;
}

.navigation button {
    flex: 1;
    padding: 12px;
    background-color: var(--secondary-color);
    color: var(--text-color);
    border: none;
    border-radius: var(--border-radius);
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s;
}

.navigation button:hover:not(:disabled) {
    background-color: #a0dff3;
}

.navigation button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

footer {
    text-align: center;
    padding: 15px;
    color: var(--text-color);
    font-size: 0.9rem;
}

/* Responsive styles */
@media (max-width: 768px) {
    .container {
        padding: 15px;
    }
    
    h1 {
        font-size: 2rem;
    }
    
    .question-text {
        font-size: 1.5rem;
    }
    
    .prediction-form {
        flex-direction: column;
    }
    
    .navigation {
        flex-direction: column;
    }
}

/* Animation for new predictions */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }}

.new-prediction {
    animation: fadeIn 0.5s ease-out;}