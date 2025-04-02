# Python Programming Quiz with LED Feedback
# Author: [Your Name]
# Date: [YYYY-MM-DD]
# Description: A 5-question Python quiz that provides visual feedback using
#              GPIO-connected LEDs (green for correct, red for incorrect answers)
#              Requires Raspberry Pi with GPIO setup

import RPi.GPIO as GPIO
import time

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GREEN_LED = 17  # GPIO17 for correct answers
RED_LED = 18    # GPIO18 for incorrect answers
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def light_led(led_pin, duration=1):
    """Light up the specified LED for the given duration"""
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(led_pin, GPIO.LOW)

def run_quiz():
    print("Welcome to the Python Programming Quiz!")
    print("Answer the following 5 questions:\n")
    
    # Questions and answers
    questions = [
        {
            "question": "1. Which of the following is NOT a Python data type?",
            "options": ["a) int", "b) float", "c) rational", "d) string", "e) bool"],
            "answer": "c"
        },
        {
            "question": "2. Which of the following is NOT a built-in operation in Python?",
            "options": ["a) +", "b) %", "c) abs()", "d) sqrt()"],
            "answer": "d"
        },
        {
            "question": "3. In a mixed-type expression involving ints and floats, Python will convert:",
            "options": ["a) floats to ints", "b) ints to strings", "c) floats and ints to strings", "d) ints to floats"],
            "answer": "d"
        },
        {
            "question": "4. The best structure for implementing a multi-way decision in Python is:",
            "options": ["a) if", "b) if-else", "c) if-elif-else", "d) try"],
            "answer": "c"
        },
        {
            "question": "5. What statement can be executed in the body of a loop to cause it to terminate?",
            "options": ["a) if", "b) exit", "c) continue", "d) break"],
            "answer": "d"
        }
    ]
    
    score = 0
    
    try:
        for q in questions:
            # Print question and options
            print(q["question"])
            for option in q["options"]:
                print(option)
            
            # Get user answer
            user_answer = input("\nYour answer (enter a, b, c, etc.): ").lower().strip()
            
            # Check answer and provide feedback
            if user_answer == q["answer"]:
                print("✓ Correct! (Green Light)")
                light_led(GREEN_LED)
                score += 1
            else:
                print("✗ Incorrect! (Red Light)")
                light_led(RED_LED)
            print("\n" + "-"*50 + "\n")
        
        # Final results
        print("Quiz completed!")
        print(f"Your final score: {score}/{len(questions)}")
        
        # Blink final result
        if score == len(questions):
            print("Perfect score! Well done!")
            for _ in range(3):
                light_led(GREEN_LED, 0.3)
                time.sleep(0.3)
        elif score >= len(questions)/2:
            print("Good job!")
            for _ in range(2):
                light_led(GREEN_LED, 0.3)
                time.sleep(0.3)
        else:
            print("Keep practicing!")
            light_led(RED_LED, 1.5)
            
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    run_quiz()