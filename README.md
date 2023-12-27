# Dugeons and Dragons User App Development
My purpose with developing this application is to create a hybrid experience of playing D and D. Mostly, to automate features of the game so players can focus on the story telling process invovled with Dungeons and Drgaons 

## Goals

* Create Auto-Development of Charaters
    * User enters Class and Race and the Character Stats are auto-generated
* Create Live Gameplay Roll
    * Systems will autoroll and add advantage/disadvantage to any dice roll in the game   
* Create Dugeon Master Ability to control game play
    * The dugeon master should have the ability to deal out hit points and place items in a players inventory
* Live Map Renderings
    * Battle Maps are an essential part of D and D
    * Dugeon Master will be able to broadcast the map to players and players will be able to move around the battle map on their turn
* Server Capabilties
    * Players and Dugeon Masters are able to be on their own devices and view live updates via the server
* AI Generation
    * ** **To Be Added At a Later Date** **
    * The ability to use AI image prompting to develope Character Rendering and Battle Maps

## Current Porgress 

**12/22/26**
After fighting with Apple OS not liking anything that isn't apple made, I finally got tkinter up and working! After watching various youtube videos I have a very basic outline of what the GUI stucture will look like and how I can pull data from user input. I'm spending most of today mostly just writing out with pen and paper, how I want the data to flow in / my overall hierachy / UX flow . I also need to do reserach on how to do multiple pages in tkinter so that once a character is created, game play can start.

[Guide to Multiple Pages tkinter](https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/#)
[Ultimate Beginner Tkinter Guide](https://www.youtube.com/watch?v=mop6g-c5HEY)

**12/22/23**

Ive decided a couple of things, because the set up is taking so long time. I am going to for the sake of completetion operate under the assumption that users are only going to choose the barbarian class. Second, I've been trying to find other ways to work around this time consuming issue and I am honestly feeling stuck about the scope of this project. Like yesterday, I took a little time to explore one of the other functonalities of this program I want to include. I started reseraching TKinter to help make my GUIl. I think its important to start integrating this now because user input is so integralo to the set up of characters and having them enter text into the command line just isnt it. After 30 minutes of youtube tutoritals, I got the general gist. Hopefully will get some more work done with it today


**12/21/23**

After getting very frustrated that I was still working only on the character development portion of the game (why I chose one of the most complicated games to automate, I wonder), I decided to take a step back and do some research on server functionalilities in python. I have never worked with servers so I was interested to see how I could fit it in with my program. After garnering a suggestion from a fellow programmer, he recommended DJango for developing a non-static server. 

I watched this  [youtube video](https://youtu.be/rHux0gMZ3Eg?feature=shared).

It was very informative in explaining just exactly was a web server was and why DJango was considered one of the best

I orignally thought server functionality was going to be easy for my program, however this video made me realize I have got my work cut out for me. Backend web development is a whole section of the Computer Science Industry and I may not be able to create a functional project by the end of winter break While I am interested in learning more about web development, for sake of timing on this project, I may look to alternative solutions. 

What those may be, I will have to consult the elders (my brother - a full time Data Engineer)





**12/15/23**

Progress is relatilvly slow. Just chugging out a lot of python lines for calculation. I keep changing my mind on how I want to implement some of the automate calculations. Functions? Dicitionaries. I am really interested once I finish developing this specific section of code to see what optimization I can apply. 



**12/12/23**

Just beginning this project and I am focusing mostly on developing the ability to auto-generate characters. Its a lot more leg work than I thought it would be simply because there are slight differations in character development for each race and class. Futhermore, I still have to be concious of user input, and how much of it is required for this game.




