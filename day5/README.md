# Day 5

## For Loop

```py
for item in list_of_items:
  #Do something to each item
```

## For loop in a range

In javascript it would be like:

```js
for(i = 1; i < 100; i++){
  // do something
}
```
### Range

But in python we use ***range***:

```py
for number in range(1, 100):
  print(number)
```

In order to jump steps we can add a new parameter to the range function

```py
for number in range(1, 11, 3):
  print(number)

# Now we have
# 1
# 4
# 7
# 10 
```