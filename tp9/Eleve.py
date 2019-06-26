class eleve:
    '''Classe représentant un élève.
    
    Example
    -------
    >>> e1 = eleve('1,salmi,said,15.25,14.0,15.5')
    >>> e1
    '1,salmi,said,15.25,14.0,15.5'
    '''
    def __init__(self, texte):
        '''Constructeur pour créer des élèves.
        
        Parameters
        ----------
        texte : str
            une chaine de la forme id,nom,prenom,n1,n2,n3
        Exceptions
        ----------
        AssertionError : si texte ne contient pas 6 champs
        ValueError : echec de conversion de id ou des notes
        '''
        champs = texte.strip().split(',')
        assert len(champs) == 6, 'Nombre de champs non compatible'
        self.id = int(champs[0])
        self.nom = champs[1]
        self.prenom = champs[2]
        self.note1 = float(champs[3])
        self.note2 = float(champs[4])
        self.note3 = float(champs[5])

    def __str__(self):
        'Convertit l\'objet eleve en str.'
        return "{},{},{},{},{},{}".format(self.id, self.nom, self.prenom,
                                 self.note1, self.note2, self.note3)
    def __repr__(self):
        'Représentation de l\'objet eleve.'
        return self.__str__()
    #Todo getters
    def getId(self):
        return self.id
    #Todo setters
    # Méthodes d'instance
    def format(self):
        'Formate l\'élève pour l\'affichage.'
        return '''\n\nEleve #{}\n=======\n{} {}\nNote1 :{}\nNote2 :{}\nNote3 :{}'''.format(self.id, self.nom, self.prenom,
                                 self.note1, self.note2, self.note3)
    
    def moyenne(self):
        'Calcule la moyenne des notes.'
        som = self.note1 + self.note2 + self.note3 
        return som / 3
        

# Gestion des fichiers
class dbeleve:
    '''Gère le stockage des élèves dans un fichier csv.
    
    Les méthodes sont statiques 
    '''
    fichier = "eleves.csv"
    
    @staticmethod
    def getEleve(id):
        '''Retourne l'élève spécifié par l'id.
        
        Parameters
        ----------
        id : int
            identifiant numérique de l'élève.
        Returns
        -------
        eleveencours : eleve
        
        '''
        try:
            trouve = False
            with open(dbeleve.fichier, encoding='utf-8') as fd:
                for line in fd:
                    eleveencours = eleve(line)
                    if id == eleveencours.getId():
                        trouve = True
                        return eleveencours
            if not trouve:
                raise ValueError('Id %d non trouvé' % id)   
                
        except Exception as e:
            print('Impossible de récupérer l\'élève', e)
        
    def getTout():
        try:
            leseleves = []
            with open(dbeleve.fichier, encoding='utf-8') as fd:
                for line in fd:
                    eleveencours = eleve(line)
                    leseleves.append(eleveencours)
        except:
            print('Impossible de récupérer les élèves')
        finally:
            return leseleves
            
    @staticmethod
    def sauverTout(leseleves):
        try:
            assert input('Attention vous allez écraser toutes les données\nContinuer? (o/n) ').upper() == 'O', 'Opération annulée'
            with open(dbeleve.fichier, "w", encoding='utf-8') as fd:
                fd.write('\n'.join(map(str, leseleves)))
        except AssertionError as e:
            print(e)
        except Exception as e:
            print('Impossible d\'effectuer l\'enregistrement', e)
        else:
            print('Ok')

    
    @staticmethod
    def sauverun(uneleve):
        try:
            with open(dbeleve.fichier, "a", encoding='utf-8') as fd:
                fd.write('\n'+str(uneleve))
        except:
            print('Impossible d\'effectuer l\'enregistrement')
        else:
            print('Opération réussie')

class eleveManager():
    leseleves = dbeleve.getTout()
    try:
        id = leseleves[-1].getId()
    except:
        id = 0

    @staticmethod
    def affichertout():
        try:
            assert len(eleveManager.leseleves), 'Aucun élève...'
            for chaqueeleve in eleveManager.leseleves:
                print(chaqueeleve.format())
        except AssertionError as e:
            print(e)
    
    @staticmethod
    def sauverTout():
        dbeleve.sauverTout(eleveManager.leseleves)
    
    @staticmethod
    def sauverun():
        dbeleve.sauverun(eleveManager.leseleves[-1])

    @staticmethod
    def rechercheid():
        id = int(input('Entrez l\'id de l\'élève à chercher'))
        elv = dbeleve.getEleve(id)
        print(elv.format())
    
    @staticmethod
    def ajouter():
        eleveManager.id += 1
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
        elevetxt = "{},{},{},{},{},{}".format(eleveManager.id, nom, prenom, note1, note2, note3)
        elv = eleve(elevetxt)
        eleveManager.leseleves.append(elv)

# IHM
class cli:
    action = {
    'L': eleveManager.affichertout,
    'N': eleveManager.ajouter,
    'R': eleveManager.rechercheid,
    'S': eleveManager.sauverun,
    'A': eleveManager.sauverTout
    }
    
    titre = "\n\n\nGestion des élèves"
    options = ["Nouveau N",
    "Lister L",
    "Rechercher R",
    "Enregistrer S",
    "Enregistrer tout A",
    "Quitter Q",
    ]
    message = "Entrez votre choix : "
    
    @staticmethod
    def menu():
        print(cli.titre)
        for i, option in enumerate(cli.options):
            print("{:0>2}- {:20}({})".format(i+1, option[:-2], option[-1]))
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
            
