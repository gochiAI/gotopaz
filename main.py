import requests,re,os,glob,time,random

bundle_url = "https://www-cancer.enish-games.com"
resouce_url = "https://assets.enish-games.com/assets-cancer/Resources/android/"
USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53"
dire = "unity2d"

ver="1_10_10"
url = f"{bundle_url}/v{ver}/resource/list/Android"
response = requests.get(url).text
threads=[]
if "メンテナンス中" in response:
 raise Exception("Server is in maintenance")
# 応答は application/protobufで返ってくるが ここでは正規表現でアドレスを取り出す by Dosugamea
fileNames = re.findall(r"[0-9a-f]{32}", response)
existing_files = {os.path.basename(file) for file in glob.glob("unity2d/*/*")}
urls = [f"{resouce_url}{file}" for file in fileNames if file not in existing_files]

print(len(urls))
print(f"GET process...amout of {len(urls)}")
  
klut=13
Z=5
os.makedirs(f"{dire}/{klut:03d}",exist_ok=True)
for i in urls:
  if Z != 0:
   if len([cv.name for cv in os.scandir(f"{dire}/{klut:03d}")])<1000:
     stime=random.uniform(0.03,0.81)
     print(stime)
     time.sleep(stime)
     with open(os.path.join(f'{dire}/{klut:03d}',os.path.basename(i)),"wb") as bundle:
         bundle.write(requests.get(i).content)          
   else:
      os.system(f"git add {dire}/{klut:03d}")
      os.system(f"git commit -m  '{klut:03d}'")
      os.system("git push")
      klut+=1
      os.makedirs(f"{dire}/{klut:03d}",exist_ok=True)
      Z-=1
      continue
  else:
    os.system(f"git add {dire}/{klut:03d}")
    os.system(f"git commit -m  '{klut:03d}'")
    os.system("git push")