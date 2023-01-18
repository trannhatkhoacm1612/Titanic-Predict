from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

x = np.random.rand(100,2)
y = np.random.randint(0,2,100)

x_train, x_test, y_train,y_test = train_test_split(x,y,test_size=0.2)

log = LogisticRegression()
log.fit(x_train,y_train)

y_pre = log.predict(x_test)

print('Acurancy: ',accuracy_score(y_test,y_pre))
