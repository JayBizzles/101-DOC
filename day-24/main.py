#TODO: Create a letter using starting_letter.txt

letter_path = "/Input/Letters/starting_letter.txt"
names_path = "/Input/Names/invited_names.txt"
with open(names_path, 'r') as reader, open(letter_path,'r') as writer:
    lines = reader.readlines()
    for line in lines:
        writer.read(0)


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp