from exrc.dlearn.aitrader.models import DnnEnsemble, DnnModel, LstmModel, LstmEnsemble

if __name__ == '__main__':
    DnnModel().create()
    DnnEnsemble().create()
    LstmModel().create()
    LstmEnsemble().create()

