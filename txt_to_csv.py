import pandas as pd
import re

def product_title_extract(string):
    x = re.search('sametab">(.*)</a>', string)
    return x.group(1)


def product_link_extract(string):
    y = re.search('href="(.*)#lnk', string)
    return y.group(1)

def result_txt_to_df(file):
#    file = 'result_babies_6-9m.txt'
    f = open(file, 'r')
    lines = [line for line in f.readlines()]
    f.close()
    product_title_array = map(product_title_extract, lines)
    product_title_list = list(product_title_array)
    product_title_df = pd.DataFrame.from_dict(product_title_list)
    product_link_array = map(product_link_extract, lines)
    product_link_list = list(product_link_array)
    product_link_df = pd.DataFrame.from_dict(product_link_list)
    product_df_all = product_title_df.join(product_link_df, lsuffix='_name', rsuffix='_link')
    return product_df_all

df_12_18m = result_txt_to_df('result_babies_12-18m.txt')
df_5t = result_txt_to_df('result_5t.txt')
df_5t.to_csv('df_5t.csv')
df_12_18m.to_csv('df_12_18m.csv')