from simulator import Simulator

if __name__=="__main__":
        while(True):
                languages = ["EN","TR"]
                for lang in languages:
                        print(f"{languages.index(lang)} - {lang}")
                selectedLanguage=input(">>|")
                if selectedLanguage in "0123456789" :
                        selectedLanguage = int(selectedLanguage)
                        if   0 <= selectedLanguage and  selectedLanguage < len(languages):
                                selectedLanguage = languages[selectedLanguage]
                                break
                        else:
                                continue
                else:
                        selectedLanguage = languages.index(selectedLanguage.upper())
                        if selectedLanguage ==-1:
                                continue
                        else:
                                break
        while(True):
                Simulator(doSave=True,language=selectedLanguage)