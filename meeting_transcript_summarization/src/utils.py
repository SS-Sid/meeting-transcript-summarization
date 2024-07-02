def read_transcript(file_path):
    with open(file_path, 'r') as file:
        transcript = file.read()
    return transcript