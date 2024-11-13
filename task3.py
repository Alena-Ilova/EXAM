import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Student Name': ['Kate', 'Bob', 'Mark', 'Stephan', 'Eva'],
    'Attendance (%)': [90, 85, 78, 65, 95],
    'Marks': [98, 65, 70, 80, 72]
}

df = pd.DataFrame(data)


print(df)

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Attendance (%)', y='Marks', s=100)
plt.title('Correlation between Attendance and Marks')
plt.xlabel('Attendance Percentage (%)')
plt.ylabel('Marks (out of 100)')
plt.grid()
plt.axhline(y=df['Marks'].mean(), color='r', linestyle='--', label='Average Marks')
plt.axvline(x=df['Attendance (%)'].mean(), color='g', linestyle='--', label='Average Attendance')
plt.legend()
plt.show()