# Rule-Based-AI-Systems
Assignment 2.3 for CAP320-O 'Artificial Intelligence Ecosystem'

# Three AI Based Ideas
1. MyHQ 4X Game Planning Tool: Optimization & validation logic AI
2. DnD 4X Fief Simulator: Control Module
3. DnD 4X Fief Simulator: Weather Module

## MyHQ 4X Game Planning Tool: Optimization & validation logic AI
MyHQ was first conceived in 2023, and the concept was realized in Project & Portfolio 2 & 3 (Comp Sci).
The application is designed the mirror the qualities of in-game design, but instead through a web-app that can be dynamically modified by the user to serve ANY 4X game.
This requires understanding the various kinds of logic and how they interact, and then comparing that across thousands of titles to find the repeating patterns.
Developing just the tool side of this is a huge asking-- but the feather in the cap for the project is the implementation of an optimization-focused AI: it tracks how the most proficient designers tackle 
the different challenges and nuances of the varying needs of high level design. The goal is to develop an understanding of these golden patterns, train them into new users, and document the principles in a 
scholastic manner that pushes humanity to develop smarter systems management and spacial awareness designs.

## DnD 4X Fief Simulator: Control Module
I make Dungeons and Dragons content in my downtime for fun. My crown jewel is a Fief life simulator intended to allow a player to go from adventurer to vassal lord.
The core to this module is the player's ability to control the fief, but more than that, a simple rule-based AI is intended so that basic alerts can help players succeed.
The scope of this module is massive, and covers the full scope of the fief module- databases, global and local variables, Avrae Aliases which uses Draconic, a variant of Python, a Web UI to clean up the UX...

## DnD 4X Fief Simulator: Weather Module
Contrary to the extensive scope of the control module, the weather module is a single sub-layer, based on real-world weather simulation programming.
Initially in my planning for this, I wanted to implement a visual system so that I could create a functional grid map tool which could simulate how storms react with mountains and local temperature gradients 
to produce the different biomes found in a world. Unfortunately the scope of the assignment is smaller than anticipated and the deadline is sooner than would promote for a visual tool of such a manner... SO 
my new thought process is to focus smaller: the cell level. How does each cell react and change as different sets of data/rules collide with it?

# CHOSEN: DnD 4X Fief Simulator: Weather Module
Weather and world realism is at the height of my curiousity at this time. I can put together a simulation that runs at 10000x speed to take a basic grid map that demonstrates oceans, lakes, and mountains-- then pass a basic layer of temperature/humidity/elevation over it all to basically PRINT out a real LIVING world. What I'm designing could be used on a scale on par with predictive world colonizing models or understanding how our own home here on Earth came to be. Previously, I created a system already for artists that simulates how weather works to create biomes, but my focus then was on terrain only-- not the conditions that caused it to behave the way it did. I focused on tectonic plates and biome ZONING based on what we understand about the formation of biomes using context, but now I'm hoping to step toward predictive modeling where I can insert any grid based map, and AI logic will tell me where the deserts, forests, tundras and jungles would form.
