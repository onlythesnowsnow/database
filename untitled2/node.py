1 # -*- coding:utf8 -*-
  2 #/usr/bin/env python
  3 
  4 class Node(object):
  5     def __init__(self, data, pnext = None):
  6         self.data = data
  7         self._next = pnext
  8 
  9     def __repr__(self):
 10         return str(self.data)
 11 
 12 class ChainTable(object):
 13     def __init__(self):
 14         self.head = None
 15         self.length = 0
 16 
 17     def isEmpty(self):
 18         return (self.length == 0)
 19 
 20     def append(self, dataOrNode):
 21         item = None
 22         if isinstance(dataOrNode, Node):
 23             item = dataOrNode
 24         else:
 25             item = Node(dataOrNode)
 26 
 27         if not self.head:
 28             self.head = item
 29             self.length += 1
 30 
 31         else:
 32             node = self.head
 33             while node._next:
 34                 node = node._next
 35             node._next = item
 36             self.length += 1
 37 
 38     def delete(self, index):
 39         if self.isEmpty():
 40             print "this chain table is empty."
 41             return
 42 
 43         if index < 0 or index >= self.length:
 44             print 'error: out of index'
 45             return
 46 
 47         if index == 0:
 48             self.head = self.head._next
 49             self.length -= 1
 50             return
 51 
 52         j = 0
 53         node = self.head
 54         prev = self.head
 55         while node._next and j < index:
 56             prev = node
 57             node = node._next
 58             j += 1
 59 
 60         if j == index:
 61             prev._next = node._next
 62             self.length -= 1
 63 
 64     def insert(self, index, dataOrNode):
 65         if self.isEmpty():
 66             print "this chain tabale is empty"
 67             return
 68 
 69         if index < 0 or index >= self.length:
 70             print "error: out of index"
 71             return
 72 
 73         item = None
 74         if isinstance(dataOrNode, Node):
 75             item = dataOrNode
 76         else:
 77             item = Node(dataOrNode)
 78 
 79         if index == 0:
 80             item._next = self.head
 81             self.head = item
 82             self.length += 1
 83             return
 84 
 85         j = 0
 86         node = self.head
 87         prev = self.head
 88         while node._next and j < index:
 89             prev = node
 90             node = node._next
 91             j += 1
 92 
 93         if j == index:
 94             item._next = node
 95             prev._next = item
 96             self.length += 1
 97 
 98     def update(self, index, data):
 99         if self.isEmpty() or index < 0 or index >= self.length:
100             print 'error: out of index'
101             return
102         j = 0
103         node = self.head
104         while node._next and j < index:
105             node = node._next
106             j += 1
107 
108         if j == index:
109             node.data = data
110 
111     def getItem(self, index):
112         if self.isEmpty() or index < 0 or index >= self.length:
113             print "error: out of index"
114             return
115         j = 0
116         node = self.head
117         while node._next and j < index:
118             node = node._next
119             j += 1
120 
121         return node.data
122 
123 
124     def getIndex(self, data):
125         j = 0
126         if self.isEmpty():
127             print "this chain table is empty"
128             return
129         node = self.head
130         while node:
131             if node.data == data:
132                 return j
133             node = node._next
134             j += 1
135 
136         if j == self.length:
137             print "%s not found" % str(data)
138             return
139 
140     def clear(self):
141         self.head = None
142         self.length = 0
143 
144     def __repr__(self):
145         if self.isEmpty():
146             return "empty chain table"
147         node = self.head
148         nlist = ''
149         while node:
150             nlist += str(node.data) + ' '
151             node = node._next
152         return nlist
153 
154     def __getitem__(self, ind):
155         if self.isEmpty() or ind < 0 or ind >= self.length:
156             print "error: out of index"
157             return
158         return self.getItem(ind)
159 
160     def __setitem__(self, ind, val):
161         if self.isEmpty() or ind < 0 or ind >= self.length:
162             print "error: out of index"
163             return
164         self.update(ind, val)
165 
166     def __len__(self):
167         return self.length