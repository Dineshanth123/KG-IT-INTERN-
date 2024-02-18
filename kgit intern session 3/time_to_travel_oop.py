class Time:
  def __init__(self,distance,speed):
    self.distance=distance
    self.speed=speed

  def display(self):
    x=self.distance
    y=self.speed
    return (x/y)*60
  
dis=float(input("enter dis in kms:"))
speed=float(input("enter speed in kms/hr:"))
obj=Time(dis,speed)
print("time taken in minutes:",round(obj.display(),2))
