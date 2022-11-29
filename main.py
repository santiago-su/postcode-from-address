import sys

import pandas as pd
from random import randint
from geopy.geocoders import Nominatim
from functools import partial
from cli import cli

def eval_results(x):
  try:
    return (x.raw['address']['postcode'] if x.raw['address']['postcode'] else None)
  except:
    return (None, None)


def main():
  input_file = cli(sys.argv[1:])['input_csv']
  output_file = cli(sys.argv[1:])['output_csv']

  #Creating a dataframe with address of locations we want to reterive
  dfs = pd.read_excel(input_file, sheet_name=None, usecols=['ShipperFullAddress'])

  # #Creating an instance of Nominatim Class
  user_agent = 'user_me_{}'.format(randint(10000,99999))
  geolocator = Nominatim(user_agent=user_agent)

  # new dataframe
  df = pd.DataFrame()
  df['postcode'] = dfs['Sheet1']['ShipperFullAddress'].apply(geolocator.geocode, timeout=15, addressdetails=True).apply(lambda x: eval_results(x))
  df['address'] = dfs['Sheet1']['ShipperFullAddress']
  df['id'] = dfs['Sheet1']['idfirm']
  print(df)

  df.to_csv(output_file, encoding='utf-8', index=False)



if __name__ == "__main__":
    main()