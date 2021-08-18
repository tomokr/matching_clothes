from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re

df_12_18m = pd.read_csv('df_12_18m.csv')
df_5t = pd.read_csv('df_5t.csv')

def age_group_extract(df):
    y = re.search('^Baby', df['0_name'])
    if y == None:
        df['age_group'] = 'Toddler'
    else:
        df['age_group'] = 'Baby'
    return df

df_12_18m_group = df_12_18m.apply(age_group_extract, axis = 1)
df_5t_group = df_5t.apply(age_group_extract, axis=1)

list_12_18m = df_12_18m_group['0_name'].tolist()
vectorizer = CountVectorizer(list_12_18m,max_df=0.30) #remove boys/girls/baby/carter's
X = vectorizer.fit_transform(list_12_18m)

print(vectorizer.get_feature_names())

no_mean_list = ['18m','12', '2pc', '2pk', '3pc', '3pk', '4pc', '4pk', '6pk', 'and', 'with', 'toddler', 'on','my','for','all','off']
color_list = ['black', 'blue','gray', 'green', 'pink', 'purple', 'red', 'white', 'yellow', 'orange','brown','navy','coral',
              'gold', 'heather','mint','olive']
fashion_list = ['bodysuit', 'cardigan', 'dress', 'footed','hat', 'jumpsuit',  'piece', 'print', 
                 'romper', 'short', 'sleeve', 'socks', 'pajama', 'long', 'rash',
                 'pants','striped','chambray','pull','ruffle','skirtall','sunsuit','overalls','guard', 'hoodie','knit','swim','sweater','footed']

remove_list = no_mean_list + color_list+fashion_list

count_vect_df = pd.DataFrame(X.todense(), columns=vectorizer.get_feature_names())
count_vect_df = count_vect_df.drop(remove_list, axis=1)
df_12_18m_group = df_12_18m_group.drop(['Unnamed: 0'], axis=1)
df_12_18m_word = df_12_18m_group.join(count_vect_df)
list_5t = df_5t_group['0_name'].tolist()
Y = vectorizer.transform(list_5t)
count_5t_df = pd.DataFrame(Y.todense(), columns=vectorizer.get_feature_names())
count_5t_df = count_5t_df.drop(remove_list, axis=1)
df_5t = df_5t.drop(['Unnamed: 0'], axis=1)
df_5t_word = df_5t_group.join(count_5t_df)
df_5t_and_12_18m = pd.concat([df_5t_word, df_12_18m_word])

sum_list = df_5t_and_12_18m.sum(axis=0)
sum_df = sum_list.to_frame()
sum_df = sum_df.drop(['0_link', '0_name','age_group'])
sum_df = sum_df.drop(['Unnamed: 0'])
# sum_df_mod = sum_df[(sum_df[0]>1) & (sum_df[0]<21)]
sum_df_mod = sum_df[(sum_df[0]>1)]
sum_df_mod = sum_df_mod.reset_index()


def generate_html_from_df(df):
    target_url = 'https://www.target.com'
    df['html_string'] = '<a href="'+target_url+df['0_link']+'" target="_blank">'+df['0_name']+'</a>'
    return df
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele+"<br>"
    return str1

html = "<h1>5t/12-18m</h1> <h2>keywords</h2>"
for index, row in sum_df_mod.iterrows():
    html += '<a href="#'+row["index"] + '">' + row["index"] +'</a> '
for index, row in sum_df_mod.iterrows():
    html += '<h2 id="'+row["index"] + '">' + row["index"] +'</h2>'
    df_output = df_5t_and_12_18m[df_5t_and_12_18m[row['index']]==1]
    df_output_html = df_output.apply(generate_html_from_df, axis = 1)
    df_output_list = df_output_html['html_string'].values.tolist()
    html += listToString(df_output_list)

with open('output.html', mode='w') as f:
    f.write(html)