// Friendship Game - Main JavaScript Logic
class FriendshipGame {
    constructor() {
        this.players = [];
        this.currentQuestions = [];
        this.currentRound = 0;
        this.currentPlayerIndex = 0;
        this.score = 0;
        this.gameResults = [];
        this.totalRounds = 10;

        this.initializeGame();
    }

    initializeGame() {
        // Initialize language system
        window.translations.initializeLanguage();

        // Get DOM elements
        this.screens = {
            welcome: document.getElementById('welcome-screen'),
            setup: document.getElementById('setup-screen'),
            game: document.getElementById('game-screen'),
            results: document.getElementById('results-screen')
        };

        this.elements = {
            playerCount: document.getElementById('player-count'),
            playersContainer: document.getElementById('players-container'),
            currentRound: document.getElementById('current-round'),
            currentScore: document.getElementById('current-score'),
            currentPlayerName: document.getElementById('current-player-name'),
            currentQuestion: document.getElementById('current-question'),
            playersGrid: document.getElementById('players-grid'),
            finalScore: document.getElementById('final-score'),
            resultsSummary: document.getElementById('results-summary')
        };

        this.bindEvents();
        this.showScreen('welcome');
    }

    bindEvents() {
        // Welcome screen
        document.getElementById('start-game').addEventListener('click', () => {
            this.showScreen('setup');
        });

        // Setup screen
        this.elements.playerCount.addEventListener('change', () => {
            this.generatePlayerInputs();
        });

        document.getElementById('back-to-welcome').addEventListener('click', () => {
            this.showScreen('welcome');
        });

        document.getElementById('start-playing').addEventListener('click', () => {
            this.startGame();
        });

        // Game screen
        document.getElementById('skip-question').addEventListener('click', () => {
            this.skipQuestion();
        });

        document.getElementById('end-game').addEventListener('click', () => {
            this.endGame();
        });

        // Results screen
        document.getElementById('play-again').addEventListener('click', () => {
            this.playAgain();
        });

        document.getElementById('new-game').addEventListener('click', () => {
            this.newGame();
        });

        // Initialize player inputs
        this.generatePlayerInputs();
    }

    showScreen(screenName) {
        // Hide all screens
        Object.values(this.screens).forEach(screen => {
            screen.classList.remove('active');
        });

        // Show target screen
        this.screens[screenName].classList.add('active');

        // Update translations when screen changes
        window.translations.updateTranslations();
    }

    generatePlayerInputs() {
        const count = parseInt(this.elements.playerCount.value);
        const container = this.elements.playersContainer;

        container.innerHTML = '';

        for (let i = 1; i <= count; i++) {
            const playerInput = document.createElement('div');
            playerInput.className = 'player-input';

            const input = document.createElement('input');
            input.type = 'text';
            input.id = `player-${i}`;
            input.placeholder = window.translations.getText('player_placeholder') + ` ${i}`;
            input.required = true;

            playerInput.appendChild(input);
            container.appendChild(playerInput);
        }
    }

    startGame() {
        // Collect player names
        const playerInputs = document.querySelectorAll('.player-input input');
        this.players = [];

        let allNamesEntered = true;
        playerInputs.forEach((input, index) => {
            const name = input.value.trim();
            if (name) {
                this.players.push({
                    id: index,
                    name: name,
                    correctAnswers: 0
                });
            } else {
                allNamesEntered = false;
            }
        });

        if (!allNamesEntered) {
            alert(window.translations.getText('enter_all_names'));
            return;
        }

        // Initialize game state
        this.currentRound = 0;
        this.currentPlayerIndex = 0;
        this.score = 0;
        this.gameResults = [];

        // Get random questions for the game
        const currentLang = window.translations.getCurrentLanguage();
        this.currentQuestions = window.questionsDB.getRandomQuestions(currentLang, this.totalRounds);

        // Generate players grid
        this.generatePlayersGrid();

        // Start first round
        this.nextRound();

        // Show game screen
        this.showScreen('game');
    }

    generatePlayersGrid() {
        const grid = this.elements.playersGrid;
        grid.innerHTML = '';

        this.players.forEach(player => {
            const button = document.createElement('button');
            button.className = 'player-option';
            button.textContent = player.name;
            button.dataset.playerId = player.id;

            button.addEventListener('click', () => {
                this.selectPlayer(player.id, button);
            });

            grid.appendChild(button);
        });
    }

    nextRound() {
        if (this.currentRound >= this.totalRounds) {
            this.showResults();
            return;
        }

        // Update round info
        this.elements.currentRound.textContent = this.currentRound + 1;
        this.elements.currentScore.textContent = this.score;

        // Select random player for this round
        this.currentPlayerIndex = Math.floor(Math.random() * this.players.length);
        const currentPlayer = this.players[this.currentPlayerIndex];
        this.elements.currentPlayerName.textContent = currentPlayer.name;

        // Display current question
        this.elements.currentQuestion.textContent = this.currentQuestions[this.currentRound];

        // Reset player options
        document.querySelectorAll('.player-option').forEach(option => {
            option.classList.remove('selected');
            option.disabled = false;
        });

        // Add animation to question
        this.elements.currentQuestion.classList.add('success-animation');
        setTimeout(() => {
            this.elements.currentQuestion.classList.remove('success-animation');
        }, 600);
    }

    selectPlayer(playerId, buttonElement) {
        // Remove previous selections
        document.querySelectorAll('.player-option').forEach(option => {
            option.classList.remove('selected');
        });

        // Select current option
        buttonElement.classList.add('selected');

        // Check if correct answer (the current player)
        const isCorrect = playerId === this.currentPlayerIndex;

        // Store result
        this.gameResults.push({
            round: this.currentRound + 1,
            question: this.currentQuestions[this.currentRound],
            selectedPlayer: this.players[playerId].name,
            correctPlayer: this.players[this.currentPlayerIndex].name,
            isCorrect: isCorrect
        });

        // Update score
        if (isCorrect) {
            this.score++;
            this.players[this.currentPlayerIndex].correctAnswers++;
            this.showFeedback(window.translations.getText('correct_answer'), 'success');
        } else {
            this.showFeedback(window.translations.getText('wrong_answer'), 'error');
        }

        // Disable all options
        document.querySelectorAll('.player-option').forEach(option => {
            option.disabled = true;
        });

        // Move to next round after delay
        setTimeout(() => {
            this.currentRound++;
            this.nextRound();
        }, 2000);
    }

    skipQuestion() {
        // Store skipped result
        this.gameResults.push({
            round: this.currentRound + 1,
            question: this.currentQuestions[this.currentRound],
            selectedPlayer: window.translations.getText('skipped'),
            correctPlayer: this.players[this.currentPlayerIndex].name,
            isCorrect: false
        });

        this.currentRound++;
        this.nextRound();
    }

    showFeedback(message, type) {
        // Create feedback element
        const feedback = document.createElement('div');
        feedback.className = `feedback ${type}`;
        feedback.textContent = message;
        feedback.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: ${type === 'success' ? '#28a745' : '#dc3545'};
            color: white;
            padding: 20px 40px;
            border-radius: 10px;
            font-size: 1.2rem;
            font-weight: 600;
            z-index: 10000;
            animation: fadeInOut 2s ease;
        `;

        // Add CSS animation
        if (!document.getElementById('feedback-styles')) {
            const style = document.createElement('style');
            style.id = 'feedback-styles';
            style.textContent = `
                @keyframes fadeInOut {
                    0% { opacity: 0; transform: translate(-50%, -50%) scale(0.8); }
                    20% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
                    80% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
                    100% { opacity: 0; transform: translate(-50%, -50%) scale(0.8); }
                }
            `;
            document.head.appendChild(style);
        }

        document.body.appendChild(feedback);

        // Remove feedback after animation
        setTimeout(() => {
            if (feedback.parentNode) {
                feedback.parentNode.removeChild(feedback);
            }
        }, 2000);
    }

    endGame() {
        if (confirm(window.translations.getText('confirm_end_game'))) {
            this.showResults();
        }
    }

    showResults() {
        // Update final score
        this.elements.finalScore.textContent = `${this.score} / ${this.totalRounds}`;

        // Generate results summary
        this.generateResultsSummary();

        // Show results screen
        this.showScreen('results');

        // Show completion message
        setTimeout(() => {
            alert(window.translations.getText('game_completed'));
        }, 500);
    }

    generateResultsSummary() {
        const summary = this.elements.resultsSummary;
        summary.innerHTML = '';

        // Score percentage
        const percentage = Math.round((this.score / this.totalRounds) * 100);

        // Performance message
        let performanceMessage;
        if (percentage >= 80) {
            performanceMessage = window.translations.getText('excellent');
        } else if (percentage >= 60) {
            performanceMessage = window.translations.getText('good');
        } else if (percentage >= 40) {
            performanceMessage = window.translations.getText('okay');
        } else {
            performanceMessage = window.translations.getText('needs_work');
        }

        // Create summary content
        const summaryContent = `
            <div class="performance-message">
                <p>${window.translations.getText('you_got')} ${this.score} ${window.translations.getText('out_of')} ${this.totalRounds} ${window.translations.getText('questions_right')}</p>
                <p><strong>${performanceMessage}</strong></p>
            </div>
            <div class="detailed-results">
                <h4>${window.translations.getText('detailed_results')}</h4>
                ${this.gameResults.map((result, index) => `
                    <div class="result-item ${result.isCorrect ? 'correct' : 'incorrect'}">
                        <strong>${window.translations.getText('round_label')} ${result.round}:</strong> ${result.question}<br>
                        <small>${window.translations.getText('selected_label')}: ${result.selectedPlayer} | ${window.translations.getText('correct_label')}: ${result.correctPlayer}</small>
                    </div>
                `).join('')}
            </div>
        `;

        summary.innerHTML = summaryContent;

        // Add styles for detailed results
        if (!document.getElementById('results-styles')) {
            const style = document.createElement('style');
            style.id = 'results-styles';
            style.textContent = `
                .performance-message {
                    text-align: center;
                    margin-bottom: 20px;
                    font-size: 1.1rem;
                }
                .detailed-results h4 {
                    margin-bottom: 15px;
                    color: #667eea;
                }
                .result-item {
                    padding: 10px;
                    margin-bottom: 10px;
                    border-radius: 8px;
                    border-left: 4px solid;
                }
                .result-item.correct {
                    background: rgba(40, 167, 69, 0.1);
                    border-left-color: #28a745;
                }
                .result-item.incorrect {
                    background: rgba(220, 53, 69, 0.1);
                    border-left-color: #dc3545;
                }
                [dir="rtl"] .result-item {
                    border-left: none;
                    border-right: 4px solid;
                }
                [dir="rtl"] .result-item.correct {
                    border-right-color: #28a745;
                }
                [dir="rtl"] .result-item.incorrect {
                    border-right-color: #dc3545;
                }
            `;
            document.head.appendChild(style);
        }
    }

    playAgain() {
        // Reset game with same players
        this.currentRound = 0;
        this.currentPlayerIndex = 0;
        this.score = 0;
        this.gameResults = [];

        // Get new random questions
        const currentLang = window.translations.getCurrentLanguage();
        this.currentQuestions = window.questionsDB.getRandomQuestions(currentLang, this.totalRounds);

        // Start first round
        this.nextRound();

        // Show game screen
        this.showScreen('game');
    }

    newGame() {
        // Reset everything and go back to setup
        this.players = [];
        this.currentQuestions = [];
        this.currentRound = 0;
        this.currentPlayerIndex = 0;
        this.score = 0;
        this.gameResults = [];

        // Clear player inputs
        document.querySelectorAll('.player-input input').forEach(input => {
            input.value = '';
        });

        // Show setup screen
        this.showScreen('setup');
    }
}

// Initialize the game when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new FriendshipGame();
});

// Handle language changes
document.addEventListener('DOMContentLoaded', () => {
    // Update placeholder text when language changes
    const originalSetLanguage = window.translations.setLanguage;
    window.translations.setLanguage = function (lang) {
        originalSetLanguage(lang);

        // Update player input placeholders
        document.querySelectorAll('.player-input input').forEach((input, index) => {
            input.placeholder = window.translations.getText('player_placeholder') + ` ${index + 1}`;
        });
    };
});
