// Translation system for the Friendship Game
const translations = {
    en: {
        // General
        title: "Friendship Game",

        // Welcome Screen
        welcome_title: "🎉 Friendship Game",
        welcome_subtitle: "Test how well you know your friends!",
        start_game: "Start Game",

        // Setup Screen
        setup_title: "Game Setup",
        num_players: "Number of Players:",
        player_placeholder: "Enter player name",
        back: "Back",
        start_playing: "Start Playing",

        // Game Screen
        round: "Round",
        score: "Score:",
        current_player: "Current Player:",
        skip: "Skip",
        end_game: "End Game",

        // Results Screen
        game_over: "🎊 Game Over!",
        final_score: "Final Score:",
        play_again: "Play Again",
        new_game: "New Game",

        // Messages
        enter_all_names: "Please enter all player names!",
        correct_answer: "Correct! 🎉",
        wrong_answer: "Wrong answer! 😅",
        game_completed: "Game completed successfully!",
        confirm_end_game: "Are you sure you want to end the game?",

        // Results summary
        you_got: "You got",
        out_of: "out of",
        questions_right: "questions right!",
        detailed_results: "Detailed Results:",
        round_label: "Round",
        selected_label: "Selected",
        correct_label: "Correct",
        skipped: "Skipped",
        excellent: "Excellent! You know your friends very well! 🌟",
        good: "Good job! You have a solid friendship! 👍",
        okay: "Not bad! There's room to learn more about each other! 😊",
        needs_work: "Time to spend more quality time together! 💪"
    },

    ar: {
        // General
        title: "لعبة الصداقة",

        // Welcome Screen
        welcome_title: "🎉 لعبة الصداقة",
        welcome_subtitle: "اختبر مدى معرفتك بأصدقائك!",
        start_game: "ابدأ اللعبة",

        // Setup Screen
        setup_title: "إعداد اللعبة",
        num_players: "عدد اللاعبين:",
        player_placeholder: "أدخل اسم اللاعب",
        back: "رجوع",
        start_playing: "ابدأ اللعب",

        // Game Screen
        round: "الجولة",
        score: "النقاط:",
        current_player: "اللاعب الحالي:",
        skip: "تخطي",
        end_game: "إنهاء اللعبة",

        // Results Screen
        game_over: "🎊 انتهت اللعبة!",
        final_score: "النتيجة النهائية:",
        play_again: "العب مرة أخرى",
        new_game: "لعبة جديدة",

        // Messages
        enter_all_names: "يرجى إدخال أسماء جميع اللاعبين!",
        correct_answer: "إجابة صحيحة! 🎉",
        wrong_answer: "إجابة خاطئة! 😅",
        game_completed: "تم إكمال اللعبة بنجاح!",
        confirm_end_game: "هل أنت متأكد أنك تريد إنهاء اللعبة؟",

        // Results summary
        you_got: "حصلت على",
        out_of: "من أصل",
        questions_right: "أسئلة صحيحة!",
        detailed_results: "النتائج التفصيلية:",
        round_label: "الجولة",
        selected_label: "المختار",
        correct_label: "الصحيح",
        skipped: "تم التخطي",
        excellent: "ممتاز! أنت تعرف أصدقاءك جيداً جداً! 🌟",
        good: "عمل جيد! لديك صداقة قوية! 👍",
        okay: "ليس سيئاً! هناك مجال لتتعلم المزيد عن بعضكم البعض! 😊",
        needs_work: "حان الوقت لقضاء المزيد من الوقت الممتع معاً! 💪"
    }
};

// Current language
let currentLanguage = 'en';

// Language management functions
function setLanguage(lang) {
    currentLanguage = lang;

    // Update HTML attributes
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';

    // Update all translatable elements
    updateTranslations();

    // Update language buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });

    // Save language preference
    localStorage.setItem('friendshipGameLanguage', lang);
}

function updateTranslations() {
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.dataset.translate;
        if (translations[currentLanguage] && translations[currentLanguage][key]) {
            if (element.tagName === 'INPUT' && element.type === 'text') {
                element.placeholder = translations[currentLanguage][key];
            } else {
                element.textContent = translations[currentLanguage][key];
            }
        }
    });
}

function getText(key) {
    return translations[currentLanguage] && translations[currentLanguage][key]
        ? translations[currentLanguage][key]
        : translations.en[key] || key;
}

// Initialize language system
function initializeLanguage() {
    // Load saved language preference
    const savedLanguage = localStorage.getItem('friendshipGameLanguage');
    if (savedLanguage && translations[savedLanguage]) {
        setLanguage(savedLanguage);
    }

    // Add event listeners to language buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            setLanguage(btn.dataset.lang);
        });
    });
}

// Export functions for use in other scripts
window.translations = {
    setLanguage,
    getText,
    initializeLanguage,
    updateTranslations,
    getCurrentLanguage: () => currentLanguage
};
