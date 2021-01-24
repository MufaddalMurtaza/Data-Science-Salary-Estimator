import pandas as pd
df = pd.read_csv("US_DS_jobs.csv")

#Cleans the columns which are not needed
df.drop("Unnamed: 0", axis = 1, inplace=True)
df.drop("Headquarters", axis=1, inplace=True)
df.drop("Competitors", axis=1, inplace=True)

#Dropping all the duplicate records
df.drop_duplicates(inplace = True)

#Cleaning Salary Estimate column
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('k', "").replace('$',"").replace('-'," "))
minus_perhr = minus_kd.apply(lambda x: x.lower().replace('per hour', ""))

#Adding new features for the Salary Estimate column
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['min_salary'] = minus_perhr.apply(lambda x: int(x.split()[0]))
df['max_salary'] = minus_perhr.apply(lambda x: int(x.split()[1]))
df['avg_salary'] = (df['min_salary'] + df['max_salary']) / 2

#Cleaning Company name column
df['Cleaned_company_name'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-4], axis=1)

#Creating and Cleaning the State Column from Location
df['State'] = df['Location'].apply(lambda x: x.split(',')[-1])
df['State'] = df['State'].apply(lambda x: x.replace('Maryland','MD'))
df['State'] = df['State'].apply(lambda x: x.replace('United States','USA'))
df['State'] = df['State'].apply(lambda x: x.replace('Virginia','VA'))
df['State'] = df['State'].apply(lambda x: x.replace('North Carolina','NC'))
df['State'] = df['State'].apply(lambda x: x.replace('Bristol','TN'))
df['State'] = df['State'].apply(lambda x: x.replace('California','CA'))
df['State'] = df['State'].apply(lambda x: x.replace('Utah','UT'))
df['State'] = df['State'].apply(lambda x: x.strip())

#Creating the city column from the location column
df['City'] = df['Location'].apply(lambda x: x.split(',')[0])

#Creating the Age of the company column
df['Age'] = df['Founded'].apply(lambda x: x if x<1 else 2020 - x)

#language features
#Python
df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#Java
df['Java'] = df['Job Description'].apply(lambda x: 1 if 'java' in x.lower() else 0)
#SQL
df['SQL'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
#Scala
df['Scala'] = df['Job Description'].apply(lambda x: 1 if 'scala' in x.lower() else 0)
#Spark
df['Spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
#Hadoop
df['Hadoop'] = df['Job Description'].apply(lambda x: 1 if 'hadoop' in x.lower() else 0)
#Yarn
df['Yarn'] = df['Job Description'].apply(lambda x: 1 if 'yarn' in x.lower() else 0)
#AWS
df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
#Tableau
df['Tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
#Matplolib
df['Matplotlib'] = df['Job Description'].apply(lambda x: 1 if 'matplotlib' in x.lower() else 0)
#Pandas
df['Pandas'] = df['Job Description'].apply(lambda x: 1 if 'pandas' in x.lower() else 0)
#Seaborne
df['Seaborn'] = df['Job Description'].apply(lambda x: 1 if 'seaborn' in x.lower() else 0)
#Docker
df['Docker'] = df['Job Description'].apply(lambda x: 1 if 'docker' in x.lower() else 0)
#Kubernetes
df['Kubernetes'] = df['Job Description'].apply(lambda x: 1 if 'kubernetes' in x.lower() else 0)
#Neural Networks
df['Neural Networks'] = df['Job Description'].apply(lambda x: 1 if 'neural networks' in x.lower()
                                                                or 'deep learning' in x.lower() else 0)
#R-Studio
df['R'] = df['Job Description'].apply(lambda x: 1 if 'r-studio' in x.lower()
                                                    or 'r studio' in x.lower()
                                                     or ' r ' in x.lower() else 0)
#Nosql
df['Nosql'] = df['Job Description'].apply(lambda x: 1 if 'nosql' in x.lower() or
                                                        'cassandra' in x.lower() or
                                                         'mongodb' in x.lower() or
                                                         'dynamodb' in x.lower() else 0)

#Printing the value counts for all the languages and packages
columns = df.columns
for language in list(columns[20:]):
    print(language)
    print(df[language].value_counts())
    print('\n')

#Converting the cleaned dataset into csv
df.to_csv('US_DS_jobs_(Cleaned).csv')