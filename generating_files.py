with open('wordlist') as wordlist:
    file_content = wordlist.read()
    start = file_content[0][0]
    # Finding the characters length where letter changed and genrating all files
    for index,line in enumerate(file_content.split('\n')):
        if line[0] == 'a':
            with open('words/a.txt','a') as current_file:
                current_file.write(f"{line}\n")
        else:
            if line[0].lower() != start:
                start = line[0]
                with open(f'words/{line[0]}.txt','w+') as current_file:
                    current_file.write(f"{line}\n")
            else:
                with open(f'words/{line[0]}.txt','a') as current_file:
                    current_file.write(f"{line}\n")