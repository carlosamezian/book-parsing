# import math
# class triangle_area:
    
#     def __init__(self, base, hieght, is_right = False):
        
#         self.base = base
#         self.hieght = hieght
#         self.is_right = is_right 
        
#     def hypotenuse(self):
#         if self.is_right == True:
#             c  = 0 
#             c = (self.base**2) + (self.hieght**2)
#             return math.sqrt(c)
#         else:
#             return "Triangle isn't a right triangle."    
#     def area(self):
#         if self.base and self.hieght > 0 :
#             a = (0.5) * self.base * self.hieght
#             return a
#         else:
#             return ValueError
                  
# if __name__ == "__main__":
#     triangle1 = triangle_area(4, 3, True)
#     triangle2 = triangle_area(10 , 4, False)
    
#     print(triangle1.hypotenuse())
#     print(triangle1.area())
#     print(triangle2.hypotenuse())
#     print(triangle2.area())

def ran(x = None):
    return x

if __name__ == "__main__":
    ran()