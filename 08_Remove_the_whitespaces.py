# This is one sentence output with the different variabels
Dua_Lipa = " Dua Lipa"
Julio_Iglesias = "Julio Iglesias "
Ariana_Grande = " Ariana Grande "
message = "Sentence with whitespaces: \n" + "My favourite artists are: " + Dua_Lipa + ", " + Julio_Iglesias + " and " + Ariana_Grande + "!"
print(message + "\n")



# Adding the .rstrip() function to remove the extra whitespaces on the right side
Dua_Lipa = " Dua Lipa"
Julio_Iglesias = "Julio Iglesias "
Ariana_Grande = " Ariana Grande "
message = "Output of rstrip(): \n" + "My favourite artists are: " + Dua_Lipa.rstrip() + ", " + Julio_Iglesias.rstrip() + " and " + Ariana_Grande.rstrip() + "!"
print(message + "\n")



# Adding the .lstrip() function to remove the extra whitespaces on the left side
Dua_Lipa = " Dua Lipa"
Julio_Iglesias = "Julio Iglesias "
Ariana_Grande = " Ariana Grande "
message = "Output of lstrip(): \n" + "My favourite artists are: " + Dua_Lipa.lstrip() + ", " + Julio_Iglesias.lstrip() + " and " + Ariana_Grande.lstrip() + "!"
print(message + "\n")



# Adding the .strip() function to remove the extra whitespaces
Dua_Lipa = " Dua Lipa"
Julio_Iglesias = "Julio Iglesias "
Ariana_Grande = " Ariana Grande "
message = "Output of strip(): \n" + "My favourite artists are: " + Dua_Lipa.strip() + ", " + Julio_Iglesias.strip() + " and " + Ariana_Grande.strip() + "!"
print(message + "\n")



# Safe the .strip() as the same variabel, we need to rewrite the same variable for one time
Dua_Lipa = " Dua Lipa"
Dua_Lipa = Dua_Lipa.strip()
Julio_Iglesias = "Julio Iglesias "
Julio_Iglesias = Julio_Iglesias.strip()
Ariana_Grande = " Ariana Grande "
Ariana_Grande = Ariana_Grande.strip()
message = "Without whitespaces: \n" + "My favourite artists are: " + Dua_Lipa + ", " + Julio_Iglesias + " and " + Ariana_Grande + "!"
print(message)