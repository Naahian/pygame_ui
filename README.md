# Pygame UI

Since pygame doesnot have any gui features and only draws shapes and handle event loop I decided to make UI components for making menus similar to flutter widget. If you ever created flutter apps this should be easier.
### Features
Button, Row, Column, ToggleSwitch, Text (dropdown, Slider coming soon...)

## Usage
First create the ui object and function for click event(for buttons)
```python
def clickEvent():
    print("Button Event called!")

btn = Button(x=0, y=0, text="Hello", onClick=clickEvent)
btnRow = Row(x=0, y=90, marginRight=5, children=[btn1, btn2])
```
use `.draw(surface)` method to draw which takes `pygame.Surface` as parameter.
```python
while running:
  window.fill((255,255,255))
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
![|200](https://github.com/user-attachments/assets/f2fd5409-9257-4af6-91b8-06d40f2a493f)
#### default Button
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
    centered= True, #whether to use x,y as the center of the button or not   
    fill= (230, 57, 43), #red
    borderColor=(255, 235, 59), #yellow
    borderRadius= 50,
    fontSize=32,
    text= "Customized Button",
    onClick=buttonEvent
)
```
#### Imaged Button
```python
btn = Button(
        x=0, y=0,
        text= "Img Button",
        image="assets/btn1.png",
        onClick=func
      )
```
![qa](https://github.com/user-attachments/assets/7249c145-5401-41ba-a1f3-0184b841d667)
(x,y of children is ignored when drawn)
#### Row
```python
rowBtns = Row(x=50, y=50, marginRight=15, children=[btn1, btn2, btn3])
```
#### Column
```python
colBtns = Column(x=50, y=50, marginBottom=15, children=[btn1, btn2, btn3])
```
#### Row-Column nested
```python
rowBtns1 = Row(x=50, y=50, marginRight=15, children=[button3, button4, button5])
rowBtns2 = Row(x=50,y=50, marginRight=15, children=[button6, button7])
colBtns = Column(x=50, y=50, marginBottom=15, children=[rowBtns1, rowBtns2])
```
or
```python
colBtns = Column(
    x=50,
    y=50,
    marginBottom=15,
    children=[
        Row(x=50, y=50, marginRight=15, children=[
            Button(x= 0, y= 0, text= "Button 1", onClick= button1Event),
            Button(x= 0, y= 0, text= "Button 2", onClick= button2Event),
            Button(x= 0, y= 0, text= "Button 3", onClick= button3Event),
        ]),
        Row(x=0, y=0, marginRight=15, children=[
            Button(x= 0, y= 0, text= "Button 4", onClick= button4Event),
            Button(x= 0, y= 0, text= "Button 5", onClick= button5Event),
        ]),
    ])
```
![image](https://github.com/user-attachments/assets/e3882d5a-9626-4235-a44c-cf2c6630acd9)
#### Text
```python
text = Text(x=0, y=0, text="Some Text")
styled = Text(0,0,"Styled Text ", size= 28, color=(255, 152, 0),family="Georgia")
```
#### ToggleSwitch
```python
toggle1 = ToggleSwitch(x=0,y=0,) 
toggle2 = ToggleSwitch(x=0,y=0, width=80, color=(95, 216, 18), onActive=func) 
toggle1State = toggle1.value #boolean
```
