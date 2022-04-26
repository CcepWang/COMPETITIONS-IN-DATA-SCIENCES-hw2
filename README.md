# COMPETITIONS-IN-DATA-SCIENCES-hw2

## app.py若是無法執行，可以使用colab直接運行
colab:https://colab.research.google.com/drive/1y1c0AV8kn-3yWlMI78nveQrvdamk4-yr?usp=sharing

### preprocessing
- 因為prophet必須要有日期參數，故先將資料加入日期
- 僅取出資料中的'open'作為訓練參數
- 觀察training參數曲線圖
![下載](https://user-images.githubusercontent.com/37070545/165309485-2b661dc8-2591-4903-99ac-f53e2199723e.png)
### data
- 僅取出資料中的'open'作為訓練參數
- 將資料調整成模型需要的輸入格式
### training
- 這次使用的是FB的Prophet，或稱“Facebook Prophet”，是一個由Facebook開發的用於單變數時間序列預測的開源庫。
- Prophet實現的是一個可加的時間序列預測模型，支援趨勢、季節性週期變化及節假日效應。
- “該模型所實現的是一個基於可加模型的時間序列資料預測過程，擬合了年度、周度、日度的季節性週期變化及節假日效應的非線性趨勢。” — Package ‘prophet’, 2019.
### predict
![下載 (1)](https://user-images.githubusercontent.com/37070545/165310384-a33e5eb4-753b-4047-9275-0a8ff109f33e.png)
- 取出最後實際預測的曲線
![下載 (2)](https://user-images.githubusercontent.com/37070545/165310850-66fc4c87-3149-428e-b7ef-71343e5f292d.png)
- 與實際值做比較

![下載 (3)](https://user-images.githubusercontent.com/37070545/165310678-94ac01e6-2725-4be1-b104-0856d4af1321.png)
### strategy
- 算出後天與前天的漲跌狀況，如果是漲，則標記為'^'，相反則為'v'
![下載 (4)](https://user-images.githubusercontent.com/37070545/165311589-49b25ff7-6af0-4b9a-be5a-5c4e48da9fa9.png)
- 以此判斷當天的策略應該是買進或是賣出，並且遵守unit介於-1到1之間
### result
- 最終的profit為2.25
### conclusion
- 因為這個策略的結果並不算太好，所以曾經嘗試了增加特徵來做訓練，但是最終由於技術問題以失敗告終。
