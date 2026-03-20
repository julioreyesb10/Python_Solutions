import os

# Número estimado de ejercicios de programación por capítulo 
# para "Starting Out with Python, 3rd Edition"
chapters = {
    2: 15,  # Input, Processing, and Output
    3: 18,  # Decision Structures and Boolean Logic
    4: 15,  # Repetition Structures
    5: 22,  # Functions
    6: 12,  # Files and Exceptions
    7: 15,  # Lists and Tuples
    8: 14,  # More About Strings
    9: 10,  # Dictionaries and Sets
    10: 10, # Classes and Object-Oriented Programming
    11: 3,  # Inheritance
    12: 8,  # Recursion
    13: 8,  # GUI Programming
    14: 6   # Database Programming
}

def create_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for chapter, num_exercises in chapters.items():
        chapter_dir = os.path.join(base_dir, f"Chapter_{chapter:02d}")
        os.makedirs(chapter_dir, exist_ok=True)
        
        for exercise in range(1, num_exercises + 1):
            file_name = f"exercise_{chapter:02d}_{exercise:02d}.py"
            file_path = os.path.join(chapter_dir, file_name)
            
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f'# Starting Out with Python, Third Edition\n')
                    f.write(f'# Capítulo {chapter}, Ejercicio {exercise}\n\n')
                    f.write('def main():\n')
                    f.write('    pass\n\n')
                    f.write('if __name__ == "__main__":\n')
                    f.write('    main()\n')

    print("Archivos de ejercicios creados exitosamente.")

if __name__ == "__main__":
    create_files()
