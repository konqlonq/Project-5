# Imports for this project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Brand, Item, User

engine = create_engine('postgresql://catalog:password@localhost/catalog')
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Creates a Default User to hold example data
user1 = User(name= "konqlonq123", email= "example@123.com")
session.add(user1)
session.commit()

# Creates Brand Apple
brand1 = Brand(name= "Apple")
session.add(brand1)
session.commit()

# Creates Apple Item 1
appleItem1 = Item(name="iPhone6s", description="Apple iPhone6s",
                     price="$1000", brand=brand1, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-6s1.jpg")
session.add(appleItem1)
session.commit()

# Creates Apple Item 2
appleItem2 = Item(name="iPhone6s(Plus)", description="Apple iPhone6s Plus",
                     price="$1000", brand=brand1, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-6s-plus.jpg")
session.add(appleItem2)
session.commit()

# Creates Apple Item 3
appleItem3 = Item(name="iPad Air 2", description="Apple iPad Air 2",
                     price="$1000", brand=brand1, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/apple-ipad-air-2-new.jpg")
session.add(appleItem3)
session.commit()

# Creates Apple Item 4
appleItem4 = Item(name="iPad Mini 4", description="Apple iPad Mini 4",
                     price="$1000", brand=brand1, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/ipad-mini-41.jpg")
session.add(appleItem4)
session.commit()

# Creates Apple Item 5
appleItem5 = Item(name="iPad Pro", description="Apple iPad Pro",
                     price="$1000", brand=brand1, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/apple-ipad-pro-.jpg")
session.add(appleItem5)
session.commit()


#################################################################


# Creates Brand Samsung
brand2 = Brand(name= "Samsung")
session.add(brand2)
session.commit()

# Creates Samsung Item 1
SamsungItem1 = Item(name="Galaxy S6", description="Samsung Galaxy S6",
                     price="$1000", brand=brand2, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s6.jpg")
session.add(SamsungItem1)
session.commit()

# Creates Samsung Item 2
SamsungItem2 = Item(name="Galaxy S6 Edge", description="Samsung Galaxy S6 Edge",
                     price="$1000", brand=brand2, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s6-edge.jpg")
session.add(SamsungItem2)
session.commit()

# Creates Samsung Item 3
SamsungItem3 = Item(name="Galaxy Note 5", description="Samsung Galaxy Note 5",
                     price="$1000", brand=brand2, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/samsung-galaxy-note5.jpg")
session.add(SamsungItem3)
session.commit()

# Creates Samsung Item 4
SamsungItem4 = Item(name="Galaxy Note 8", description="Samsung Galaxy Note 8",
                     price="$1000", brand=brand2, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/samsung-galaxy-note-80-n5100.jpg")
session.add(SamsungItem4)
session.commit()


#################################################################


# Creates Brand LG
brand3 = Brand(name= "LG")
session.add(brand3)
session.commit()

# Creates LG Item 1
LGItem1 = Item(name="LG G4", description="LG's G4",
                     price="$1000", brand=brand3, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/lg-g4-.jpg")
session.add(LGItem1)
session.commit()

# Creates LG Item 2
LGItem2 = Item(name="LG G4 Beat", description="LG's G4 Beat",
                     price="$1000", brand=brand3, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/lg-g4s-beat.jpg")
session.add(LGItem2)
session.commit()


#################################################################


# Creates Brand Sony
brand4 = Brand(name= "Sony")
session.add(brand4)
session.commit()

# Creates Sony Item 1
SonyItem1 = Item(name="Xperia Z1", description="Sony's Xperia Z1",
                     price="$1000", brand=brand4, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/sony-xperia-z1-ofic.jpg")
session.add(SonyItem1)
session.commit()

# Creates Sony Item 2
SonyItem2 = Item(name="Xperia Z2", description="Sony's Xperia Z2",
                     price="$1000", brand=brand4, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/sony-xperia-z2-new.jpg")
session.add(SonyItem2)
session.commit()

# Creates Sony Item 3
SonyItem3 = Item(name="Xperia Z3", description="Sony's Xperia Z3",
                     price="$1000", brand=brand4, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/sony-xperia-z3.jpg")
session.add(SonyItem3)
session.commit()

# Creates Sony Item 4
SonyItem4 = Item(name="Xperia Tablet Z", description="Sony's Xperia Tablet Z",
                     price="$1000", brand=brand4, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/-sony-xperia-z4-tablet.jpg")
session.add(SonyItem4)
session.commit()


#################################################################


# Creates Brand Huawei
brand5 = Brand(name= "Huawei")
session.add(brand5)
session.commit()

# Creates Sony Item 1
HuaweiItem1 = Item(name="MediaPad 7 Youth", description="Huawei's MediaPad 7 Youth",
                     price="$1000", brand=brand5, user=user1, image="http://cdn2.gsmarena.com/vv/bigpic/huawei-mediapad-t1-70.jpg")
session.add(HuaweiItem1)
session.commit()

print "added items!"