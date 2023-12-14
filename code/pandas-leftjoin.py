import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    return person.merge(address,on="personid",how="left")



if __name__ == '__main__':
    person={"personid":[1,2],"name":["x","y"] }
    address={"addid":[4,5],"personid":[1,3]}
    person=pd.DataFrame(person)
    address=pd.DataFrame(address)
    print(person)
    print(address)


    print(combine_two_tables(pd.DataFrame(person),pd.DataFrame(address)))

