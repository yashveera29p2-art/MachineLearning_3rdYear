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


def Q_A4():
    file = "Lab Session Data (1).xlsx"
    df = pd.read_excel(file, sheet_name="thyroid0387_UCI")
    print("\nattributes:")
    print(df.columns)
    print("\ndatatypes:")
    print(df.dtypes)
    print("\nencoding:")

    for col in df.columns:
        if df[col].dtype == "object":
            if df[col].nunique() <= 10:
                print(col, "-> one hot encoding")
            else:
                print(col, "-> label encoding")
        else:
            print(col, "-> no encoding needed")

    print("\nrange of numeric data:")
    num = df.select_dtypes(include=np.number)
    for col in num.columns:
        print("\n", col)
        print("min :", num[col].min())
        print("max :", num[col].max())

    print("\nmissing values:")
    print(df.isnull().sum())
    print("\noutliers:")

    for col in num.columns:
        q1 = num[col].quantile(0.25)
        q3 = num[col].quantile(0.75)
        iqr = q3 - q1
        low = q1 - 1.5 * iqr
        up = q3 + 1.5 * iqr
        out = num[(num[col] < low) | (num[col] > up)]
        print(col, ":", len(out))

    print("\nmean variance std:")
    for col in num.columns:
        print("\n", col)
        print("mean :", num[col].mean())
        print("variance :", num[col].var())
        print("std :", num[col].std())


def Q_A5():
    file = "Lab Session Data (1).xlsx"
    df = pd.read_excel(file, sheet_name="thyroid0387_UCI")
    b = []
    for col in df.columns:
        u = set(df[col].dropna().astype(str).str.lower().unique())
        if u.issubset({"t", "f"}):
            b.append(col)

    d1 = df.loc[0, b]
    d2 = df.loc[1, b]
    f11 = 0
    f10 = 0
    f01 = 0
    f00 = 0

    for i in range(len(b)):
        a = str(d1.iloc[i]).lower()
        c = str(d2.iloc[i]).lower()
        if a == "t" and c == "t":
            f11 += 1
        elif a == "t" and c == "f":
            f10 += 1
        elif a == "f" and c == "t":
            f01 += 1
        elif a == "f" and c == "f":
            f00 += 1

    if (f11 + f10 + f01) != 0:
        jc = f11 / (f11 + f10 + f01)
    else:
        jc = 0

    smc = (f11 + f00) / (f11 + f10 + f01 + f00)
    print("binary attributes:")
    print(b)
    print("\nf11 :", f11)
    print("f10 :", f10)
    print("f01 :", f01)
    print("f00 :", f00)
    print("\njaccard coefficient :", jc)
    print("simple matching coefficient :", smc)

    if jc > smc:
        print("\njc is more suitable")
    elif smc > jc:
        print("\nsmc is more suitable")
    else:
        print("\nboth are equally suitable")


def Q_A6():
    file = "Lab Session Data (1).xlsx"
    df = pd.read_excel(file, sheet_name="thyroid0387_UCI")
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str)
            df[col] = pd.factorize(df[col])[0]

        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(0)

    v1 = df.iloc[0].to_numpy(dtype=float)
    v2 = df.iloc[1].to_numpy(dtype=float)
    dot = np.dot(v1, v2)
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    cs = dot / (n1 * n2)
    print("cosine similarity :", cs)


def Q_A7():
    file = "Lab Session Data (1).xlsx"
    df = pd.read_excel(file, sheet_name="thyroid0387_UCI")
    df = df.iloc[:20]
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = pd.factorize(df[col].astype(str))[0]

        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(0)

    n = len(df)
    jc = np.zeros((n, n))
    smc = np.zeros((n, n))
    cos = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            a = df.iloc[i].values
            b = df.iloc[j].values
            a1 = (a > 0).astype(int)
            b1 = (b > 0).astype(int)
            f11 = np.sum((a1 == 1) & (b1 == 1))
            f10 = np.sum((a1 == 1) & (b1 == 0))
            f01 = np.sum((a1 == 0) & (b1 == 1))
            f00 = np.sum((a1 == 0) & (b1 == 0))

            if (f11 + f10 + f01) != 0:
                jc[i][j] = f11 / (f11 + f10 + f01)

            smc[i][j] = (f11 + f00) / (f11 + f10 + f01 + f00)

            d = np.dot(a, b)
            n1 = np.linalg.norm(a)
            n2 = np.linalg.norm(b)

            if n1 != 0 and n2 != 0:
                cos[i][j] = d / (n1 * n2)

    plt.figure(figsize=(6,5))
    sns.heatmap(jc)
    plt.title("jaccard coefficient")
    plt.show()
    plt.figure(figsize=(6,5))
    sns.heatmap(smc)
    plt.title("simple matching coefficient")
    plt.show()
    plt.figure(figsize=(6,5))
    sns.heatmap(cos)
    plt.title("cosine similarity")
    plt.show()


def Q_A8():
    file = "Lab Session Data (1).xlsx"
    df = pd.read_excel(file, sheet_name="thyroid0387_UCI")
    for col in df.columns:
        num = pd.to_numeric(df[col], errors="coerce")
        if num.notna().sum() > 0:
            q1 = num.quantile(0.25)
            q3 = num.quantile(0.75)
            iqr = q3 - q1
            low = q1 - 1.5 * iqr
            up = q3 + 1.5 * iqr
            out = num[(num < low) | (num > up)]

            if len(out) == 0:
                val = num.mean()
            else:
                val = num.median()

            df[col] = num.fillna(val)

        else:

            val = df[col].mode()[0]
            df[col] = df[col].fillna(val)

    print("missing values after imputation:")
    print(df.isnull().sum())


def Q_A9():
    file = "Lab Session Data (1).xlsx"
    df = pd.read_excel(file, sheet_name="thyroid0387_UCI")
    ndf = df.copy()
    print("normalized attributes:")
    for col in ndf.columns:
        num = pd.to_numeric(ndf[col], errors="coerce")
        if num.notna().sum() > 0:
            num = num.fillna(num.mean())
            if num.max() != num.min():
                ndf[col] = (num - num.min()) / (num.max() - num.min())
                print(col)

    print("\nnormalized data:")
    print(ndf.head())








def main():
    Q_A1()
    Q_A3()
    Q_A4()
    Q_A5()
    Q_A6()
    Q_A7()
    Q_A8()
    Q_A9()

if __name__=="__main__":
    main()