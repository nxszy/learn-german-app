import requests
import re
from concurrent.futures import ThreadPoolExecutor

def extract_forms(verbs):
    
    for verb in verbs:

        url = "https://pl.bab.la/koniugacja/niemiecki/" + verb
        print(url)
        try:

            session_obj = requests.Session()
            response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})

            forms = [verb]
            for form in ("ich", "du", "er/sie/es", "wir", "ihr", "sie/Sie"):
                pattern = '<div class="conj-person">{}</div>.*?<div class="conj-result">(.*?)</div>'.format(form)
                try:
                    match = re.search(pattern, response.text, re.DOTALL | re.IGNORECASE).group(1)
                except AttributeError as e:
                    print(f"Error whie procesing {verb} : {e}")

                forms.append(match)

            all_forms.append(forms)

        except requests.RequestException as e:
            print(f"Error fetching data for verb {verb}: {e}")


#with open("kod_html.txt", "w", encoding="utf-8") as f:
#    f.write(response.text)

all_forms = []

with open("verbs.csv", "r+", encoding="utf-8") as file:
    text = file.read()
    verbs = [line.split(',')[1] for line in text.split('\n')]

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(extract_forms, [verbs[i:i+20] for i in range(0, len(verbs), 20)])

print(all_forms)

with open("forms.csv", "w+", encoding="utf-8") as f:
    
    for package in sorted(all_forms):
        f.write(",".join(package) + "\n")





 