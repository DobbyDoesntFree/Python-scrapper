def save_to_file(file_name, jobs):
    file=open(f"{file_name}.csv","w", encoding="utf-8") # create file 
    file.write("Position,Company,Location,URL\n")
                

    for job in jobs:
        file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

    file.close()

# function for save data as csv file