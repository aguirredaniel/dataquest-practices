import pandas as pd


# 1. Create a boolean series, motor_bool, that compares whether the values in the industry column from the f500
#    dataframe are equal to "Motor Vehicles and Parts".
# 2. Use the motor_bool boolean series to index the country column. Assign the result to motor_countries.
def main():
    f500 = pd.read_csv('../f500.csv')
    motor_bool = f500['industry'] == 'Motor Vehicles and Parts'
    motor_countries = f500.loc[motor_bool, 'country']

    print(motor_countries)



if __name__ == "__main__":
    main()
