engine = create_engine('sqlite:///mealtime.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# restaurantName = (name = "insert_name", popularity = x, operatingHours="M:00:00-00:00, T:00:00-00:00, W ..... ", address="insert_address")

restaurantMedDel = (name = "Mediterannean Deli", popularity = 1, operatingHours= "M:11:00-22:00, T:11:00-23:00, W:11:00-23:00, R:11:00-22:00, F:11:00-22:00, SA:11:00-22:00, SU:11:00-21:00", address="410 W Franklin St. Chapel Hill, NC 27516")
restaurantRams = (name = "Rams Head Dining Hall", popularity = 5, operatingHours= "M:7:00-0:00, T:7:00-0:00, W:7:00-0:00, R:7:00-0:00, F:7:00-8:00, SA:9:00-8:00, SU:9:00-0:00", address="104 Ridge Rd Chapel Hill, NC 27514")
restaurantLenoir = (name = "Lenoir Dining Hall", popularity = 6, operatingHours= "M:7:00-20:30, T:7:00-20:30, W:7:00-20:30, R:7:00-20:30, F:7:00-15:00, SA:10:00-15:00, SU:10:00-20:00", address="37 Lenoir Dr, Chapel Hill, NC 27599")
restaurantSushinara = (name = "Lenoir Mainstreet Sushinara", popularity = 1, operatingHours= "M:10:30-15:00, T:10:30-15:00, W:10:30-15:00, R:10:30-15:00, F:10:30-16:00, SA:0:00-0:00, SU:0:00-0:00", address="37 Lenoir Dr, Chapel Hill, NC 27599")
restaurantLenoir_Chickfila = (name = "Lenoir Mainstreet Chick-fil-A", popularity = 2, operatingHours= "M:8:30-19:00, T:8:30-19:00, W:8:30-19:00, R:8:30-19:00, F:8:30-16:00, SA:0:00-0:00, SU:0:00-0:00", address="37 Lenoir Dr, Chapel Hill, NC 27599")
restaurantSubway = (name = "Lenoir Mainstreet Subway", popularity = 2, operatingHours= "M:10:30-19:00, T:10:30-19:00, W:10:30-19:00, R:10:30-19:00, F:10:30-16:00, SA:0:00-0:00, SU:0:00-0:00", address="37 Lenoir Dr, Chapel Hill, NC 27599")
restaurantSitar = (name = "Lenoir Mainstreet Sitar", popularity = 1, operatingHours= "M:10:30-15:00, T:10:30-15:00, W:10:30-15:00, R:10:30-15:00, F:10:30-15:00, SA:0:00-0:00, SU:0:00-0:00", address="37 Lenoir Dr, Chapel Hill, NC 27599")
restaurantLenoir_MedDel = (name = "Lenoir Mainstreet Med Deli", popularity = 2, operatingHours= "M:10:30-15:00, T:10:30-15:00, W:10:30-15:00, R:10:30-15:00, F:22:30-15:00, SA:0:00-0:00, SU:0:00-0:00", address="37 Lenoir Dr, Chapel Hill, NC 27599")
restaurantSaladSoups = (name = "Lenoir Mainstreet Salad/Soups", popularity = 1, operatingHours= "M:10:30-17:00, T:10:30-17:00, W:10:30-17:00, R:10:30-17:00, F:22:30-17:00, SA:0:00-0:00, SU:0:00-0:00", address="37 Lenoir Dr, Chapel Hill, NC 27599")
restaurantHealthyBB = (name = "Healthy Bowl-Bowls", popularity = 1, operatingHours= "M:11:00-16:00, T:11:00-16:00, W:11:00-16:00, R:11:00-16:00, F:11:00-15:00, SA:0:00-0:00, SU:0:00-0:00", address="37 Lenoir Dr, Chapel Hill, NC 27599")
restaurantHealthyBS = (name = "Healthy Bowl-Smoothies", popularity = 1, operatingHours= "M:9:00-16:00, T:9:00-16:00, W:9:00-16:00, R:9:00-16:00, F:9:00-15:00, SA:0:00-0:00, SU:0:00-0:00", address="37 Lenoir Dr, Chapel Hill, NC 27599")
restaurantAlpineB = (name = "Alpine Bagels", popularity = 2, operatingHours= "M:7:00-0:00, T:7:00-0:00, W:7:00-0:00, R:7:00-0:00, F:7:00-22:00, SA:9:00-22:00, SU:11:00-0:00", address="3103 South Rd, Chapel Hill, NC 27599")
restaurantAlpineDC = (name = "Alpine Deli & Café", popularity = 1, operatingHours= "M:8:00-16:00, T:8:00-16:00, W:8:00-16:00, R:8:00-16:00, F:8:00-16:00, SA:0:00-0:00, SU:0:00-0:00", address="104 Manning Dr Chapel Hill, NC 27599")
restaurantStarbucks = (name = "Starbucks", popularity = 2, operatingHours= "M:7:00-0:00, T:7:00-0:00, W:7:00-0:00, R:7:00-0:00, F:7:00-21:00, SA:9:00-21:00, SU:9:00-0:00", address="104 Ridge Rd Chapel Hill, NC 27514")
restaurantFriendsC = (name = "Friends Café", popularity = 1, operatingHours= "M:7:30-18:00, T:7:30-18:00, W:7:30-18:00, R:7:30-18:00, F:7:30-17:00, SA:0:00-0:00, SU:0:00-0:00", address="335 S Columbia St, Chapel Hill, NC 27599")
restaurantWendys = (name = "Wendys", popularity = 3, operatingHours= "M:10:30-14:00, T:10:30-14:00, W:10:30-14:00, R:10:30-15:00, F:10:30-15:00, SA:10:30-15:00, SU:10:30-14:00", address="3103 South Rd, Chapel Hill, NC 27599")
restaurantBeach_Quiznos = (name = "The Beach Quiznos", popularity = 2, operatingHours= "M:10:30-18:00, T:10:30-18:00, W:10:30-18:00, R:10:30-18:00, F:10:30-15:00, SA:0:00-0:00, SU:0:00-0:00", address="160 N Medical Dr, Chapel Hill, NC 27599")
restaurantBeach_Chickfila = (name = "The Beach Chick-fil-A", popularity = 2, operatingHours= "M:7:00-16:00, T:7:00-16:00, W:7:00-16:00, R:7:00-16:00, F:7:00-15:00, SA:0:00-0:00, SU:0:00-0:00", address="161 N Medical Dr, Chapel Hill, NC 27599")
restaurantBeach_Green = (name = "The Beach Green", popularity = 1, operatingHours= "M:7:00-15:00, T:7:00-15:00, W:7:00-15:00, R:7:00-15:00, F:7:00-15:00, SA:0:00-0:00, SU:0:00-0:00", address="162 N Medical Dr, Chapel Hill, NC 27599")

session.add(restaurantMedDel)
session.add(restaurantRams)
session.add(restaurantLenoir)
session.add(restaurantSushinara)
session.add(restaurantLenoir_Chickfila)
session.add(restaurantSubway)
session.add(restaurantSitar)
session.add(restaurantLenoir_MedDel)
session.add(restaurantSaladSoups)
session.add(restaurantHealthyBB)
session.add(restaurantHealthyBS)
session.add(restaurantAlpineB)
session.add(restaurantAlpineDC)
session.add(restaurantStarbucks)
session.add(restaurantFriendsC)
session.add(restaurantWendys)
session.add(restaurantBeach_Quiznos)
session.add(restaurantBeach_Chickfila)
session.add(restaurantBeach_Green)

session.commit()
