import pandas as pd
import matplotlib.pyplot as plt
import os.path

##########
# Setting files to read
##########

# Dataset of grades to download here :
# https://www.data.gouv.fr/fr/datasets/indicateurs-de-resultat-des-lycees-denseignement-general-et-technologique-1/
file_grades = 'fr-en-indicateurs-de-resultat-des-lycees-denseignement-general-et-technologique.csv'
# Dataset of taxes to download here :
# https://www.data.gouv.fr/fr/datasets/l-impot-sur-le-revenu-par-collectivite-territoriale/
file_taxes = 'ircom_2017_revenus_2016.xlsx'
# Directory where both files are located. Let it empty if it is in the current directory :
filepath = '!!! PASTE YOUR FOLDER PATH HERE !!!'


if filepath != '' and filepath[-1] != '/':
    filepath += '/'
if not (os.path.exists(filepath) and os.path.exists(filepath+file_grades) and os.path.exists(filepath+file_taxes)):
    print("\nPlease put both the files in the same directory, and set \"filepath\" as this directory or let it empty "
          "if the directory is the current one. Else, the datasets will be downloaded each time.\n"
          "Dataset of grades to download here :\n"
          "https://www.data.gouv.fr/fr/datasets/indicateurs-de-resultat-des-lycees-denseignement-general-et"
          "-technologique-1/\nDataset of taxes to download here :\n"
          "https://www.data.gouv.fr/fr/datasets/l-impot-sur-le-revenu-par-collectivite-territoriale/ "
          )
    filepath = ''
    file_taxes = 'https://www.data.gouv.fr/fr/datasets/r/e198657f-eb65-4f19-a3e9-2c8f9ed15699'
    file_grades = 'https://www.data.gouv.fr/fr/datasets/r/7580d6d2-a7bb-4cbb-a78f-5dbaa1891cc4'

print("\n%s the highschool grades Dataset..." % ("Reading" if filepath != '' else "Downloading"), end='')
df_grades = pd.read_csv(filepath + file_grades, sep=';')
print("done!")


def prepare_list_sheets():
    """Sets a list containing the name of all the sheets we need to analyse.
    Since there are letters (for Corsica '2A0 and '2B0', it must be a list of strings."""
    my_sheet_list = []
    for i in range(1, 10):
        my_sheet_list.append('0'+str(i) + '0')
    for i in range(10, 20):
        my_sheet_list.append(str(i) + '0')
    my_sheet_list .append('2A0')
    my_sheet_list.append('2B0')
    for i in range(21, 96):
        my_sheet_list.append(str(i) + '0')
    for i in range(971, 975):
        my_sheet_list.append(str(i))
    my_sheet_list.append('976')
    return my_sheet_list


print("%s the income taxes Dataset..." % ("Reading" if filepath != '' else "Downloading"), end='')
df_taxes = pd.read_excel(filepath+file_taxes, sheet_name=prepare_list_sheets(), skiprows=20)
print('done!')

##########
# Cleaning the grades file
##########


columns_to_keep = ['Taux Brut de Réussite Total séries', 'Effectif Présents Total séries', 'Code commune']
renamed_columns = ['success_rate', 'number_students', 'city_code']


def moyenne_ponderee(group):
    """Weighted average"""
    return pd.Series({'success_rate': (group.success_rate.sum() / group.number_students.sum()),
                     'number_students': group.number_students.max()})


df_grades = df_grades[df_grades['Année'] == 2016][columns_to_keep]
df_grades.columns = renamed_columns
df_grades['success_rate'] = df_grades.success_rate * df_grades.number_students
df_grades = df_grades.groupby('city_code').apply(moyenne_ponderee)
df_grades['size_ratio'] = df_grades.number_students*100 / df_grades.number_students.sum()

##########
# Cleaning the taxes file
##########


def get_dpt_code(c):
    """Sets the departement code to match the format of the other dataset,
    before the concatenation with the city code."""
    c = str(c)
    if len(c) == 3:
        return c[0:2]
    else:
        return c


def get_commune_code(c):
    """Sets the city code to match the format of the other dataset,
    before the concatenation with the department code."""
    if c < 10:
        return '00'+str(c)
    elif c < 100:
        return '0'+str(c)
    else:
        return str(c)


df_taxes = pd.concat(df_taxes, sort=False)
df_taxes = df_taxes[df_taxes.iloc[:, 4] == 'Total'].iloc[:, [1, 2, 3, 4, 5, 7]]
df_taxes['city_code'] = df_taxes.iloc[:, 0].map(get_dpt_code)+df_taxes.iloc[:, 1].map(get_commune_code)
df_taxes = df_taxes.iloc[:, [4, 5, 6]]
df_taxes.columns = ['homes', 'taxes', 'city_code']
df_taxes['taxes'] = pd.to_numeric(df_taxes.taxes, errors='coerce')
df_taxes['homes'] = pd.to_numeric(df_taxes.homes, errors='coerce')
df_taxes = df_taxes.dropna()
df_taxes = df_taxes[df_taxes.taxes > 0]
df_taxes['taxes'] = df_taxes.taxes*1000 / df_taxes.homes
df_taxes = df_taxes[['city_code', 'taxes']]

##########
# Merging both Dataframes on the city codes column
##########

df_final = pd.merge(df_grades, df_taxes, how="inner", on='city_code')
df_final = df_final.groupby('city_code').mean()
plt.scatter(df_final.taxes, df_final.success_rate, df_final.size_ratio*500)
plt.ylabel('Taux de réussite')
plt.xlabel('Impôts moyens par foyer')
plt.title('Taux de réussite moyen au lycée en fonction des impôts par foyer, par commune de France en 2016')
plt.show()
