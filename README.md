# Student-Utility-App

## To get started after clonning the repository:

# 1. we need to install all the packages to run the scripts so head over to terminal directed to this current directory and type the following:
  
  > ## i = use virtual environment(Recommended) to install it:  
  > ### pip install virtualenv


```python
      if i == True:         
          bash:
            virtualenv <venv name>
            source <venv name>/Scripts/activate
            pip install -r requiremts.txt

          cmd:
            virtualenv <venv name>
            <venv name>\Scripts\activate

      else:
        pip install -r requirements.txt
```

# 2. Inside the app.py script head over to  "Default images and music used && CONSTANTS" section (this is the first section) and read the commented function and do as instructed

# 3. As there is already an .exe build of the script you can head over to app.spec and find "-*- file location below to be changed with your path -*-" and do as instructed

# 4 To build the exe file yourself

	go to pyinstaller docs and do as instructed (Recommended)
  
   or
   
	inside in venv type: pyinstaller --onefile --noconsole app.py (the simplest way)
  

### >>>>> DONOT FORGET TO UPADTE YOUR .spec FILE AS in MENTIONED IN POINT 3 <<<<<


# Here goes some sample images:

### Front page without loading the weather and news
![image1](https://user-images.githubusercontent.com/66205793/120650815-c7715380-c49b-11eb-898e-233aca4405a0.jpg)

### Front page after loading the weather and news

![image2](https://user-images.githubusercontent.com/66205793/120650865-cf30f800-c49b-11eb-9437-f0c86d15e742.jpg)

### The Wikipedia tab with a view of the result of search

![image3](https://user-images.githubusercontent.com/66205793/120650981-e7a11280-c49b-11eb-9bc4-4e108b12ba9a.jpg)

### The Calculator Tab(I)

![image4](https://user-images.githubusercontent.com/66205793/120651076-fdaed300-c49b-11eb-96bd-9b328a554491.jpg)

### The Calculator Tab(II)

![image5](https://user-images.githubusercontent.com/66205793/120651191-220aaf80-c49c-11eb-8b45-93dc3a68db1d.jpg)

### Todo Tab showing some task to do
![image6](https://user-images.githubusercontent.com/66205793/120651106-099a9500-c49c-11eb-8399-46c02485ef14.jpg)


### Todo Tab showing some task to do along with the view of editing
![image7](https://user-images.githubusercontent.com/66205793/120651128-0f907600-c49c-11eb-8f4f-131263997fbb.jpg)

### Todo Tab showing some task to do with a task edited
![image8](https://user-images.githubusercontent.com/66205793/120651135-11f2d000-c49c-11eb-85bc-b9550b983878.jpg)

### The Local Music player tab(work in progress)
![image9](https://user-images.githubusercontent.com/66205793/120651145-161eed80-c49c-11eb-8e1b-d3312996e809.jpg)

### Credits
![image10](https://user-images.githubusercontent.com/66205793/120651179-1f0fbf00-c49c-11eb-9162-77100260f16e.jpg)
