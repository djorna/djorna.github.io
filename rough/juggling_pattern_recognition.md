Title: Recognizing Juggling Patterns in My First Mobile Game
Date: 2019-07-08-17:20
Modified: 2019-07-08-17:20
Category: Projects
Tags: Programming, C#, Unity
Slug: juggling-pattern-recognition 
Authors: David Jorna

I started building my first (and so far, only) mobile game in 2 years ago during my yearlong internship. I wanted to make a game that realistically simulated juggling, a hobby I picked up over a decade ago. All of the existing attempts at a juggling game on the Play Store were overly simplistic, and they didn't have capture the zen-like *feel* of juggling that I was envisioning. Which was great news, because it meant my app would be unique.

# An Overview of 3-Ball Juggling Patterns
If you have a social life, you might not be familiar with the myriad juggling patterns that exist. Luckily for you, I wasted the better years of my childhood becoming an expert on the subject. There are quite a few, so I'll limit limit the list to the 6 or 7 basic patterns I included in my game.

1. The Cascade  
This is the pattern that everyone starts out with. It's 


2. The Shower  
This is the pattern that everyone who doesn't know how to juggle tries to do when they're starting out. There is a subtle but important difference between this pattern and preceding ones: instead of throwing the balls alternately, both balls are thrown at the same time. Beginners often struggle with this pattern because they try to throw the balls alternately, which disrupts the flow of the pattern.


3. The Box  
The Box is The Shower's trickier, bidirectional cousin. 


# Recognizing Juggling Patterns with Code  
So now we have a sequence of data points (the player's throws), and we want to classify them into a finite number of categories. Looks like a perfect application for recurrent neural nets, right? Well, not necessarily. I might have taken this approach if I had more experience in machine learning 