# Pygame UI

Since pygame doesnot have any gui features and only draws shapes and handle event loop I decided to make UI components for making menus similar to flutter widget. If you ever created flutter apps this should be easier.
### Features
- Button
- Column
- Row
### screenshot
![image](https://github.com/user-attachments/assets/4abaef85-ab19-47f3-ad96-be992bc94aad) 

### Documentation
Common For all:
1. first create the object.
```python
btn1 =  Button(
            fill=Colors.red,
            x=0, y=0,
            centered= True,   
            text= "Item 4",
            onClick=lambda:print("Item 4")
        )

btnRow = Row(0,0,20, [
        Button(
            x=0, y=0,
            centered= True,   
            text= "Item 4",
             image="assets/btn1.png",
            onClick=lambda:print("Item 4")
        ),
        Button(
            x=0, y=0,
            height= 220,
            # width= 50,
            centered= True,   
            text= "Item 5",
            onClick=lambda:print("Item 5"),  
        ),
    ])
```
2. use `.draw(surface)` method to draw which takes `pygame.Surface` as parameter.
```python
...
while running:
  btn1.draw(window)
  btnRow.draw(window)
...
```
3. use `.handleEvent(event)` which takes `pygame.event` to handle event.<br>
```python
while running:
  ...
  for event in pygame.event.get():
    btn1.handleEvent(event)
    btnRow.handleEvent(event)
...
```

(incomplete documentaion)
