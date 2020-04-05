quick export component for kwaku - export nodes to json arrays of objects.

config:
  query: the query to select the nodes to include
  atributes: an array of attribute definitions for the nodes. Key is the attribute name, value of the graph path to the value. E.g. -author.title is the path to the title of the node connected through in-edges labelled "author".
  