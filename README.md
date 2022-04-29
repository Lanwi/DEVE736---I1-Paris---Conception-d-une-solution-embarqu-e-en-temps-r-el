# DEVE736---I1-Paris---Conception-d-une-solution-embarqu-e-en-temps-r-el

Comment on peut le voir les pompe vont remplir les machines selon leurs besoins, mais lorsque celui-ci est plein cela bloquer, car la tache est complétée. Lorsque la machine 1 aura fait son job et sera vide et aura de nouveaux besoins d'huile moteur les pompe vont de nouveau l'alimenter, ainsi de suite.

The current time is: 8
machine 1 : Début de la tache  (12:08:16) : execution temps = 6
machine 1 bloquée
The current time is: 9
machine 2 : Début de la tache  (12:08:17) : execution temps = 5
machine 2 bloquée

Scheduler tick 3 : 12:08:18
The current time is: 10
pompe1 : Début de la tache  (12:08:18) : execution temps = 7
reservoir du pump bloqué car tank est plein
The current time is: 10
pompe2 : Début de la tache  (12:08:18) : execution temps = 3
 reservoir du pompe1 bloqué
The current time is: 10
machine 1 : Début de la tache  (12:08:18) : execution temps = 7
machine 1 bloquée
The current time is: 11
machine 2 : Début de la tache  (12:08:19) : execution temps = 6
machine 2 bloquée

Scheduler tick 4 : 12:08:20
The current time is: 12
pompe1 : Début de la tache  (12:08:20) : execution temps = 7
reservoir du pump bloqué car tank est plein
The current time is: 12
pompe2 : Début de la tache  (12:08:20) : execution temps = 3
 reservoir du pompe1 bloqué
The current time is: 12
machine 1 : Début de la tache  (12:08:20) : execution temps = 8
Traceback (most recent call last):
