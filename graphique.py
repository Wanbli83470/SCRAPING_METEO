import pandas as pd
test = [1,2,3,4]
test2 = ["lion", 'chien', 'chat', 'elephant']

weather = pd.DataFrame({
    "test": test,
    "test2": test2,
})

print(weather)