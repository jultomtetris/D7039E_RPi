


        if quadrant == 1:
        	# traverse down from top wall
	        i = 0
	        x = distY / 
	        while True:
	        	if i >= distY:
	        		break

	        	if round( distY / self.mowOffset ) > 0:
	        		print "fire Line"

	        	i+=1

			# traverse right from left wall
	        i = 0

	        while True:
	        	if i >= distX:
	        		break

	        	if floor( distX / self.mowOffset ) > 0:
	        		print "fire Line"

	        	i+=1