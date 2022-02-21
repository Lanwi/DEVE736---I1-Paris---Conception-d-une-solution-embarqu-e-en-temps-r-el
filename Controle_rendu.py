import time
import datetime

class my_task():

	def __init__(self, name, priority, period, execution_time, last_execution, state, huile_moteur, Besoin_huile_moteur):

		self.name = name
		self.priority = priority
		self.period = period
		self.execution_time = execution_time
		self.last_execution_time = last_execution
		self.state = state 
		self.huile_moteur = huile_moteur 
		self.Besoin_huile_moteur = Besoin_huile_moteur


    	############################################################################
	def run(self):
		
		
		global tank_stock
		global roues_stock
		global moteur_stock

		self.last_execution_time = datetime.datetime.now()

		print("\t" + self.name + " : Début de la tache (" + self.last_execution_time.strftime("%H:%M:%S") + ")")
		if(self.name == "Pompe1" or self.name == "Pompe2"):
			if(tank_stock < 50):
				tank_stock += self.huile_moteur
				print("ajout de l'huile moteur au tank  :"+str(self.huile_moteur)+",ainsi le tank contient donc :" + str(tank_stock))
			else : 
				print("Réservoir rempli")
		
		if(self.Besoin_huile_moteur > 0): 
			tank_stock -= self.Besoin_huile_moteur
			if(self.name == "Machine1"):
				roues_stock += 1
				print("Il y aura don"+str(roues_stock)+"roues")
			if(self.name == "Machine2"):
				moteur_stock += 1
				print("on a donc  "+str(moteur_stock)+"moteur")

                if(tank_stock <=0):
                    print("rechargement d'huile moteur dans le tank")
                    pompe_list=[]
                    pompe_list.append(my_task(name="Pompe1",priority =2 , period = 5 ,execution_time=2,last_execution=last_execution,state="",huile_moteur=10,Besoin_huile_moteur=None))
                    pompe_list.append(my_task(name="Pompe1",priority =1 , period = 15 ,execution_time=3,last_execution=last_execution,state="",huile_moteur=10,Besoin_huile_moteur=None))                task_to_run = None 
	                
                    for current_task in pompe_list:
			            task_to_run = current_task
			          task_to_run.run()
				
			print("La "+str(self.name)+"utilise :"+str(self.Besoin_huile_moteur)+" unité d'huile du tank, il reste donc "+str(tank_stock)+" d'huile moteur")

	
		time.sleep(self.execution_time)
		current_hour = datetime.datetime.now()
		print("\t" + self.name + " : fin de la tache  (" + current_hour.strftime("%H:%M:%S") + ")")




if __name__ == '__main__':


	last_execution = datetime.datetime.now()
	
	# global tank_stock
	tank_stock = 0
	roues_stock = 0 
	moteur_stock = 0 	

	# Instanciation of task objects
	task_list = []
	task_list.append(my_task(name="Pompe1", priority = 2, period = 5, execution_time = 2, last_execution = last_execution, state="",huile_moteur=10, Besoin_huile_moteur=None))
	task_list.append(my_task(name="Pompe2", priority = 1, period = 15, execution_time = 3, last_execution = last_execution, state="", huile_moteur=20, Besoin_huile_moteur=None))
	task_list.append(my_task(name="Machine1", priority = 3, period = 5, execution_time = 5, last_execution = last_execution, state="", huile_moteur=None, Besoin_huile_moteur=25))
	task_list.append(my_task(name="Machine2", priority = 4, period = 3, execution_time = 3, last_execution = last_execution, state="", huile_moteur=None, Besoin_huile_moteur=5))

	n = len(task_list)
	for i in range(n):
		for j in range(0, n-i-1):
			if task_list[j].priority > task_list[j+1].priority :
				task_list[j], task_list[j+1] = task_list[j+1], task_list[j]


	#for x in range(n):
		time_now = datetime.datetime.now()
		
		print("\nScheduler tick : " + time_now.strftime("%H:%M:%S"))
		for current_task in task_list:
			task_to_run = current_task
			task_to_run.run()



