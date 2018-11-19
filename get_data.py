#
# Get the raw data from Todoist
#
from todoist.api import TodoistAPI
from settings import get_api_token, get_raw_data_path


def get_data():
    output_path = get_raw_data_path()
    api = TodoistAPI(get_api_token())
    api.sync()

    # Get all Tasks
    tasks = api.items.all()

    tasks_with_labels = [t for t in tasks if len(t['labels']) != 0]
    tasks_without_labels = [t for t in tasks if len(t['labels']) == 0]

    print('Num Tasks with no labels %s' % len(tasks_without_labels))
    print('Num Tasks with labels %s' % len(tasks_with_labels))

    return tasks
