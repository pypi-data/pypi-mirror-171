# JoelData
Simple data types I to use in my projects.

# Documentation
## Stack
FIFO (like a stack of cups)

```py
from joeldata import Stack
my_stack=Stack()
```

* `push(item)` - adds new item
* `pop() -> item` - removes item
* `peek() -> item` - see top item without removing
* `is_empty() -> bool`


## Queue
LIFO (like a line at a store)

```py
from joeldata import Queue
my_q=Queue()
```

* `enqueue(item)` - add new item
* `dequeue() -> item` - remove an item
* `peek() -> item` - see the item that next to be dequeued
* `is_empty() -> bool`



## BST (aliased to Binary Search Tree)
Stores a list of numbers in a tree where each node can have up to two chiuldren. The left node is always less than the parent node and the right node is always greater than the parent node.

```py
from joeldata import BST
my_bst=BST()
```

* `add(item)` - adds an item to the BST
* `search(value) -> bool` - sees if a value is in the BST
* `inorder() -> item[]` - returns the items as an array in order
* `remove(item)` - removes an item from the BST

