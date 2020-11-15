# Flot D'un Réseau

**Auteur : Eliot Viseux**

## Description des Versions et commandes


---

#### Version 2 :

La version utilise à la place de l'algorithme de calcul de flow, la fonction de la librairie NetWorkX `maximum_flow` pour calculer le flot maximal et avoir le dictionnaire des flots sur les arcs.

Elle contient également la méthode `update(self,u,v,capcity)` qui prend en argument les deux sommets de l'arc à modifier et la nouvelle valeur et retourne une erreur si l'arc nexiste pas sinon elle modifie et mets à jour le flot maximal.

***Pour Lancer la commande :***

*Se mettre dans le dossier Version_2 et taper*

```bash
python3 FlowNet.py <nom du fichier.csv> <premier sommet> <deuxième sommet> <nouvelle capacité>
```

un exemple de commande utilisable avec le fichier *'fig42.cvs'* : 
```bash
python3 FlowNet.py 'fig42.csv' 'a' 'c' 9
```

Cela va créer un graphe à partir du fichier, calculer le flot maximal, faire une image .png du réseau, modifier l'arête demandée, recalculer le flot maximal et mettre le résultat dans une autre image .png


## FAQ


*Q1 Qu’est-ce qu’un flot maximal ?*

Dans un graphe **orienté** (S,A), avec S l'ensemble des **sommets** et A des **arcs** qui relient ces sommets. On choisit un somme s qui sera la **source** et un sommet p qui sera le **puit**. Pour chaque arc on associe une **capacité** qui est un nombre positif.

Un **Flot** représente le débit traversant le réseaux de la source jusqu'au puit. On parle de ***Flot Maximal*** quand la somme des débits sortant de la source est maximale.

---



Le chemin (s→a→c→t) peut contenir un débit de : **12**

Le chemin (s→a→c→b→d→t) peut contenir un débit de : 9

Le chemin (s→b→a→c→t) peut contenir un débit de : 4

Le chemin (s→b→d→(c→t,t)) peut contenir un débit de : **11**


Le flot maximal est de ***12+11 = 23***

---

*Q3 Quelles sont les informations à stocker pour modéliser un réseau ?*

Pour modéliser un réseau il faut stocker les noeuds, le noeud source, le noeud puit, les noms des arcs et leur orientation pour un graphe orienté et leur attribut (capacité).

---

*Q4 Qu’est-ce qu’un chemin augmentant (on dit aussi chaîne améliorante ou chemin améliorant) ?*

Il faut définir le **chemin alterné** qui est un chemin dans le graphe dont les arêtes sont alternativement dans le chemin et hors du chemin

Un **chemin augmentant** est un chemin alterné dont la source et l'arrivé sont des sommets qui ne sont pas couvert par le chemin.
Si un chemin est augmentant, alors il n'est pas maximal.

---

*Q5 Qu’est-ce qu’un réseau résiduel ? A quoi cela sert-il ?*

Un réseau résiduel est une notation du réseau qui indique la quantité de capacité disponible, il est utile pour savoir si le flot d'un réseau est maximal car sur un si un **réseau résiduel ne contient pas de chemin, alors le flot est maximal**

---

*Q6 Quels sont les algorithmes de calcul de flot disponibles dans NetworkX ?*

NetworkX dispose de deux fonctions `maximum_flow` qui renvoie la valeur du flot maximal et le dctionnaire des flots et `maximum_flow_value` qui renvoie juste la valeur du flot maximal.

---


