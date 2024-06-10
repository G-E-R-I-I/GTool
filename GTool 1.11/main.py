import os
import shutil
import time
from tqdm import tqdm
import yaml
import sys
import re

######### base #########

def file_struct(index=1):

 os.makedirs(directory+"/history")
 os.makedirs(directory+"/common")
 os.makedirs(directory+"/localisation")
 os.makedirs(directory+"/gfx")

 ######### history #########

 os.makedirs(directory+"/history/countries")
 os.makedirs(directory+"/history/states")

 ######### common #########

 os.makedirs(directory+"/common/countries")
 os.makedirs(directory+"/common/country_tags")

 ######### gfx #########

 os.makedirs(directory+"/gfx/flags")
 os.makedirs(directory+"/gfx/flags/small")
 os.makedirs(directory+"/gfx/flags/medium")
 os.makedirs(directory+"/gfx/flags/leaders")

 ######### copy paste #########

 shutil.copyfile(HOI4directory+'/common/countries/colors.txt', directory+'/common/countries/colors.txt')

 shutil.copyfile(HOI4directory+'/common/country_tags/00_countries.txt', directory+'/common/country_tags/00_countries.txt')

 shutil.copyfile(HOI4directory+'\localisation\english\countries_l_english.yml', directory+'\localisation\countries_l_english.yml')
            
 for file in os.listdir(HOI4directory+'/history/states'):
    shutil.copy(HOI4directory+'/history/states' + '/' + file, directory+"/history/states")

print("    -=-----=--------- --=#=----+=--=-      ---=+-:     .=-++---*-+--.   +---*=---==+-+-    +==+===:-+            ")
print("     @@@@@@@@.@@@@@@@@ -@@@@@@@@@@@@@-     :@@@@@@@:    .@@@@@@@@@@@@@@   @@@@@@@@@@@@@@  @@@@@@@@@@@@            ")
print("       +@@@@@. :@@@@@.    @@@@@@:@@ @@=    =@@@@@@@@@      @@@@@@ +@@@@@   @@: @@@@@# *@%  @@@@@@@@@+%*            ")
print("         +@@@@@@@@@@@@@     @@@@@@@@@       .@@@.:@@@@@@     @@@@@@@@@@@-.      :@@@@@=      %@@@@@@@@@@@*          ")
print("         +@@@@@  .@@@@@     @@@@@@ @@=@@#  .@@@@@@@@@@@@+    @@@@@# .@@@@@-     -@@@@@+      @@%   -@@@%@-           ")
print("         #@@@@@@@ @@@@@@@+  @@@@@@@@@@@@@# -@@@%% -@@@@@@@#  @@@@@@@@+@@@@@@#  .#@@@@@@@%+    @@@@@*@@@@@@:           ")
print("")
print("                                                   =@@@#-@@@+-@@@ -@@                                                   ")
print("                                                    *##%  %##  @#%@@                                                     ")
print("                                                     =@*++@#=#.@@+++.                                                     ")
print("")
print("        :%@@@@@@@+ .%%@@@@@@%%%@.         @@@@@@@@@     +@@@@@%%  *@@@@@.  -.    ---:--::.  =---:::-. ---::           ")
print("         :@@@@@@@@- :@@@@@@@@@@@@@@@   *%@@@@@@@@@@@@@@  *@@@@@@@% @@@@@@     .  +@@@@@@@@+ #@@@@@@@@* @@@@@.          ")
print("            @@@@@@     @@@@@@  @@@@@@   @@@@@@@   @@@@@@+   @@@@@@@@* @@@           @@@@@%     *@@@@@:  #@@@            ")
print("             @@@@@@     #@@@@@@@@@@=     %@@@@@@   @@@@@@:   @@+@@@@@@@@@@           @@@@@%      %@%@@@ .@@*             ")
print("              @@@@@@     +@@@@@  %@@@@@   @@@@@@@   @@@@@@    @@+  @@@@@@@@           @@@@@#       %%@%@@@@@              ")
print("              -#@@@@@@*:  +@@@@@@- @@@@@@@. @@@@@@@@@@@@@@@@  :@@@@:. .@@@@@@         .:@@@@@#        @@@@@@@              ")
print("              .*====++#. .*++#@@*+  .=+*=+:    .+*%+++*#+     .+--::    =-:-+         +@#---::*-      .*-:*@                ")
print("")
print("")

#########################################

directory = input("Enter MOD directory: ")
HOI4directory = input("Enter HOI4 directory: ")

response = ("Y")

if input("Press (Y)es to confirm or (no) to skip file pasting ").upper() in response:
    file_struct()
else: print("")
      
for i in tqdm (range (101), 
               desc="Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)
      
def country_creation(index=1):
 countrytag = input("Enter new country tag: ")
 countrycolor = input("Enter country color (like this -> ( 20 40 21 )) : ")
 countryname = input("Enter country name: ")
 countryleader = input("Enter the name of the country leader : ")
 countryideology = input("Enter the ideology of this country [fascism,democratic,neutrality,communism] : ")
 countrycapital = input("Set country capital : ")

 for i in tqdm (range (101), 
               desc="Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)

 # Define the file path 
 folder_path = directory+"/common/countries//" 
 file_name = countryname+".txt"
 file_path = os.path.join(folder_path, file_name) 
 
 # Create the country file
 with open(file_path, 'w') as file: 
    file.write("""
 graphical_culture = eastern_european_gfx
 graphical_culture_2d = eastern_european_2d
               
 #graphical_culture = middle_eastern_gfx
 #graphical_culture_2d = middle_eastern_2d 
                                
    color = {""" + countrycolor + " }") 
  
 # Edit country color
 f = open(directory+"/common/countries/colors.txt", 'a')
 f.write( 

 countrytag + """ = {
	color = rgb { """ + countrycolor + "}" """
	color = rgb { """ + countrycolor + """ }
 }"""
 )

 def prepend_country_tag(directory, countrytag, countryname):
    file_path = os.path.join(directory, "common", "country_tags", "00_countries.txt")

    # Read the existing content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        existing_content = file.read()

    # Create the new content to prepend
    new_content = (
        countrytag + " = \"countries/" + countryname + ".txt\"\n"
    )

    # Combine the new text with the existing content
    combined_content = new_content + existing_content

    # Write the combined content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(combined_content)

 prepend_country_tag(directory, countrytag, countryname)

 ######### history #########

 filepath2 = os.path.join(directory+"/history/countries//",countrytag + " - " + countryname)
        
 with open(filepath2, 'w') as file: 
    file.write("""
       
    capital =""" + countrycapital + """

 set_research_slots = 3

 set_technology = {
	infantry_weapons = 1
	infantry_weapons1 = 1
	tech_recon = 1
	tech_support = 1		
	tech_engineers = 1
	tech_military_police = 1
	tech_mountaineers = 1
	motorised_infantry = 1
	paratroopers = 1
	gw_artillery = 1
	
	mass_assault = 1
	fleet_in_being = 1

 set_politics = {
	ruling_party = """ + countryideology + """
	last_election = "1936.1.1"
	election_frequency = 48
	elections_allowed = yes
 }

 set_popularities = {
	democratic = 60
	fascism = 30
	communism = 10
	neutrality = 0
 }

 create_country_leader = {
	name = """ '"'+ countryleader + '"' """
	desc = ""
	picture = GFX_portrait_Noe_Zhordania
	expire = "1953.3.1"
	traits = {
		
	}


 """
    )
       

 ######### state modding #########

 def search_files_by_exact_numbers(directory, numbers):
    matches = []
    # Compile regex patterns for each number to match at the beginning of the file name
    patterns = [re.compile(rf'^{number}-') for number in numbers]
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if any of the numbers match exactly at the beginning of the file name
            if any(pattern.search(file) for pattern in patterns):
                matches.append(os.path.join(root, file))
    return matches

 def modify_file(file_path, old_word, new_word):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the old_word with the new_word
    new_content = re.sub(old_word, new_word, content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

 def modify_files(files, old_word, new_word):
    for file_path in files:
        modify_file(file_path, old_word, new_word)

 def main():
    country_states = input("Enter country states like this --> (21 24 43): ")
    numbers_to_search = [int(num) for num in country_states.split()]
    
    old_word = r'\b[A-Z]{3}\b'  # regex to match any 3 letter uppercase word
    new_word = countrytag

    # Search for files
    matched_files = search_files_by_exact_numbers(directory, numbers_to_search)

    # Modify files
    modify_files(matched_files, old_word, new_word)


    # Print out the modified files
    if matched_files:
        print("Modified files:")
        for match in matched_files:
            print(match)
    else:
        print("No files found containing the specified numbers.")


    
 print("All files succesfully moved to their desired directory!")

 ######### color printing #########
 def print_colored(text, color, end='\n'):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m'}
    reset = '\x1b[0m'
    sys.stdout.write(colors.get(color, '') + text + reset + end)

 print_colored('Waring!, please edit the country localisation files by yourself.', color='red')


 if input("Press (Y)es to countinue to country creator or (no) to quit ").upper() in response:
     country_creation()

 else:

   print("Bye")
   quit

if input("Press (Y)es to countinue to country creator or (no) to quit ").upper() in response:
     country_creation()

else:

   print("Bye")
   quit
   