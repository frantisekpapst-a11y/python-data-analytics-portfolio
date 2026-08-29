import numpy as np

sales = np.array([1200, 1500, 900, 1800, 2100])

print(sales)
print(type(sales))

print(sales.mean())
print(np.median(sales))
print(sales.sum())
print(sales.min())
print(sales.max())

print(sales > 1500)

sales_new = sales * 1.10
print(sales_new)

costs = np.array([800, 1000, 700, 1200, 1400])
profit = sales - costs
print(profit)

category = np.where(
    sales > 1500,
    "High",
    "Low"
)
print(category)

values = np.array([10, 20, np.nan, 40, 50])
print(values)

print(np.mean(values))
print(np.nanmean(values))

print(sales[0:3])

print(sales[-2:])

sales = np.array([1200, 1500, 900, 1800, 2100])

print(sales.shape)
print(sales.ndim)
print(sales.size)

data = np.array([
    [1200, 800],
    [1500, 1000],
    [900, 700]
])

print(data)
print(data.shape)
print(data.ndim)
print(data.size)
print(data[:, 0])
print(data[:, 1])

print(data.mean(axis=0))
print(data.mean(axis=1))
print(data.sum(axis=0))
print(data.sum(axis=1))

print(np.nanmean(data, axis=0))
print(np.nanmean(data, axis=1))
print(np.nansum(data, axis=0))
print(np.nansum(data, axis=0))

values = np.array([10, 20, 30, 40])
print(values.dtype)

values = np.array([10, 20, 30.5, 40])
print(values)
print(values.dtype)

data = np.array([
    [1200.5, "text"],
    [1500, 1000],
    [900, 700]
])

print(data.dtype)

conditions = [
    sales >= 1800,
    sales >= 1200
]

choices = [
    "High",
    "Medium"
]

category = np.select(
    conditions,
    choices,
    default="Low"
)
print(category)

q1 = np.percentile(sales, 25)
q2 = np.percentile(sales, 50)
q3 = np.percentile(sales, 75)
print(q1)
print(q2)
print(q3)

q1 = np.percentile(sales, 25)
q3 = np.percentile(sales, 75)
iqr = q3 - q1
print(iqr)

print(np.std(sales))
print(np.var(sales))

values = np.array([1, 2, 2, 3, 3, 3])
print(np.unique(values))

print(np.sort(sales))

array = df["sales"].to_numpy()
series = pd.Series(array)