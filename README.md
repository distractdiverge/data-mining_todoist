# Todoist Data Mining
A simple data mining program to look at all of my todo items,
and re-categorize the tasks.

## Prerequesites
 * Python 3
 * Pipenv

## Getting Started
1. Clone this Repository
```
git clone git@github.com:alexlapinski/data-mining_todoist.git
```

2. Create ```.env``` file (copy ```.env.sample```) and supply values.
```
cp .env.sample .env
```

3. Run pipenv install
```
pipenv install
```

4. Run main file
```
pipenv exec python main.py
```

## Process
1. Fetch raw data
2. Write out possible categories
3. Split data into 2 groups (with existing categories & without)
    1. For data w/ caegories, further split this into training & test data
    2. Write data to file for later use
4. Prepare training data
    1. Split todo task into words
    2. remove stop words
    3. create bag of words for each task
    4. associate task with pre-existing categories
5. Train model on input data
6. Execute model on test set to determine efficency
7. Output results
8. Write new categories back to todoist

