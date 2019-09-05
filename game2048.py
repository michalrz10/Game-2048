import pygame
import numpy as np
import sys
import random

class Game_control:
	def __init__(self):
		self.tab=np.zeros((4,4),np.int)
		self.random()
		self.score=0
	def reset(self):
		self.tab=np.zeros((4,4),np.int)
		self.random()
		print('Your score: '+str(self.score))
		self.score=0
	def random(self):
		while True:
			a=(random.randint(0,3),random.randint(0,3))
			if self.tab[a[0]][a[1]]==0: break
		self.tab[a[0]][a[1]]=2
		if random.randint(1,10)<=2: self.tab[a[0]][a[1]]=2
		temp=True
		for i in range(4): 
			for j in range(4): 
				if self.tab[i][j]==0: temp=False
		if temp:
			for i in range(4):
				for j in range(3):
					if self.tab[i][j]==self.tab[i][j+1]: return False
					if self.tab[j][i]==self.tab[j+1][i]: return False
			return True
		return False
	def move(self,direction):
		tem=False
		if direction==0: #up
			for i in range(4):
				new=[]
				while True:
					temp=0
					for j in range(1,4):
						if self.tab[j][i]>0:
							if self.tab[j-1][i]==0:
								self.tab[j-1][i]=self.tab[j][i]
								self.tab[j][i]=0
								if j in new:
									for k in range(len(new)):
										if new[k]==j: new[k]==j-1
								tem=True
								break
							elif self.tab[j-1][i]==self.tab[j][i] and j not in new and (j-1) not in new:
								self.tab[j-1][i]+=self.tab[j][i]
								self.score+=self.tab[j-1][i]
								self.tab[j][i]=0
								tem=True
								new.append(j-1)
								break
						temp+=1
					if temp==3: break
		elif direction==1: #right
			for i in range(4):
				new=[]
				while True:
					temp=0
					for j in range(2,-1,-1):
						if self.tab[i][j]>0:
							if self.tab[i][j+1]==0:
								self.tab[i][j+1]=self.tab[i][j]
								self.tab[i][j]=0
								if j in new:
									for k in range(len(new)):
										if new[k]==j: new[k]==j+1
								tem=True
								break
							elif self.tab[i][j+1]==self.tab[i][j] and j not in new and (j+1) not in new:
								self.tab[i][j+1]+=self.tab[i][j]
								self.score+=self.tab[i][j+1]
								self.tab[i][j]=0
								tem=True
								new.append(j+1)
								break
						temp+=1
					if temp==3: break
		elif direction==2: #down
			for i in range(4):
				new=[]
				while True:
					temp=0
					for j in range(2,-1,-1):
						if self.tab[j][i]>0:
							if self.tab[j+1][i]==0:
								self.tab[j+1][i]=self.tab[j][i]
								self.tab[j][i]=0
								if j in new:
									for k in range(len(new)):
										if new[k]==j: new[k]==j+1
								tem=True
								break
							elif self.tab[j+1][i]==self.tab[j][i] and j not in new and (j+1) not in new:
								self.tab[j+1][i]+=self.tab[j][i]
								self.score+=self.tab[j+1][i]
								self.tab[j][i]=0
								tem=True
								new.append(j+1)
								break
						temp+=1
					if temp==3: break
		else: #left
			for i in range(4):
				new=[]
				while True:
					temp=0
					for j in range(1,4):
						if self.tab[i][j]>0:
							if self.tab[i][j-1]==0:
								self.tab[i][j-1]=self.tab[i][j]
								self.tab[i][j]=0
								if j in new:
									for k in range(len(new)):
										if new[k]==j: new[k]==j-1
								tem=True
								break
							elif self.tab[i][j-1]==self.tab[i][j] and j not in new and (j-1) not in new:
								self.tab[i][j-1]+=self.tab[i][j]
								self.score+=self.tab[i][j-1]
								self.tab[i][j]=0
								tem=True
								new.append(j-1)
								break
						temp+=1
					if temp==3: break
		if tem:
			if(self.random()):
				self.reset()
				return -10
			return 10
		return -0.1


class Game:
	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.font=pygame.font.Font(None,25)
		self.window = pygame.display.set_mode((300, 300))
		pygame.display.set_caption(('2048'))
		self.clock = pygame.time.Clock()
		self.points=[]
		self.game=Game_control()
	def show(self):
		self.window.fill((255,255,255))
		#draw
		for i in range(4):
			for j in range(4):
				pygame.draw.rect(self.window,((self.game.tab[i][j]*9)%155+100,(self.game.tab[i][j]*16)%155+100,(self.game.tab[i][j]*25)%155+100),pygame.Rect(75*j,75*i,75,75))
				self.window.blit(self.font.render(str(self.game.tab[i][j]),True,(0,0,0)),(75*j+27,75*i+27))
		for i in range(3):
			pygame.draw.line(self.window,(0,0,0),(i*75+75,0),(i*75+75,300),1)
			pygame.draw.line(self.window,(0,0,0),(0,i*75+75),(300,i*75+75),1)
		
		pygame.display.flip()
		self.clock.tick(60)
	def loop(self):
		while True:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit(0)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.game.move(0)
					if event.key == pygame.K_RIGHT:
						self.game.move(1)
					if event.key == pygame.K_DOWN:
						self.game.move(2)
					if event.key == pygame.K_LEFT:
						self.game.move(3)
			self.show()

game=Game()
game.loop()
