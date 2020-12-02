from matplotlib import pyplot as plt 


y = [90,80,85,75,65,60,5]
x = ['ML & DL', 'Django', 'HTML5', 'JavaScript', 'CSS3', 'Bootstrap', 'VUE.JS']
colours = ['#39d084', '#30a5dc', '#7447f0', '#ee742b', '#d0ce39', '#ee2bbd', 'red']

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12,8))
ax1.barh(x,y, height=0.8, color=colours, edgecolor='white')
for index, value in enumerate(y):
    ax1.text(value, index, str(value), color='white')
plt.legend()
ax2.pie(y, labels=x, colors=colours,shadow=True)
ax2.set_title('Skills Pie Chart', fontsize=24, color='white')

ax1.set_title('Skills Bar Chart', color='white', fontsize=24)
ax1.set_xlabel('x title', color='violet', fontsize=24)
ax1.set_ylabel('y title', color='violet', fontsize=24)

ax1.set(title='Skills Bar Chart',
xlabel='Proficiency Level (%)',
ylabel='Skills')
ax1.set_title('Skills Bar Chart', color='white', fontsize=24)
plt.setp(ax1.get_xticklabels(), color='white')
plt.setp(ax1.get_yticklabels(), color='white')
plt.suptitle('NWOVU SUNDAY SKILLS PROFICIENCY LEVEL', color='white', fontsize=24)
plt.savefig('skillsbart', transparent=True)
plt.show()