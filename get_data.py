#
# Get the raw data from Todoist
#
from todoist.api import TodoistAPI
from settings import get_api_token, get_raw_data_path, debug
import pickle
from os import path
import math


def get_data():
    api = TodoistAPI(get_api_token())
    api.sync()

    tasks = api.items.all()

    tasks_with_labels = [t for t in tasks if len(t['labels']) != 0]
    tasks_without_labels = [t for t in tasks if len(t['labels']) == 0]

    test_data_size = math.floor(len(tasks_with_labels) * 0.2);
    test_data = tasks_with_labels[test_data_size:]
    training_data = tasks_with_labels[:test_data_size]

    save(test_data, 'test_data.p')
    save(training_data, 'training_data.p')
    save(tasks_without_labels, 'unlabeled_data.p')

    if debug():
        print('Num Tasks with no labels %s' % len(tasks_without_labels))
        print('Num Tasks with labels %s' % len(tasks_with_labels))

        print('Size of Training Data: %s' % len(training_data))
        print('Size of Test Data: %s' % len(test_data))

    return {
        'test_data': test_data,
        'training_data': training_data,
        'unlabeled_data': tasks_without_labels
    }


def save(data, name):
    output_dir = get_raw_data_path()
    output_path = path.join(output_dir, name)

    pickle.dump(data, open(output_path, 'wb'))


def load(name):
    input_dir = get_raw_data_path()
    input_path = path.join(input_dir, name)
    return pickle.load(open(input_path, 'rb'))
