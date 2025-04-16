import pandas as pd
import matplotlib.pyplot as plt

def estimatePrice(t0, t1, mileage):
    return t0 + (t1 * mileage)

def getSumT0(t0, t1):
    sumTheta = [estimatePrice(t0, t1, data['km'][i]) - data['price'][i] for i in range(m)]
    return sum(sumTheta)

def getSumT1(t0, t1):
    sumTheta = [(estimatePrice(t0, t1, data['km'][i]) - data['price'][i]) * data['km'][i] for i in range(m)]
    return sum(sumTheta)

def gradient_descent(t0, t1, l):
    grad0 = (1/m) * getSumT0(t0, t1)
    grad1 = (1/m) * getSumT1(t0, t1)
    new_t0 = t0 - l * grad0
    new_t1 = t1 - l * grad1
    
    if (t0 == float('inf') or t1 == float('inf')):
        print('t0 or t1 diverged')
        exit()
    return new_t0, new_t1

def train():
    global theta0, theta1
    for epoch in range(epochs):
        theta0, theta1 = gradient_descent(theta0, theta1, learning_rate)
        cost = compute_cost(theta0, theta1)
        cost_history.append(cost)
        print(f"Epoch {epoch+1}/{epochs} - Cost: {cost}")

def normalise_data():
    data['km'] = (data['km'] - data['km'].min()) / (data['km'].max() - data['km'].min())
    data['price'] = (data['price'] - data['price'].min()) / (data['price'].max() - data['price'].min())

def compute_cost(t0, t1):
    total_cost = 0
    for i in range(m):
        error = estimatePrice(t0, t1, data['km'][i]) - data['price'][i]
        total_cost += error ** 2
    return total_cost / (2 * m)

try:
    data = pd.read_csv('data.csv')

    m = len(data)
    theta0 = 0.0
    theta1 = 0.0
    learning_rate = 0.06
    epochs = 500
    cost_history = []
    normalise_data()
    train()
    values = [{'theta0': theta0, 'theta1': theta1}]
    theta_df = pd.DataFrame(values)
    theta_df.to_csv('theta.csv', header=['theta0', 'theta1'], index=False)
    print('Traiing finished !')
except FileNotFoundError:
    print('File Not found, likely data.csv')
except:
    print('Could not finish traing !')
