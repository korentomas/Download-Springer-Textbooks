import wget, requests, os 
import pandas as pd

nindex = 0
tindex = 0
tcategory = "Everything" #Elegir categoria

# Everything
# Engineering
# Humanities, Social Sciences and Law
# Mathematics and Statistics
# Behavioral Science
# Biomedical and Life Sciences       
# Chemistry and Materials Science    
# Medicine
# Business and Economics
# Earth and Environmental Science
# Physics and Astronomy
# Computer Science
# Behavioral Science and Psychology
# Energy
# Business and Management
# Religion and Philosophy
# Economics and Finance
# Education
# Law and Criminology
# Social Sciences
# Literature, Cultural and Media Studies
# Intelligent Technologies and Robotics

pre = os.path.dirname(os.path.realpath(__file__))
fname = 'Free+English+textbooks.xlsx'
path = os.path.join(pre, fname)
df = pd.read_excel(path)

for cat in df["English Package Name"].unique():
    try:
        os.mkdir(pre + "/download/" + tcategory) if tcategory != "Everything" else os.mkdir(pre + "/download/" + cat)
    except OSError as error:
        break

for index, row in df.iterrows():
     category = row.loc["English Package Name"]
     if category == tcategory or tcategory == "Everything":      
         nindex = nindex+1

for index, row in df.iterrows():
        category = row.loc["English Package Name"]
        if category == tcategory or tcategory == "Everything":        
            file_name = f"{row.loc['Book Title']}_{row.loc['Edition']}".replace('/','-').replace(':','-')
            url = f"{row.loc['OpenURL']}"
            r = requests.get(url) 
            download_url = f"{r.url.replace('book','content/pdf')}.pdf"
            wget.download(download_url, pre + "/download/" + category +"/" + file_name + ".pdf") 
            tindex = tindex+1
            print(f"downloading {file_name}.pdf Complete .... {tindex}/{nindex}")