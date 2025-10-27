import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class GazalPredictionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Gazal's Prediction Game")
        self.root.geometry("800x700")
        self.root.configure(bg="#f9f9f9")
        
        # Colors
        self.primary_color = "#ff9ed8"
        self.secondary_color = "#b5e8f7"
        self.accent_color = "#ffde59"
        self.text_color = "#333333"
        self.light_color = "#ffffff"
        
        # Initialize questions
        self.questions = self.load_questions()
        self.current_question_index = 0
        
        # Initialize predictions storage
        self.predictions_file = "gazal_predictions.json"
        self.predictions = self.load_predictions()
        
        # Create UI
        self.create_widgets()
        
        # Set today's question
        self.set_todays_question()
    
    def load_questions(self):
        """Load the 155 questions for the game"""
        questions = [
            # First words and language development
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
            
            # Physical development
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
            
            # Social and emotional development
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
            
            # Sleep patterns
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
            
            # Food and eating habits
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
            
            # Play and interests
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
            
            # Appearance and physical traits
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
            
            # Milestones and firsts
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
            
            # Personality and temperament
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
            
            # Family relationships
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
            
            # Communication style
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
            
            # Cognitive development
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
            
            # Behavior and discipline
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
            
            # Health and wellness
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
            
            # Future predictions
            "What career might Gazal be suited for based on early interests?",
            "What sport or activity might Gazal excel at?",
            "Will Gazal show early signs of artistic talent?",
            "Will Gazal show early signs of musical ability?",
            "Will Gazal show early signs of mathematical thinking?",
        ]
        
        # Ensure we have exactly 155 questions
        if len(questions) < 155:
            # Add generic questions if we don't have enough
            for i in range(len(questions), 155):
                questions.append(f"What will be surprising about Gazal's development on day {i+1}?")
        elif len(questions) > 155:
            # Trim if we have too many
            questions = questions[:155]
            
        return questions
    
    def load_predictions(self):
        """Load predictions from file or create new if doesn't exist"""
        if os.path.exists(self.predictions_file):
            try:
                with open(self.predictions_file, 'r') as f:
                    return json.load(f)
            except:
                return [[] for _ in range(len(self.questions))]
        else:
            return [[] for _ in range(len(self.questions))]
    
    def save_predictions(self):
        """Save predictions to file"""
        with open(self.predictions_file, 'w') as f:
            json.dump(self.predictions, f)
    
    def set_todays_question(self):
        """Set the question to today's date (day of year)"""
        today = datetime.now()
        day_of_year = today.timetuple().tm_yday - 1  # 0-indexed
        
        # If we're within the first 155 days of the year, show that day's question
        if day_of_year < len(self.questions):
            self.current_question_index = day_of_year
            self.update_question_display()
    
    def create_widgets(self):
        """Create all UI widgets"""
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f9f9f9")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = tk.Frame(main_frame, bg=self.primary_color, padx=20, pady=20)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(
            header_frame, 
            text="Gazal's First Year Predictions",
            font=("Comic Sans MS", 24, "bold"),
            bg=self.primary_color,
            fg=self.light_color
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame, 
            text="Make your predictions about Gazal's milestones!",
            font=("Comic Sans MS", 14),
            bg=self.primary_color,
            fg=self.light_color
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Game container
        game_frame = tk.Frame(main_frame, bg=self.light_color, padx=30, pady=30)
        game_frame.pack(fill=tk.BOTH, expand=True)
        
        # Question number
        self.question_number_label = tk.Label(
            game_frame,
            text="Question 1/155",
            font=("Comic Sans MS", 16),
            fg=self.primary_color,
            bg=self.light_color
        )
        self.question_number_label.pack(pady=(0, 15))
        
        # Question text
        question_text_frame = tk.Frame(game_frame, bg=self.secondary_color, padx=15, pady=15)
        question_text_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.question_text_label = tk.Label(
            question_text_frame,
            text=self.questions[0],
            font=("Comic Sans MS", 18, "bold"),
            wraplength=600,
            bg=self.secondary_color,
            fg=self.text_color
        )
        self.question_text_label.pack()
        
        # Prediction input
        prediction_frame = tk.Frame(game_frame, bg=self.light_color)
        prediction_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.prediction_entry = tk.Entry(
            prediction_frame,
            font=("Comic Sans MS", 14),
            width=40,
            bd=2,
            relief=tk.SOLID
        )
        self.prediction_entry.pack(pady=(0, 15), ipady=8)
        
        submit_button = tk.Button(
            prediction_frame,
            text="Submit Prediction",
            font=("Comic Sans MS", 14, "bold"),
            bg=self.accent_color,
            fg=self.text_color,
            padx=15,
            pady=8,
            bd=0,
            command=self.add_prediction
        )
        submit_button.pack()
        
        # Prediction stats
        stats_frame = tk.Frame(game_frame, bg="#f8f8f8", padx=20, pady=20)
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        stats_title = tk.Label(
            stats_frame,
            text="Prediction Stats",
            font=("Comic Sans MS", 16),
            fg=self.primary_color,
            bg="#f8f8f8"
        )
        stats_title.pack(pady=(0, 10))
        
        self.prediction_count_label = tk.Label(
            stats_frame,
            text="Total Predictions: 0",
            font=("Comic Sans MS", 12, "bold"),
            bg="#f8f8f8",
            fg=self.text_color
        )
        self.prediction_count_label.pack(pady=(0, 10))
        
        # Prediction list
        prediction_list_frame = tk.Frame(stats_frame, bg=self.light_color, bd=1, relief=tk.SOLID)
        prediction_list_frame.pack(fill=tk.BOTH, expand=True)
        
        self.prediction_listbox = tk.Listbox(
            prediction_list_frame,
            font=("Comic Sans MS", 12),
            height=6,
            bd=0,
            highlightthickness=0
        )
        self.prediction_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(prediction_list_frame, orient=tk.VERTICAL)
        scrollbar.config(command=self.prediction_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.prediction_listbox.config(yscrollcommand=scrollbar.set)
        
        # Navigation
        nav_frame = tk.Frame(game_frame, bg=self.light_color)
        nav_frame.pack(fill=tk.X)
        
        self.prev_button = tk.Button(
            nav_frame,
            text="Previous Question",
            font=("Comic Sans MS", 12, "bold"),
            bg=self.secondary_color,
            fg=self.text_color,
            padx=10,
            pady=8,
            bd=0,
            command=self.prev_question,
            state=tk.DISABLED
        )
        self.prev_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        self.next_button = tk.Button(
            nav_frame,
            text="Next Question",
            font=("Comic Sans MS", 12, "bold"),
            bg=self.secondary_color,
            fg=self.text_color,
            padx=10,
            pady=8,
            bd=0,
            command=self.next_question
        )
        self.next_button.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))
        
        # Footer
        footer_frame = tk.Frame(main_frame, bg="#f9f9f9", pady=10)
        footer_frame.pack(fill=tk.X)
        
        footer_label = tk.Label(
            footer_frame,
            text="Created with love for Gazal's first birthday! 💕",
            font=("Comic Sans MS", 10),
            bg="#f9f9f9",
            fg=self.text_color
        )
        footer_label.pack()
        
        # Update the display
        self.update_question_display()
    
    def update_question_display(self):
        """Update the question display and navigation buttons"""
        # Update question number
        self.question_number_label.config(text=f"Question {self.current_question_index + 1}/155")
        
        # Update question text
        self.question_text_label.config(text=self.questions[self.current_question_index])
        
        # Update navigation buttons
        self.prev_button.config(state=tk.NORMAL if self.current_question_index > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_question_index < len(self.questions) - 1 else tk.DISABLED)
        
        # Update prediction list
        self.update_prediction_list()
    
    def update_prediction_list(self):
        """Update the prediction list display"""
        # Clear the listbox
        self.prediction_listbox.delete(0, tk.END)
        
        # Get current predictions
        current_predictions = self.predictions[self.current_question_index]
        
        # Count predictions by value
        prediction_counts = {}
        for prediction in current_predictions:
            prediction_counts[prediction] = prediction_counts.get(prediction, 0) + 1
        
        # Sort by count (descending)
        sorted_predictions = sorted(prediction_counts.items(), key=lambda x: x[1], reverse=True)
        
        # Add to listbox
        for prediction, count in sorted_predictions:
            self.prediction_listbox.insert(tk.END, f"{prediction} ({count})")
        
        # Update count label
        self.prediction_count_label.config(text=f"Total Predictions: {len(current_predictions)}")
    
    def add_prediction(self):
        """Add a new prediction"""
        prediction_text = self.prediction_entry.get().strip()
        
        if prediction_text:
            # Add to predictions
            self.predictions[self.current_question_index].append(prediction_text)
            
            # Save predictions
            self.save_predictions()
            
            # Clear entry
            self.prediction_entry.delete(0, tk.END)
            
            # Update display
            self.update_prediction_list()
            
            # Show confirmation
            messagebox.showinfo("Prediction Added", "Your prediction has been added!")
        else:
            messagebox.showwarning("Empty Prediction", "Please enter a prediction before submitting.")
    
    def prev_question(self):
        """Go to previous question"""
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.update_question_display()
    
    def next_question(self):
        """Go to next question"""
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.update_question_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = GazalPredictionGame(root)
    root.mainloop()