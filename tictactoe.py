import sys
class TicTacToe(object):

		ls = []
		p1 = 0
		p2 = 0
		count = 1
		def __init__(self):
				self.begin()
		def checkcell(self,p,i):
				
				try:
					val = int(i)
					if(self.ls[val-1] == '_'):
						self.ls[val-1] = p.upper()
						self.checkboard(p)
						return True
					else:
						return Faself.lse
				except ValueError:
					print 'Invalid Value!'
				return False
			

				
				
		def checkboard(self,p):
				
				if(self.count ==9):
					self.gameover1()
					self.end()
				elif(self.ls[0] == p.upper() and self.ls[1] == p.upper() and self.ls[2] == p.upper()):
					self.gameover(p)
					self.end()
				elif(self.ls[3] == p.upper() and self.ls[4] == p.upper() and self.ls[5] == p.upper()):
					self.gameover(p)
					self.end()
				elif(self.ls[6] == p.upper() and self.ls[7] == p.upper() and self.ls[8] == p.upper()):
					self.gameover(p)
					self.end()
				elif(self.ls[0] == p.upper() and self.ls[3] == p.upper() and self.ls[6] == p.upper()):
					self.gameover(p)
					self.end()
				elif(self.ls[0] == p.upper() and self.ls[4] == p.upper() and self.ls[8] == p.upper()):
					self.gameover(p)
					self.end()
				elif(self.ls[2] == p.upper() and self.ls[5] == p.upper() and self.ls[8] == p.upper()):
					self.gameover(p)
					self.end()
				elif(self.ls[1] == p.upper() and self.ls[4] == p.upper() and self.ls[7] == p.upper()):
					self.gameover(p)
					self.end()
				elif(self.ls[2] == p.upper() and self.ls[4] == p.upper() and self.ls[6] == p.upper()):
					self.gameover(p)
					self.end()
				else:
					self.printboard()
					return True
					
			
			


		def printboard(self):
				
				for c in range(0,9,3):
					print '| ', self.ls[c], ' | ', self.ls[c+1],'| ',self.ls[c+2],' |'		
					
		def gameover1(self):
				self.printboard()
				print 'This game is a Draw!'
				print 'The score is:'
				print 'Player 1: ',self.p1,'\n','Player 2: ', self.p2
				return True

				
				
		def gameover(self,p):
				
				self.printboard()
				if(p.upper() == 'X'):
					print 'Player 1 is the winner!!!'
					print 'The score is:'
					self.p1 += 1
					print 'Player 1: ',self.p1,'\n','Player 2: ', self.p2
				else:
					
					print 'Player 2 is the winner!!!'
					print 'The score is:'
					self.p2 += 1
					print 'Player 1: ',self.p1,'\n','Player 2: ', self.p2
			
			
		def start(self):
				
				
				
				
				self.ls = ['_']*9
				print 'The list is ',self.ls
				
				
				print '*********New Game!*************'
				print 'Player 1 symbol: X'
				print 'Player 2 Symbol: O'
				print 'The list is '
				
				while(self.count <=8):
					if(self.count%2 !=0 ):
						print "Player 1's turn"
						choice = raw_input("Choose a position: ")
						while(self.checkcell('X',choice) != True):
							print 'Invalid Value or cell has already been filled!'
							choice = raw_input("Choose a position: ")
						self.checkboard('X')
						self.count +=1
					
					else:
						
						print "Player 2's turn"
						choice = raw_input("Choose a position: ")
						while(self.checkcell('O',choice) != True):
							print 'Invalid Value or cell has already been filled!'
							choice = raw_input("Choose a position: ")
						
						self.checkboard('O')
						
						self.count += 1
					

		def end(self):
				
				user_input = raw_input('Do you want to continue? (Y or N)')
				if (user_input.upper() == 'Y' or user_input.upper()=='YES'):
					
					self.count =1
					self.start()
				elif(user_input.upper() == 'N' or user_input.upper()=='NO'):
					print 'Thank you. Exiting the game.....'
					sys.exit(0)
				else:
					self.end()


		def begin(self):
				print 'Welcome to Tic Tac Toe!'
				user_input = raw_input('Do you want to start the game? (Y or N)')
				if (user_input.upper() == 'Y' or user_input.upper()=='YES'):
					self.start()
				else:
				 pass
				 
		