import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

def Q_A1():
    df=pd.read_excel("Lab Session Data (1).xlsx", sheet_name="Purchase data")
    x=df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].values
    y=df[["Payment (Rs)"]].values

    print(x)
    print(y)

    dim=x.shape[1]
    print("dimensionality of vector space: ",dim)

    vec=x.shape[0]
    print("no of vectors: ",vec)

    rank=np.linalg.matrix_rank(x)
    print("rank of matrix: ",rank)

    pi=np.linalg.pinv(x)
    cost=pi @ y

    print("cost of each product: ")
    print("candy      : ",cost[0][0])
    print("mango      : ",cost[1][0])
    print("milk packet: ",cost[2][0])



def my_mean(data):
    return np.mean(data)

def my_var(data):
    return np.var(data)

def Q_A3():
    df = pd.read_excel("Lab Session Data (1).xlsx", sheet_name="IRCTC Stock Price")
    price = df["Price"].values
    mean = my_mean(price)
    var = my_var(price)

    print("\nMean of Price:", mean)
    print("Variance of Price:", var)

    np_time = 0
    own_time = 0
    for i in range(10):
        start = time.time()
        np.mean(price)
        np.var(price)
        end = time.time()
        np_time += (end - start)

        start = time.time()
        my_mean(price)
        my_var(price)
        end = time.time()
        own_time += (end - start)
    print("\nAverage time using numpy:", np_time / 10)
    print("Average time using own function:", own_time / 10)
    wed = df[df["Day"] == "Wed"]
    wed_mean = np.mean(wed["Price"])
    print("\nWednesday Mean:", wed_mean)
    april = df[df["Month"] == "Apr"]
    april_mean = np.mean(april["Price"])

    print("April Mean:", april_mean)

    loss = df[df["Chg%"] < 0]
    prob_loss = len(loss) / len(df)

    print("\nProbability of Loss:", prob_loss)

    wed_profit = wed[wed["Chg%"] > 0]
    prob_profit_wed = len(wed_profit) / len(df)

    print("Probability of Profit on Wednesday:", prob_profit_wed)

    cond = len(wed_profit) / len(wed)

    print("Conditional Probability (Profit | Wednesday):", cond)

    plt.scatter(df["Day"], df["Chg%"])
    plt.title("Change % vs Day")
    plt.xlabel("Day")
    plt.ylabel("Change %")

    plt.show()






































def main():
    Q_A1()
    Q_A3()

if __name__=="__main__":
    main()