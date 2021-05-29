import pandas

db=pandas.read_csv("Salary_Data.csv")

print("Data Set uploaded")


x=db["YearsExperience"].values.reshape(30, 1)


y=db["Salary"]



from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x, y)

model.coef_

model.intercept_

print("Model Created Suceessfully")

n = float(input("Enter Year of Experince: "))

p = model.predict([[n]])

print("The expected salary: ")
print(p)

