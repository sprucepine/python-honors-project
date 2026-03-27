# Write your actual data processing, AI, or math here
def process_data(user_input: str):
    # Example logic: reverse a string and count characters
    result = user_input[::-1].upper()
    return {
        "processed_text": result,
        "length": len(user_input)
    }