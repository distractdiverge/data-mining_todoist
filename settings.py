import os
import dotenv

dotenv.load_dotenv()


def get_api_token():
    return os.getenv('TODOIST_API_TOKEN')