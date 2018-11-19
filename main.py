from nltk import word_tokenize
from get_data import get_data


def main():
    tasks = get_data()
    print('Total Number of Tasks %s' % len(tasks))

    task_one = tasks[0]
    print('First Task \'%s\'' % task_one['content'])
    print(word_tokenize(task_one['content']))


if __name__ == "__main__":
    main()
    # TODO: https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html