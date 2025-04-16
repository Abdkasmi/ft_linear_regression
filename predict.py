import pandas as pd
import matplotlib.pyplot as plt

def estimatePrice(t0, t1, mileage):
    return t0 + (t1 * mileage)

def normalise_km(normalized_km):
    return (normalized_km - data['km'].min()) / (data['km'].max() - data['km'].min())

def denormalise_price(normalized_price):
    return (normalized_price * (data['price'].max() - data['price'].min())) + data['price'].min()

try:
    theta_data = pd.read_csv('theta.csv')
    data = pd.read_csv('data.csv')
    theta0 = theta_data['theta0'][0]
    theta1 = theta_data['theta1'][0]

    ml = int(input("Enter your vehicule's mileage: "))

    if theta0 == 0.0 and theta1 == 0.0:
        raise Exception("Cannont predict with Theta0 and Theta1 at 0.0") 
    
    estimated_price = estimatePrice(theta0, theta1, normalise_km(ml))
    price = int(denormalise_price(estimated_price))
    data.plot.scatter(x='km', y='price')
    plt.scatter(ml, price, color='red', label='Predicted Price')
    plt.show()

except ValueError:
    print("Only int values are allowed")
except FileNotFoundError:
    print("Theta0 and Theta1 does not exist. Please train model before")
except Exception as error:
    print(error)
except:
    print("An Error has occured")
