

print("What is the name of your shape?")

Shapes = ["Cube","Cuboid","Cylinder","Cone","Sphere","Hemisphere","cube","cuboid","cone","cylinder","sphere","hemisphere"]
print(Shapes)

Name = str(input("Shape = "))
if Name == "Cube":
     side = (float(input("side = ")))
     Volume = side**3 ; TSA = 6 * side ** 2 ; CSA = 4 * side ** 2 
     print("Volume = ",Volume) ; print("TSA = ",TSA) ; print("CSA = ",CSA) 
elif Name == "Cuboid":
     length = float(input("length = "));breadth = float(input("breadth = "));height = float(input("height = "))
     Volume = length*breadth*height;TSA = 2*(length*breadth+breadth*height+height*length);CSA = 2*(length+breadth)*height 
     print("Volume = ",Volume) ; print("TSA = ",TSA) ; print("CSA = ",CSA)
elif Name == "Cylinder":
     radius = float(input("radius = ")) ; height = float(input("height = "))
     Volume = 3.14*radius**2*height ; TSA = 2*3.14*radius*(height + radius) ; CSA = 2*3.14*radius*height
     print("Volume = ",Volume) ; print("TSA = ",TSA) ; print("CSA = ",CSA)
elif Name == "Cone":
     height = float(input("height = ")) ; length = float(input("length = ")) ; radius = float(input("radius = "))
     Volume =  1/3*3.14*radius**2*height ; TSA = 3.14*radius*(length + radius) ; CSA = 3.14*radius*length
     print("Volume = ",Volume) ; print("TSA = ",TSA) ; print("CSA = ",CSA)
elif Name == "Sphere":
     radius = float(input("radius = "))
     Volume = 4/3*3.14*radius**3 ; TSA = 4*3.14*radius**2
     print("Volume = ",Volume) ; print("TSA = ",TSA) 
elif Name == "Hemisphere":
     radius = float(input("radius = "))
     Volume = 2/3*3.14*radius**3 ; TSA = 3*3.14*radius**2 ; CSA = 2*3.14*radius**2
elif Name == "cube":
     side = (float(input("side = ")))
     Volume = side**3 ; TSA = 6 * side ** 2 ; CSA = 4 * side ** 2 
     print("Volume = ",Volume) ; print("TSA = ",TSA) ; print("CSA = ",CSA) 
elif Name == "cuboid":
     length = float(input("length = "));breadth = float(input("breadth = "));height = float(input("height = "))
     Volume = length*breadth*height;TSA = 2*(length*breadth+breadth*height+height*length);CSA = 2*(length+breadth)*height 
     print("Volume = ",Volume) ; print("TSA = ",TSA) ; print("CSA = ",CSA)
elif Name == "cylinder":
     radius = float(input("radius = ")) ; height = float(input("height = "))
     Volume = 3.14*radius**2*height ; TSA = 2*3.14*radius*(height + radius) ; CSA = 2*3.14*radius*height
     print("Volume = ",Volume) ; print("TSA = ",TSA) ; print("CSA = ",CSA)
elif Name == "cone":
     height = float(input("height = ")) ; length = float(input("length = ")) ; radius = float(input("radius = "))
     Volume =  1/3*3.14*radius**2*height ; TSA = 3.14*radius*(length + radius) ; CSA = 3.14*radius*length
     print("Volume = ",Volume) ; print("TSA = ",TSA) ; print("CSA = ",CSA)
elif Name == "sphere":
     radius = float(input("radius = "))
     Volume = 4/3*3.14*radius**3 ; TSA = 4*3.14*radius**2
     print("Volume = ",Volume) ; print("TSA = ",TSA) 
elif Name == "hemisphere":
     radius = float(input("radius = "))
     Volume = 2/3*3.14*radius**3 ; TSA = 3*3.14*radius**2 ; CSA = 2*3.14*radius**2

else:
     print("Invalid Shape")

     