import csv

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

lr = LogisticRegression()


def get_data():
    data_file = open("../data/company_emo.csv", "r")
    reader = csv.reader(data_file)

    headers = next(reader)
    classify_list = []
    feature_list = []
    for row in reader:
        row_dict = {}
        for i in range(1, len(row) - 1):
            row_dict[headers[i]] = float(row[i])
        classify_list.append(int(row[-1]))
        feature_list.append(row_dict)
    data_file.close()
    dict_vec = DictVectorizer(sparse=False)
    return dict_vec.fit_transform(feature_list), classify_list


def build_logistic(x, y):
    lr.fit(x, y)
    LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                       intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
                       penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
                       verbose=0, warm_start=False)


def test(x, y):
    y_result = lr.predict(x)
    print(classification_report(y, y_result, target_names=['NO', 'YES']))


if __name__ == "__main__":
    train_x, train_y = get_data()
    build_logistic(train_x, train_y)
    test(train_x, train_y)
