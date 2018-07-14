# DisplayString-Django
 Display String using Django Web  Framework 

![screenshot from 2018-07-14 12-12-39](https://user-images.githubusercontent.com/3431730/42721909-1aeab9e2-8760-11e8-9702-71a69e9b0bb2.png)

Before going ahead, Let me demonstrate what results will come at the end so that clear vision is set in the readers who is reading this. 

![output](https://user-images.githubusercontent.com/3431730/42722109-efcdec8a-8763-11e8-89cf-6b958db581eb.png)

---

### How to Run File ###
To run the file please move to main folder which is Project_folder and list the content of this folder. You can use dir command for windows and ls for ubuntu. YOu will find the file manage.py. Please run the follwing command
```
python manage.py runserver
```
![runserver](https://user-images.githubusercontent.com/3431730/42722252-6fdcb10c-8766-11e8-97ce-14eeb0518da5.png)

Please go the address shown in the image and you will be shown the result added in the image above this image.

---

### How to change the string shown as a result because all wants something else to be displayed ###
For such please go to the file views.py which you can find under the Application_folder and pass another string in the function which I have created there. I am adding the screenshot here so that it becomes easy for you.

![views](https://user-images.githubusercontent.com/3431730/42722309-5b164f7a-8767-11e8-8923-4d8516655a37.png)

Please add the Application_folder in the settings.py file which you can find in  the Project_folder created using startproject. Please locate that file and add the Application_folder in it so that Such can be integrated with Project_folder. To make you understand you more Project_folder is created using
```
django-admin.py startproject name_folder(Project_folder in my case)
```
In the same way your application is created using following command
```
django-admin.py startapp name_folder(Application_folder in my case)
```
For more undestanding please look at my code file so that you can know each thing in precise manner.

Thanks a lot for spendind some time in reading my readme file. If you gain some good points, it is **great**.
