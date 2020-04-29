import wget, requests, os 
import pandas as pd

nindex = 0
tindex = 0
tcategory = "Social Sciences" #Elegir categoria

df = pd.read_excel("Free+English+textbooks.xlsx")

for cat in df["English Package Name"].unique():
    try:
        os.mkdir("download/" + tcategory)
    except OSError as error:
        break
        

for index, row in df.iterrows():
     category = row.loc["English Package Name"]
     if category == tcategory:      
         nindex = nindex+1

for index, row in df.iterrows():
        category = row.loc["English Package Name"]
        if category == tcategory:        
            file_name = f"{row.loc['Book Title']}_{row.loc['Edition']}".replace('/','-').replace(':','-')
            url = f"{row.loc['OpenURL']}"
            r = requests.get(url) 
            download_url = f"{r.url.replace('book','content/pdf')}.pdf"
            wget.download(download_url, f"./download/{category}/{file_name}.pdf") 

            tindex = tindex+1
            print(f"downloading {file_name}.pdf Complete .... {tindex}/{nindex}")