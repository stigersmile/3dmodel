# 安裝程序

## 1. Install anaconda
https://www.anaconda.com/distribution/#download-section

## 2. Create environment

+ Open Anaconda Prompt and input command

`conda create -n pythonocct -c dlr-sc -c pythonocc pythonocc-core=7.4.0rc1`

![](https://i.imgur.com/5TfqNgv.png)


## 3. Start environment

input command
`
activate pythonocct
`

## 4. Install the wxGUI library 
input command
`pip install wxPython`

## 5. Download the program
input command

`git clone https://github.com/stigersmile/3dmodel.git `

## 6. Run the program

go into 3dmodel file and input command
`python main.py`

## 7. Load the 3d model

File -> step or iges file and
the 3d model will show on the screen

![](https://i.imgur.com/GwMn1m2.png)

example/surf114.igs
![](https://i.imgur.com/ZCCxXXn.png)

example/as1-oc-214.stp
![](https://i.imgur.com/0bSvT6m.png)


## Reference
https://github.com/tpaviot/pythonocc-core