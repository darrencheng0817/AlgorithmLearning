'''
Created on 2016年2月3日

@author: Darren
'''
'''
// Today, we’re going to be helping Joe. Joe works in a maze.
// Unfortunately, portions of the maze have caught on fire, and
// Joe doesn’t have the maze escape manual in his back pocket.
//
// Poor Joe! But you can help Joe escape the maze.
// 
// Given a maze with both Joe and the squares that are on fire, you
// must determine whether Joe can exit the maze before the fire
// reaches him, and how long it takes him to do it (in minutes).
//
// Joe and the fire each move one square per minute, vertically or 
// horizontally (not diagonally). The fire spreads in four directions
// from each square that is on fire. Joe may exit the maze from any
// square that borders the edge of the maze. Neither Joe nor the fire
// may enter a square that is occupied by a wall.
//
// As an example, consider the maze below:
//
// #############   Legend: J = Joe, F = fire, # = wall, |_ = exit
// # J         #   It will take Joe 14 minutes to exit this maze. 
// ####  ##### #   The fire will be right behind him.
// |  #  #   # #
// |  #F #   # #
// |__#______#_| 
// 
// The maze is represented by the data structure below. I’ve written.
// it in Java, but you can use whatever language you’re most
// proficient in to solve the problem. 

'''
