import os
import dotenv

dotenv.load_dotenv()


def get_api_token():
    return os.getenv('TODOIST_API_TOKEN')


def get_raw_data_path():
    return os.path.abspath('./raw-data')


def debug():
    return os.getenv('DEBUG') == "TRUE"
