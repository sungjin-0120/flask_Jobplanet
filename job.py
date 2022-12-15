def save_to_file(file_name, pls):
  with open(f"{file_name}.csv","w", encoding="utf8" ) as FIle:
    FIle.write("Company, Location, Occupation, Size, Exp, Link\n")

    for pl in pls:
      FIle.write(
        f"{pl['company']},{pl['region']},{pl['occupation']},{pl['size']},{pl['exp']},{pl['link']}\n"
      )
