![](#flypie-solution-etl.svg)

該方案本質是一個 [ETL](#ETL) 工作流程，資料涉及三個階段：

- OpenStreerMap
  - 提供台灣道路圖資
- [OpenDRIVE](#OpenDRIVE)
  - [CARLA](#CARLA) 支援的匯入格式，也是道路模擬通用的[高精度地圖](#高精度地圖)格式。
- [CARLA](#CARLA)
  - [CARLA](#CARLA) 本身基於 [UE4](#UE4)，圖資匯入後可以在基於 [UE4](#UE4) 的界面與環境中瀏覽與調整。
  - [OpenDRIVE](#OpenDRIVE) 本身僅包含道路資訊，並不包含遊戲化（模擬）所需的 3D 素材，例如：道路貼圖、建築模型...等。

---

- [CARLA](#CARLA) 支援大型地圖的切塊與動態載入，詳情請見 [Town 11](<#Town 11>)。
- [CARLA](#CARLA) 支援卡車，詳情請見 [CARLA 卡車](<#CARLA 卡車>)。

---

關於方案的前期決策，請見：[FlyPie對於方案觀點](#FlyPie對於方案觀點)。