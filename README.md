
## 目標
使用 python 建立一處理 3D 檔的功能，可以將 STEP 或 IGES 檔案 轉換成 3D 縮圖。

## 安裝程序

## 1. Install anaconda
https://www.anaconda.com/distribution/#download-section

## 2. Create environment

+ Open Anaconda Prompt and input command

`conda create -n pythonocct -c dlr-sc -c pythonocc pythonocc-core=7.4.0rc1`

![](https://i.imgur.com/jFsMFPy.png)



## 3. Start environment

input command
`
activate pythonocct
`
![](https://i.imgur.com/UnsD6KA.png)


## 4. Install the wxGUI library 
input command
`pip install wxPython`
![](https://i.imgur.com/fNOo873.png)


## 5. Download the program
input command

`git clone https://github.com/stigersmile/3dmodel.git `
![](https://i.imgur.com/Jzoxgsi.png)

## 6. Run the program

go into 3dmodel file and input command
`python main.py`
![](https://i.imgur.com/bHVRVhb.png)


## 7. Load the 3d model

File -> step or iges file 

select the 3d model in 3dmodel/3dfile


![](https://i.imgur.com/GwMn1m2.png)

3dfile/surf114.igs
![](https://i.imgur.com/ZCCxXXn.png)

3dfile/as1-oc-214.stp
![](https://i.imgur.com/0bSvT6m.png)


## Future function
**big file size case:**
suggest to use x3dom render and run in the background (multi threads) and after finish renderting, embed the iframe to the UI.


## Reference
https://github.com/tpaviot/pythonocc-core
