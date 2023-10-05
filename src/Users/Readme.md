# HiChat Users API

NB : Les données envoyées au serveur doivent être de type multipart/form-data

* ? → optionnel

# Routes

## /users

| Method                 | POST                                                                                                                                                                       | GET                                                    |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| **_Description_**      | enregistrer un utilisateur                                                                                                                                                 | Récupérer la liste de tous les utilisateurs du serveur |
| **_Entête (Headers)_** | * **Content-Type** : multipart/form-data <br/>                                                                                                                             |                                                        |
| **_Corps (Données)_**  | * **name**<br/>* **surname**<br/>* **email**<br/>* **age**<br/> * **gender**<br/>* **phone**<br/>* **birthday**<br/>* **password**<br/>* **country?**<br/>* **city?**<br/> |                                                        |
| Others                 | * valeurs possible pour _gender_ sont `M`(Masculin) `F`(Féminin) `O`(Autres)<br/>                                                                                          |


