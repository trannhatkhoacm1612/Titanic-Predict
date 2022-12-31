# Titanic-Predict

Using Logistic - Regression to predict people will dead or alive base on suitable data

# Logistic - Regression

# # Overall

Different from Linear - Regression that predict a particular value , Logistic - Regression usually return two type of value: True(0) or False(1)

![feature-image](https://miro.medium.com/max/875/1*cgdHP--EdMXJDwCcZSUGfw.png)

# # Mathematics basics

Using Sigmoid - function because of it's classify nature (Z is Linear function)

![feature-image](https://qph.cf2.quoracdn.net/main-qimg-6ab7369356c16f17ac39fbb83d5d56c1)

Reason why we choose this function is:
1. It's differentiable at all values of z ( can use Gradient Decent )
2. It has usefull meaning in classification
3. It's just run in (0;1)

If this function return a value that bigger or equal to 0.5, we will set it True (0)
Else : Set it False (1)



# Introduce 

![feature-image](https://cdn.britannica.com/72/153172-050-EB2F2D95/Titanic.jpg)

There is a problem in Kangle ( https://www.kaggle.com/c/titanic?utm_medium=email&utm_source=gamma&utm_campaign=gamma-onboarding )
You can read the problem from this link and download the dataset to train and solve

# Summarize the problem

We have a dataset about people who in The Titanic. So base on this data, we will predict people will dead or alive.

input : dataframe -> output: Alive(0) or Dead(0)

# Method
1. Preprocessor
2. We can code by yourself but I just Scikit - learn modulo to solve this problem
