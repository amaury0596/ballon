import pygame , os
from threading import Thread, RLock

pygame.init()
pygame.font.init( ) 

blue = (113,177,227)
white = (255,255,255)

surfaceW = 800

surfaceH = 500

ballonW = 50
ballonH = 66

nuageW = 300
nuage = 300












surface = pygame.display.set_mode((surfaceW,surfaceH))

pygame.display.set_caption('ballon volant')

img = pygame.image.load('Ballon01.png').convert_alpha( )


imgNuageH = pygame.image.load('NuageHaut.png').convert_alpha( )
imgNuageB = pygame.image.load('NuageBas.png')

surfaceBallon = pygame.Surface((50,60))
surfaceNuage = pygame.Surface((300,300))



print(surface)




	

# thread nuage 

# class nuageHT(Thread):

# 	def __init__(self):

# 		Thread.__init__(self)
		

# 	def run(self):

		

			

		

# 		global pos_nuage

# 		pos_nuage += -0.5

# 		nuageH(pos_nuage,0,imgNuageH)

		

		


			



		








# class ballonT(Thread):

# 	def __init__(self):

# 		Thread.__init__(self)

# 	def run(self):

# 		global x
# 		global y
# 		global y_mouvement
# 		global appuy


		

		





# 		ballon(x,y,img)
		
	


		



# 		for event in pygame.event.get():

			



# 			if event.type == pygame.KEYDOWN:
# 				if event.key == pygame.K_UP :

# 					appuy = True

# 					y_mouvement = -0.5

					


# 			if event.type == pygame.KEYUP and appuy:



# 				y_mouvement = 0.5



# 		y += y_mouvement

# 		if y > surfaceH -40 or y < -surfaceH -10:

# 			gameover()


		

				

		


					    







		



		



		




			

					

























# fin thread nuage


# partie perdu 

def gameover():



	

	

	

	while True :


		pygame.font.init( )







		v = pygame.font.Font('BradBunR.ttf',150)
		r = pygame.font.Font('BradBunR.ttf',20)

		perdu = v.render('PERDU',True,white)

		continu = r.render('Pour continuer, appuyez sur une touche ',True,white)



		surface.blit(perdu,(300,0))
		surface.blit(continu,(300,200))

		pygame.display.update()





		for event in pygame.event.get():



			if event.type == pygame.QUIT :




				print('quitter')

				pygame.quit()



			if event.type == pygame.KEYDOWN :


					print('continué')
					principal()



					

	







					













# fin partie perdu 




def nuageH(x,y,image):


	return surface.blit(image,(x,y))


def nuageB(x,y,image):


	surface.blit(image,(x,y))

		







def ballon(x,y,image):


	surface.blit(image,(x,y))


def principal():

	
	global x
	global y
	global y_mouvement
	global appuy

	


	



	x = 150
	y = 200

	y_mouvement = 0

	game_over = False

	appuy = False

	global pos_nuage

	pos_nuage = 800

	nuageoff = False

	global score 

	score = 0 



	# thread_2 = ballonT()

	





	

	



	while not game_over:



		

		if pos_nuage < -350 :

			pos_nuage = 800
		
		




	

		surface.fill(blue)

		# thread_1 = nuageHT()
		# thread_2 = ballonT()


		# thread_1.start()
		# thread_2.start()

		# thread_1.join()
		# thread_2.join()



		

	

		


	    








		

		

		

		

		ballon(x,y,img)
		nuageH(pos_nuage,-50,imgNuageH)


		

		if nuageoff:

			pos_nuage += -0.1

		



		for event in pygame.event.get():



			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP :

					appuy = True

					nuageoff = True

					y_mouvement = -0.4


			if event.type == pygame.KEYUP and appuy:



				y_mouvement = 0.4



		y += y_mouvement

		if y > surfaceH -40 or y < -surfaceH -10:
			
			print('Votre score est de : ' ,score)
			gameover()


		if y  < 200 and (200 > pos_nuage and pos_nuage > -100) :

			
			print('Votre score est de : ' ,score)
			gameover()

		if (pos_nuage > 50 and pos_nuage < 50.1 )  :

			score += 1 

		




		pygame.display.flip()




		






		



principal()



