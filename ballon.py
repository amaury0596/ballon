import pygame , os

pygame.init()
pygame.font.init( ) 

blue = (113,177,227)
white = (255,255,255)

surfaceW = 800

surfaceH = 500

ballonW = 50
ballonH = 66




surface = pygame.display.set_mode((surfaceW,surfaceH))

pygame.display.set_caption('ballon volant')

img = pygame.image.load('Ballon01.png')

print(img)





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



                           

                            
			    

                                

                        

                

	

	

	

	


	

def ballon(x,y,image):

	surface.blit(image,(x,y))


def principal():



	x = 150
	y = 200

	y_mouvement = 0

	game_over = False

	appuy = False

	

	while not game_over :

		

		surface.fill(blue)

		ballon(x,y,img)

		pygame.display.update()



		for event in pygame.event.get():
				
				
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP :

					appuy = True

					y_mouvement = -0.5

			if event.type == pygame.KEYUP and appuy:

				

				y_mouvement = 0.5



		y += y_mouvement

		if y > surfaceH -40 or y < -surfaceH -10:
			gameover()
			




		






		



principal()
       


