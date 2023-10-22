#Questions!

import sqlite3

connection = sqlite3.connect('trivia.db')
cursor = connection.cursor()

music_list = [
    ("Which classical composer was deaf?", "Ludwig van Beethoven")
    ("Who was the first woman to have four country albums reach No. 1 on the Billboard 200?", "Carrie Underwood")
    ("Which astronomer is name-dropped in 'Bohemian Rhapsody?'", "Galileo")
    ("As a child, what singer held the longest note ever on Star Search?", "Usher")
    ("Who sang the Spongebob Squarepants theme song for the movie?", "Avril Lavigne")
    ("What is Post Malone's favorite restaurant?", "Olive Garden")
    ("What Rolling Stones song title is also a restaurant chain?", "Ruby Tuesday")
    ("Weird Al Yankovic mistakenly thought which artist gave his blessing for a parody?", "Coolio")
    ("Who was the first lead guitarist of Metallica", "Dave Mustaine")
    ("Which member of the Avengers had a brief stint as a pop star?", "Brie Larson")
    ]


film_list = [
    ("What does Michael Scott eat for lunch on The Office that makes him fall asleep?", "A whole chicken pot pie")
    ("What is the name of Negan's bat on The Walking Dead?","Lucille")
    ("Michael Cera's character in Arrested Development shares a name with which pop legend?","George Michael")
    ("Which Game of Thrones star was nominated for an Emmy for every single season?","Peter Dinklage")
    ("South Park takes place in which state?","Colorado")
    ("Who was Bart Simpson's teacher?","Mrs. Krabappel")
    ("In The Twilight Zone, who was the howling man?","The Devil")
    ("Which Modern Family character is Claire Dunphy's half-brother?","Joe")
    ("Family Matters began as a spinoff of which sitcom?","Perfect Strangers")
    ("On The Big Bang Theory, Penny is a waitress at which restaurant?","Cheesecake Factory")
]

history_list = [
    ("Wielded by ancient Roman foot soldiers (as well as Maximus in the movie Gladiator), what type of weapon is a gladius?","Sword")
    ("Which former capital of Ancient Egypt is located 12 miles (20 km) south of Cairo on the west bank of the Nile? The city in question shares its name with a city in Tennessee.","Memphis")
    ("The name of the capital of the Byzantine Empire, Constantinople, is the site of which modern-day city?","Istanbul")
    ("El Pilar, located in what is now Belize, and Tikal, in what is now Guatemala, are among the great cities of what ancient Mesoamerican civilization?","Maya")
    ("About 2,000 years before the Egyptians started using it, the Chinchorro people of Chile came up with which process for preserving their dead?","Mummification")
    ("One of the key events in the lead up to the Peloponnesian war, what type of natural disaster caused chaos when it struck Sparta in the year 464BC?","Earthquake")
    ("Sharing a name with the character named in 2003 as the American Film Institute's top villain of the previous 100 years, which Carthaginian general is best remembered today for leading an invasion of Italy having crossed the alps with war elephants?","Hannibal")
    ("What was the two-letter name of the Falcon-headed God of the Sun in ancient Egyptian mythology?","Ra")
    ("Scientists would like to resurrect the woolly kind of which trunked mammal believed to have gone extinct around 1650 B.C.?","Mammoth")
    ("Because they thought it was an antidote to drunkenness, the Ancient Greeks and Romans used what purple gemstone to make drinking goblets that were meant to keep a drinker sober?","Amethyst")
    
]

art_list = [
    ("Where did the art form of calligraphy originate?", "China")
    ("What is the Japanese art of flower arranging called?", "Ikebana")
    ("What artist was a leading figure in the pop art movement and created iconic images of celebrities and everyday objects?", "Andy Warhol")
    ("What Mexican artist, remembered for her self-portraits, was born and died in the same house?", "Frida Kahlo")
    ("What flower is Claude Monet particularly known for?", "Water Lily")
    ("What famous painting by Vincent Van Gogh was painted while he was in a mental asylum?", "The Starry Night")
    ("This famous painting by Edvard Munch in 1893 was actually a series of four paintings. What is it?", "The Scream")
    ("Where is Michelangelo’s work on the ceiling of the Sistine Chapel located?", "Within the Vatican")
    ("")
    ("")
]

#create separate tables in the 'trivia.db' database for each category
cursor.executemany(music_list)
cursor.executemany(film_list)
cursor.executemany(history_list)
cursor.executemany(art_list)

connection.close