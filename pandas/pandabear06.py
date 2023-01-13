#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Challenge Solution 01 - CSV to Excel"""

import pandas

def main():

    # create a dataframe from csv
    df = pandas.read_csv("5movies.csv")

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")

    df.info()
    print(df.head())
    print("Max length of movie : ", df.Duration.max())

    print("Oldest Movie was made in : ", df.Year.min())

if __name__ == "__main__":
    main()

