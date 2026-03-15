# Rule-Based-AI-Systems
Assignment 2.3 for CAP320-O 'Artificial Intelligence Ecosystem'

## Three AI Based Ideas
Rather than allow AI to dictate my time, I instead prioritized a couple of personal ongoing projects I have been working on, and left it up to AI. It analyzed each, the value, and how suitable it is for the homework.
1. MyHQ 4X Game Planning Tool: Optimization & validation logic AI
2. DnD 4X Fief Simulator: Control Module
3. DnD 4X Fief Simulator: Weather Module

### MyHQ 4X Game Planning Tool: Optimization & validation logic AI
MyHQ was first conceived in 2023, and the concept was realized in Project & Portfolio 2 & 3 (Comp Sci). The application is designed to mirror the qualities of in-game design, but instead through a web-app that can be dynamically modified by the user to serve ANY 4X game. This requires understanding the various kinds of logic and how they interact, and then comparing that across thousands of titles to find the repeating patterns. Developing just the tool side of this is a huge ask-- but the feather in the cap for the project is the implementation of an optimization-focused AI: it tracks how the most proficient designers tackle 
the different challenges and nuances of the varying needs of high-level design. The goal is to develop an understanding of these golden patterns, train them into new users, and document the principles in a 
scholastic manner that pushes humanity to develop smarter systems management and spatial awareness designs.

### DnD 4X Fief Simulator: Control Module
I make Dungeons and Dragons content in my downtime for fun. My crown jewel is a Fief life simulator intended to allow a player to go from adventurer to vassal lord. The core of this module is the player's ability to control the fief, but more than that, a simple rule-based AI is intended so that basic alerts can help players succeed. The scope of this module is massive, and covers the full scope of the fief module- databases, global and local variables, Avrae Aliases, which uses Draconic, a variant of Python, a Web UI to clean up the UX...

### DnD 4X Fief Simulator: Weather Module
Contrary to the extensive scope of the control module, the weather module is a single sub-layer, based on real-world weather simulation programming.
Initially, in my planning for this, I wanted to implement a visual system so that I could create a functional grid map tool that could simulate how storms react with mountains and local temperature gradients 
to produce the different biomes found in a world. Unfortunately, the scope of the assignment is smaller than anticipated, and the deadline is sooner than would be required for a visual tool of such a nature... SO 
my new thought process is to focus smaller: the cell level. How does each cell react and change as different sets of data/rules collide with it?

# CHOSEN: DnD 4X Fief Simulator: Weather Module
Weather and world realism are at the height of my curiosity at this time. I can put together a simulation that runs at 10000x speed to take a basic grid map that demonstrates oceans, lakes, and mountains-- then pass a basic layer of temperature/humidity/elevation over it all to basically PRINT out a real LIVING world. What I'm designing could be used on a scale on par with predictive world colonizing models or understanding how our own home here on Earth came to be. Previously, I created a system already for artists that simulates how weather works to create biomes, but my focus then was on terrain only-- not the conditions that caused it to behave the way it did. I focused on tectonic plates and biome ZONING based on what we understand about the formation of biomes using context, but now I'm hoping to step toward predictive modeling where I can insert any grid-based map, and AI logic will tell me where the deserts, forests, tundras, and jungles would form.

To validate my rule-based weather AI, I created a physical Pangaea model using paint and paper manipulation. By tearing the paper (tectonics) and crumpling it (orographic lift), I established a 'ground truth' for my map. My Python script's goal was to recreate the logic of these physical interactions—specifically, how mountain ranges create rain shadows.

### Pangaea Map Making
#### 7 Biomes, 7 colors
1. Lime - Tropical Rain Forest
2. Green - Temperate Forest
3. Teal - Taiga/Boreal Forest
4. Yellow - Grassland
5. Orange - Savanna/Tropical Grassland
6. Red - Desert
7. Blue - Tundra

### Order of colors based on positioning on planet:
1. Blue
2. Teal
3. Green / Yellow
4. Orange / Red
5. Lime 
——— EQUATOR ———
The pattern is mirrored across the equator

### Take the following steps
#### (OPTIONAL) CREATE TECTONIC PLATES
1. Get a piece of cardboard the same size or larger than your canvas
2. Cut the cardboard into 3-6 different pieces
3. Put a few dots of glue along the edges of each piece where the paper will touch.
4. Pin the paper to the cardboard with toothpicks/thumbtacks at each corner

### CREATE A PANGAEA
1. Get a piece of paper and preferably 7 paint colors, markers, or crayons will do in a pinch
2. Pencil out 1-3 large blobs as close to the middle of the paper as you can.
3. Use the color order for proper biome placement
4. Place medium blobs of color and spread them in strange or expected patterns
5. Dip a toothpick or mini paintbrush in the associated paint color you want to work with; overlap areas where colors merge
6. Allow to dry
7. Add specks of color mixed in to other zones for unique biomes
8. Allow to dry

### CONTINENTS
1. Rip your paper into 2-8 smaller pieces. These are your continents. **IF YOU MADE TECTONIC PLATES:** Pull the paper apart along the plate lines, or cut with an exact-o knife if you want smooth splits. Remove toothpicks/pushpins after ripping
3. Pinch and twist your paper in different areas in small ways; larger pinches will mix colors more. Try to do it away from your glued spots.
4. Crumple paper in areas to create mountain ranges
5. Organize your crumpled papers near the other torn pieces in their fitting spots
6. Take a picture directly above your still twisted, pinched paper, as perpendicular as you can to the surface

### DETAILS
1. Rough out the edges
2. The space(s) between the pieces of paper are your oceans
3. Add speckles of islands both near and far
4. Add rivers and lakes
5. Add one small mini continent for the North Pole
6. One gigantic for the South Arctic

# The Rules of Weather Simulation
The Rule of Three: Biome and Weather Determinants
1. **Thermal Energy (Temperature):** Driven by latitudinal position (proximity to Equator/Poles), this determines the "potential energy" of a cell.
2. **Saturation (Humidity):** Driven by proximity to water sources (oceans/lakes), this determines the "fuel" for storm fronts.
3. **The Catalyst (Elevation):** Acts as a physical barrier. When air is forced upward (Orographic Lift), it cools and loses humidity; when it sinks, it warms and dries (Rain Shadow).

# Responses
## #1
--- DnD 4X Fief Simulator: Weather Module ---
Simulating a collision between a Moving Front (Cell A) and Local Environment (Cell B).

Configure Cell A (The Incoming Front):
Temperature (Cold, Mild, Hot): cold
Humidity (Dry, Damp, Moist): moist

Configure Cell B (The Local Terrain/Environment):
Local Temperature (Cold, Mild, Hot): hot
Elevation (Lowland, Highland, Mountain): lowland

--- AI Analysis of Collision Zone ---
Status: SEVERE ALERT: Tornado formation likely. Warm moist air is being rapidly undercut by the cold front.
Atmosphere: The sky turns a bruised purple and the wind begins to howl in circles.

--- Simulation Complete ---
Press any key to continue . . .

## #2
--- DnD 4X Fief Simulator: Weather Module ---
Simulating a collision between a Moving Front (Cell A) and Local Environment (Cell B).

Configure Cell A (The Incoming Front):
Temperature (Cold, Mild, Hot): hot
Humidity (Dry, Damp, Moist): moist

Configure Cell B (The Local Terrain/Environment):
Local Temperature (Cold, Mild, Hot): hot
Elevation (Lowland, Highland, Mountain): mountain

--- AI Analysis of Collision Zone ---
Status: OROGRAPHIC LIFT: Heavy precipitation on the windward side.
Atmosphere: Clouds snag on the peaks, dumping rain. The leeward side remains a dry rain shadow.

--- Simulation Complete ---
Press any key to continue . . .

## #3
--- DnD 4X Fief Simulator: Weather Module ---
Simulating a collision between a Moving Front (Cell A) and Local Environment (Cell B).

Configure Cell A (The Incoming Front):
Temperature (Cold, Mild, Hot): mild
Humidity (Dry, Damp, Moist): dry

Configure Cell B (The Local Terrain/Environment):
Local Temperature (Cold, Mild, Hot): mild
Elevation (Lowland, Highland, Mountain): lowland

--- AI Analysis of Collision Zone ---
Status: STABLE: No severe weather fronts detected.
Atmosphere: The weather remains calm. Ideal for travel or construction.

--- Simulation Complete ---
Press any key to continue . . .


# Reflection
How the system works:
My rule-based weather AI functions as a logic-gate processor for atmospheric interactions. Rather than using complex fluid dynamics, it utilizes a set of "if-then" rulesets derived from basic meteorological principles: the collision of differing thermal and moisture fronts. By inputting the state of an incoming weather cell and the local environment, the system evaluates the potential for severe events like tornadoes or rain shadows. This mimics early 20th-century weather prediction methods where meteorologists used observed patterns rather than the massive datasets used in modern machine learning.

Challenges with AI Prompting:
The primary challenge in prompting the AI was Scope Creep. Initially, I wanted to build a full 25x25 grid simulation, but through dialogue with the AI, I realized that the core of the assignment was about the logic of the rules, not the complexity of the visualization. I had to pivot the AI from generating a visual tool to generating a Triple-Cell Collision Engine. Another challenge was ensuring the AI understood the Pangaea DIY craft I developed. I had to guide the AI to translate physical paper-crumpling (orographic lift) into specific Python logic gates. This collaborative process taught me that the most effective AI-assisted coding happens when the developer provides the scientific truth (the world-building logic) and the AI provides the mechanical structure (the Python conditionals).

Future of the System:
Because this is only a small part (the engine) of how weather would effect a living, breathing world, the code developed as part of this assignment will later be applied to a larger grid, to multiple cells at a time, utilizing storm fronts that occupy more than a single cell. This exact functionality is nothing new, but there are no products available publicly currently that enable this sort of simplified and easy-to-understand interaction, which could allow hobby story creators to simulate the weather or formation of their world's biomes.
