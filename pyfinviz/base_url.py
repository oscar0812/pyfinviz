import dotenv
import os


def get_url(path):
    if path is None:
        raise ValueError("path must be provided")
    
    found_dotenv = dotenv.find_dotenv()
    elite = True
    if not found_dotenv:
        elite = False
    
    API_KEY = os.environ.get("API_KEY")
    if API_KEY is None:
        elite = False
    if elite:
        return f'https://elite.finviz.com/{path}.ashx?auth={API_KEY}&'
    return f'https://finviz.com/{path}.ashx?'