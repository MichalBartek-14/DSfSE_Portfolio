
import numpy as np
import pandas as pd

#==== CLASSES and operations
class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y
    def distance_to_origin(self):
        return np.sqrt(self.x**2 + self.y**2)
    def reflect(self, axis):
        self.axis = axis
        if axis =='x':
            self.y = -self.y
        elif axis =='y':
            self.x = -self.x
        else:
            print('wrong value')

pt = Point(x=8.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())

class Book:
    genre = 'novel'
    def __init__(self, author, name, year, rating):
        self.author = author
        self.name = name
        self. year = year
        self.rating = rating
    def __str__(self):
        return f"The Book is {self.name}"\
               f"by {self.author} written in"\
               f"{self.year} with the rating of {self.rating}"

B1=Book('Igor Tomo', 'SNP',2023,8.7)
print(B1)

class Footballer:
    def __init__(self, name, country, club, rating, position):
        self.name =  name
        self.country = country
        self.club = club
        self.rating = rating
        self.position = position
    def __str__(self):
        return (f'The football player {self.name} from {self.country}'
                f' ,on club level playing for {self.club} has the rating'
                f' of {self.rating} and plays as {self.position}')
f1=Footballer('Messi','Argentina','Miami',88,'attacker')
f2=Footballer('Lobotka','Slovakia', 'Napoli',87,'midfielder')
print(f1)
print(f2)
#==== DATA FRAMES and OPERATIONS on them

np.random.seed(10)
size = 40
names = ['Alice','Bob','Jacob','Lucy','Hannah']
lastnames = ['Smith','Bahrami','Kovac','Abatu', 'Schwarz','Lapaj','Zajac','Taylor']
cities = ['Dallas','Talahasee','Spokane','Denver','Charlotte','St.Louis','Alberquque','Peoria','Providence','Chedar Rapids','Mobile']
data = {'Name': np.random.choice(names, size=size, replace = True),
        'Last Name': np.random.choice(lastnames, size=size, replace = True),
        'City': np.random.choice(cities, size=size),
        'Age':np.random.randint(20,60, size = size),
        'Salary':np.random.randint(1000,40000, size = size)}

df = pd.DataFrame(data)
average_sal= df['Salary'].mean()
high_sal = (df[df['Salary']>20000])
mean_sal_bycity = df.groupby('City')['Salary'].mean()
#print(df)
print(high_sal)


#====Salary
#print(mean_sal_bycity)
Spokane = df[df['City'] == 'Spokane']['Salary']
#print(Spokane)
print(average_sal)

#==== Lists
list=[1,3,5,6,10,12,30,48,54,67,77,83]
seventh = list[6]  #seventh element
only_last = list[5:] #last five elements
list.append(99) #appends 99 to the end
list.insert(4,8) #inserts 8 into 5th position

#print(list)
evens = [x for x in list if x % 2 == 0]
odd = [y for  y in list if y % 2 != 0]
## NESTED LIST
nested=[[1,2],[3,4],[5,6]]
flattened_list = [item for sublist in nested for item in sublist]
print(flattened_list)
print(len(flattened_list))

nested2= [['kamo','kde'],['si','ty'],['nenazrany','kono']]
veta_flat = [slovo for sublist in nested2 for slovo in sublist]
print(veta_flat)

##start to ndvi project
class SatelliteImage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.image_data = None #set to None  by default
        self.meta_data = None
    def load_image(self):
        with rasterio.open(self.file_path) as src:
            self.image_data = src.read() #all the bands
            self.meta_data = src.meta()

    def get_band(self, band_number):
            if band_number is None:
                print(f"the "band_number" does not exist")
            else:
                return self.image_data[band_number)
class ImageProcessing:
    def __init__(self, redband, nirband):
        self.redband = redband
        self.nirband = nirband
    def ndvi(self):
        #NDVi = NIR - red / nir + red
        ndvi = (self.nirband.astype(float) - self.redband.astype(float)/
                self.nirband.astype(float) + self.redband.astype(float))
        return ndvi

#class MeanNDVI:
#workflow#
files = sorted(f for f in list if f.endswirth('.tif'))
ndvi_series[]
for file in files:
    #name formatting
#load the data with correct names...
    sat_image = SatelliteImage(,path_to_files)
    sat_image = load_image()
    redband = sat_image.get_band()
#ndvi calculation
#analyse ndvi
