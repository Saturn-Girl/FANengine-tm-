# FANengine™

**FANengine™** is a proprietary but source-available game engine for 3DS MAX developed by **Saturn Computing Topic**.

---

## 🧩 How to Use

```python
import FANengine
```


example seting it up
```python
import FANengine

FANengine.Init()
FANengine.Run()
```
example loading an model
```python
import FANengine

FANengine.Init()
LoadModel("MyModel.obj")
FANengine.Run()
```
example loading music
```python
import FANengine
FANengine.Init()
FANengine.PlaySound('assets/music/theme.ogg', loop=True, volume=0.5)
FANengine.Run()
```
