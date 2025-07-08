MusicArtists = ["Dua Lipa", "Julio Iglesias", "Ariana Grande"]
DutchCities = ["Amsterdam", "Hilversum", "Den Haag", "Amersfoort", "Arnhem", "Wageningen"]
Tools = ["Github", "Visual Studio Code", "Command Prompt (CMD)"]

print(MusicArtists)
print(DutchCities)
print(Tools)

# Display only the value of Dua Lipa from the variabel MusicArtists
print("This will display the value of Dua Lipa by: ", MusicArtists[0])

# Display only the value of Amersfoort from the variabel DutchCities
print("This will display the value of Amersfoort: ", DutchCities[3])

# Display only the value of Visual Studio Code from the variabel Tools
print("This will display the value Visual Studio Code: ", Tools[-2])

# What will happen with the output of this values?
print("This will display the value in uppercase: ", MusicArtists[0].upper())
print("This will display the value in lowercase: ", DutchCities[3].lower())
print("This will display the value with every new word in uppercase: ", Tools[-2].title())

# Using the custom display in a new sentence
Message = "My favourite artist is " + MusicArtists[1].title() + "."
print(Message)