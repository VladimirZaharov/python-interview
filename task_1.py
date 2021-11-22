from pathlib import Path

def file_name(name):
    answer = Path(name).parts
    answer = answer.split('.')
    answer = '.'.join(answer[:-1])
    return answer[-1]

