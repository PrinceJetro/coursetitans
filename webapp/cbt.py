from .models import Course, CBTQuestion

questions = [
    {
        'course_id': 4,
        'question_text': "What is the capital of France?",
        'option_a': "Paris",
        'option_b': "London",
        'option_c': "Berlin",
        'option_d': "Madrid",
        'correct_option': "A"
    },
    {
        'course_id': 4,
        'question_text': "What is 2 + 2?",
        'option_a': "3",
        'option_b': "4",
        'option_c': "5",
        'option_d': "6",
        'correct_option': "B"
    },
    # Add more questions as needed
]



# from webapp.cbt import questions
# from webapp.models import Course, CBTQuestion
# from webapp.cbt import questions  # Adjust this import based on the actual location of `cbt.py`

# for question_data in questions:
#     try:
#         course = Course.objects.get(id=question_data['course_id'])
#         CBTQuestion.objects.create(
#             course=course,
#             question_text=question_data['question_text'],
#             option_a=question_data['option_a'],
#             option_b=question_data['option_b'],
#             option_c=question_data['option_c'],
#             option_d=question_data['option_d'],
#             correct_option=question_data['correct_option']
#         )
#         print(f"Added question: {question_data['question_text']}")
#     except Course.DoesNotExist:
#         print(f"Course with ID {question_data['course_id']} does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
