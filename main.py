from todoist.api import TodoistAPI
from settings import get_api_token


def main():
    api = TodoistAPI(get_api_token())
    api.sync()
    print(api.state['projects'])


if __name__ == "__main__":
    main()