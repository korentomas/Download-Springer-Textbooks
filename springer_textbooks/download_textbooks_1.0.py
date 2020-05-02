import wget, requests, os 
import pandas as pd
from os import listdir
from os.path import isfile, join

nindex = 0
tindex = 0
categories = [
"Engineering",
"Humanities, Social Sciences and Law",
"Mathematics and Statistics",
"Behavioral Science",
"Biomedical and Life Sciences",    
"Chemistry and Materials Science",
"Medicine",
"Business and Economics",
"Earth and Environmental Science",
"Physics and Astronomy",
"Computer Science",
"Behavioral Science and Psychology",
"Energy",
"Business and Management",
"Religion and Philosophy",
"Economics and Finance",
"Education",
"Law and Criminology",
"Social Sciences",
"Literature, Cultural and Media Studies",
"Intelligent Technologies and Robotics",
"Everything"
]

print (*categories, sep = "\n")
print()
input_string = input("Enter a list of categories separated by semicolon: ")
tcategory = input_string.split(";")
tcategory = [x.strip(' ') for x in tcategory]

pre = os.path.dirname(os.path.realpath('__file__'))
fname = 'Free+English+textbooks.xlsx'
path = os.path.join(pre, fname)
df = pd.read_excel(path)
pathd = pre + "/download/"

for cat in df["English Package Name"].unique():
    try:
        for tcat in tcategory:
             os.mkdir(pathd + tcat) if  "Everything" not in tcategory else os.mkdir(pathd + cat)
    except OSError as error:
        break

for index, row in df.iterrows():
     category = row.loc["English Package Name"]
     if category in tcategory or  "Everything" in tcategory:      
         file_name = f"{row.loc['Book Title']}_{row.loc['Edition']}".replace('/','-').replace(':','-')
         files = [f for f in listdir(pathd + category) if isfile(join(pathd + category, f))]
         if file_name + ".pdf" not in files: 
                nindex = nindex+1
                
for index, row in df.iterrows():
        category = row.loc["English Package Name"]
        if category in tcategory or  "Everything" in tcategory:        
            file_name = f"{row.loc['Book Title']}_{row.loc['Edition']}".replace('/','-').replace(':','-')
            url = f"{row.loc['OpenURL']}"
            r = requests.get(url) 
            download_url = f"{r.url.replace('book','content/pdf')}.pdf"
            files = [f for f in listdir(pathd + category) if isfile(join(pathd + category, f))]
            if file_name + ".pdf" not in files: 
                tindex = tindex+1
                print(f"Downloading {file_name}.pdf")
                wget.download(download_url, pathd + f"{category}/{file_name}.pdf")
                print(f" Complete .... {tindex}/{nindex}")
                print(" ")
