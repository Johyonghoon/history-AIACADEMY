import numpy as np
import pandas as pd

from src.cmm.service.dataset import Dataset

"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
  'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
시각화를 통해 얻은 상관관계 변수(variable = feature = column)는
Pclass
Sex
Age
Fare
Embarked
=== null 값===
Age            177
Cabin          687
Embarked         2
"""


class TitanicModel(object):
    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        b = self.new_model(self.dataset.fname)
        return f'Train type: {type(b)}\n' \
               f'Train columns: {b.columns}\n' \
               f'Train head: {b.head()}\n' \
               f'Train null 개수: {b.isnull().sum()}'

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './save/'
        this.fname = fname
        df = pd.read_csv(this.context + this.fname)
        print(f'데이터프레임 내부 보기: \n{df}')
        return df

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this):
        return this.train['Survived']

    @staticmethod
    def drop_features(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop(i, axis=1)
            this.test = this.test.drop(i, axis=1)
        return this

    @staticmethod
    def sex_norminal(this) -> object:  # male, female
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map({"male": 0, "female": 1})
        return this

    @staticmethod
    def age_ordinal(this) -> object:  # 연령대 10대, 20대, 30대
        for i in [this.train, this.test]:
            i['Age'] = i['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 68, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                             'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in [this.train, this.test]:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def fare_ordinal(this) -> object:  # 비쌈, 보통, 저렴
        for i in [this.train, this.test]:
            i['FareBand'] = pd.qcut(i['Fare'], 4, labels=[4, 3, 2, 1])
        return this

    @staticmethod
    def embarked_norminal(this) -> object:  # 승선 항구 S, C, Q
        # {"S" : 1, "C" : 2, "Q" : 3}
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].map({"S": 1, "C": 2, "Q": 3})
        return this

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]                                        # 첫번째 for문에서 수정한 값을 담아서 다음 for문에 사용하려면 새로 인스턴스로 정의해주어야 담아서 사용할 수 있음
        for i in combine:
            i['Title'] = i.Name.str.extract('([A-Za-z]+)\.', expand=False)       # i.Name 을 해주는 것은 i 가 객체기 때문 / i['']를 하고 싶다면 i가 리스트여야 함 / str은 object의 값을 뜻함
                                                                                 # expand=False 앞의 값이 맞다면 그 값만 가져오라는 뜻
        for i in combine:
            i['Title'] = i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            i['Title'] = i['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            i['Title'] = i['Title'].replace('Mlle', 'Mr')
            i['Title'] = i['Title'].replace('Ms', 'Miss')
            i['Title'] = i['Title'].fillna(0)
            i['Title'] = i['Title'].map({
                'Mr': 1,
                'Miss': 2,
                'Mrs': 3,
                'Master': 4,
                'Royal': 5,
                'Rare': 6
            })
        return this


if __name__ == '__main__':
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = t.age_ordinal(this)
    print(this.train.columns)
    print(this.train.head(10))
