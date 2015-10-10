engine = create_engine('sqlite:///mealtime.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

restaurantName = (name = "insert_name", popularity = x, operatingHours="M:00:00-00:00, T:00:00-00:00, W ..... ", address="insert_address")


session.add(restaurantName)
session.add(...)
session.add(...)
session.add(...)
session.add(...)
session.add(...)
session.add(...)


session.commit()
