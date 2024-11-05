# Pygame UI

Since pygame doesnot have any gui features and only draws shapes and handle event loop I decided to make UI components for making menus similar to flutter widget. If you ever created flutter apps this should be easier.
### Features
Button, Row, Column

## Getting Started
First create the ui object
```python
btn = Button(x=0, y=0, text="Hello", onClick=func)
btnRow = Row(x=0, y=90, marginRight=5, children=[btn1, btn2])
```
use `.draw(surface)` method to draw which takes `pygame.Surface` as parameter.
```python
while running:
  btn.draw(window)
  btnRow.draw(window)
```
use `.handleEvent(event)` which takes `pygame.event` to handle event.
```python
while running:
  ...
  for event in pygame.event.get():
    btn.handleEvent(event)
    btnRow.handleEvent(event)
...
```
## Documentaion
#### default Button
![image](https://github.com/user-attachments/assets/8f4e48f0-1fc6-4154-a943-5b086c1444d8)
```python
default = Button(
    x= 50,
    y= 80,
    text= "Default Button",
    onClick= buttonEvent
)
```
```python
custom = Button(
    x= 220,
    y= 50,
    width= 300,
    height=100,
    fill= (230, 57, 43), #red
    borderColor=(255, 235, 59), #yellow
    borderRadius= 50,
    fontSize=32,
    text= "Customized Button",
    onClick=buttonEvent
)
```
#### Imaged Button
![image](https://github.com/user-attachments/assets/b0c27c73-5e0c-42f4-9a69-b63e7641d026)
```python
btn = Button(
        x=0, y=0,
        centered= True,   
        text= "Img Button",
        image="assets/btn1.png",
        onClick=func
      )
```
#### Row
![image](https://github.com/user-attachments/assets/4aa9bf9b-dafa-44a9-8086-7fe6ae4169da)
```python
rowBtns = Row(x=50, y=50, marginRight=15, children=[btn1, btn2, btn3])
```
#### Column
![image](https://github.com/user-attachments/assets/a22d5765-c9d9-4bcf-a7ba-7128c42a9419)
```python
colBtns = Column(x=50, y=50, marginRight=15, children=[btn1, btn2, btn3])
```
#### Row-Column nested
![image](https://github.com/user-attachments/assets/7bb312d7-501f-4800-bf05-3e50e6fbd501)
```python
rowBtns1 = Row(x=50, y=50, marginRight=15, children=[button3, button4, button5])
rowBtns2 = Row(x=50,y=50, marginRight=15, children=[button6, button7])
colBtns = Column(x=50, y=50, marginBottom=15, children=[rowBtns1, rowBtns2])

```

