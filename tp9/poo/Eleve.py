class eleve: 
    def __init__(self, texte):
        champs = texte.strip().split(',')
        assert len(champs) == 6, 'Nombre de champs non compatible'
        self.id = int(champs[0])
        self.nom = champs[1]
        self.prenom = champs[2]
        self.note1 = float(champs[3])
        self.note2 = float(champs[4])
        self.note3 = float(champs[5])
    
    def format(self):
        return "\n\nEleve #{}\n==================\n{} {}\nNote1 :{}\nNote2 : {}\nNote3 :{}".format(self.id, self.nom, self.prenom,
                                 self.note1, self.note2, self.note3)
        
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.id, self.nom, self.prenom,
                                 self.note1, self.note2, self.note3)
    def __repr__(self):
        return self.__str__()
    
    def getId(self):
        return self.id
        

# Gestion des fichiers
class dbeleve:
    fichier = "eleves.csv"
    
    @classmethod
    def getEleve(cls, id):
        try:
            with open(cls.fichier, encoding='utf-8') as fd:
                for line in fd:
                    c = eleve(line)
                    if id == c.getId():
                        return c
                
        except Exception:
            print('Impossible de récupérer l\'élève', Exception)
        
    @classmethod
    def getTout(cls):
        try:
            leseleves = []
            with open(cls.fichier, encoding='utf-8') as fd:
                for line in fd:
                    c = eleve(line)
                    leseleves.append(c)
        except:
            print('Impossible de récupérer les élèves')
        finally:
            return leseleves
            
    
    @classmethod
    def sauverTout(cls, leseleves):
        try:
            assert input('Attention vous allez écraser toutes les données\nContinuer? (o/n) ').upper() == 'O'
            with open(cls.fichier, "w", encoding='utf-8') as fd:
                fd.write('\n'.join(map(str, leseleves)))
        except AssertionError:
            print('Opération annulée')
        except Exception:
            print('Impossible d\'effectuer l\'enregistrement', )
        else:
            print('Ok')

    
    @classmethod
    def sauverun(cls, eleve):
        try:
            with open(cls.fichier, "a", encoding='utf-8') as fd:
                fd.write('\n'+str(eleve))
        except:
            print('Impossible d\'effectuer l\'enregistrement', cls)
        else:
            print('Opération réussie')

class eleveManager():
    leseleves = dbeleve.getTout()
    try:
        id = leseleves[-1].getId()
    except:
        id = 0

    @classmethod
    def affichertout(cls):
        for cntct in cls.leseleves:
            print(cntct.format())
    
    @classmethod
    def sauverTout(cls):
        dbeleve.sauverTout(cls.leseleves)
    
    @classmethod
    def sauverun(cls):
        dbeleve.sauverun(cls.leseleves[-1])


    @classmethod
    def ajouter(cls):
        cls.id += 1
        print("\n\n\n*** Ajouter un eleve ***")
        nom = input("Entrez le nom : ")
        prenom = input("Entrez le prenom : ")
        while True:
            try:
                note1 = float(input("Entrez la note 1 : "))
                note2 = float(input("Entrez la note 2 : "))
                note3 = float(input("Entrez la note 3 : "))
                if not (0<= note1 <=20):
                    raise ValueError
            except:
                print("Notes non valide")
            else:
                break
        elevetxt = "{},{},{},{},{},{}".format(cls.id, nom, prenom, note1, note2, note3)
        elv = eleve(elevetxt)
        cls.leseleves.append(elv)

# IHM
class cli:
    action = {
    'L': eleveManager.affichertout,
    'N': eleveManager.ajouter,
    'S': eleveManager.sauverun,
    'A': eleveManager.sauverTout
    }
    
    titre = "\n\n\nGestion des élèves"
    options = ["Nouveau N",
    "Lister L",
    "Rechercher R",
    "Enregistrer S",
    "Enregistrer tout A",
    ]
    message = "Entrez votre choix : "
    
    @staticmethod
    def menu():
        print(cli.titre)
        for i, option in enumerate(cli.options):
            print("{:0>2}- {:20}({})".format(i, option[:-2], option[-1]))
        choix = input(cli.message)
        return choix
    
    @staticmethod
    def loop():
        while True:
            choix = cli.menu()
            try:
                if choix.upper() == 'Q':
                    break
                else:
                    cli.action[choix.upper()]()
            except:
                print("Choix non valide")

def main():
    cli.loop()
    
if __name__ == "__main__":
    main()
            
