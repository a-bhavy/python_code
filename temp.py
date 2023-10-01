import matplotlib.pyplot as plt

DAYS = ['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
TEMPERATURE= [34,34,33,34,29,24,23]
  
plt.plot(DAYS, TEMPERATURE, color='red', marker='o')
plt.title('TEMPRATURE IN GURGAON', fontsize=14)
plt.xlabel('DAYS', fontsize=14)
plt.ylabel('TEMPERATURE', fontsize=14)
plt.grid(True)
plt.show()