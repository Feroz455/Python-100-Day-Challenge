question_data = [
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linus Torvalds created Linux and Git.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The logo for Snapchat is a Bell.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The logo for Snapchat is a Bell.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Time on Computers is measured via the EPOX System.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The Windows 7 operating system has six main editions.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The Windows ME operating system was released in the year 2000.",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "Linux was first created as an alternative to Windows XP.",
        "correct_answer": "False",
        "incorrect_answers": ["True"]
    },
    {
        "category": "Science: Computers",
        "type": "boolean",
        "difficulty": "easy",
        "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
        "correct_answer": "True",
        "incorrect_answers": ["False"]
    }
    # ... (other question dictionaries)
]


# import requests

# api_url = 'https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean'

# # Fetch the JSON data from the API
# response = requests.get(api_url)

# if response.status_code == 200:
#     quiz_data = response.json()
#     results = quiz_data["results"]
    
#     for question in results:
#         print("{")
#         for key, value in question.items():
#             if isinstance(value, list):
#                 value_str = ", ".join(f'"{item}"' for item in value)
#                 print(f'"{key}": [{value_str}]')
#             else:
#                 print(f'"{key}": "{value}"')
#         print("},")
# else:
#     print("API request failed with status code:", response.status_code)
