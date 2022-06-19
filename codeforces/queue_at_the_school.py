def update_position(s_graph, g_indexes,n,t):
  for i in range(t):
    for j in range(len(g_indexes)):
      val=  g_indexes[j]
      if val + 1 < n and s_graph[val+1]== 'G':
        s_graph[val] = 'G'
        s_graph[val+1] = 'B'
        
        g_indexes.remove(val)
        g_indexes.insert(j, val+1)
  return s_graph

if __name__=="__main__":
  n,t = map(lambda x: int(x), input().split(' '))
  s = list(input())
  g_indexes = []
  
  s_graph = {}

  for (idx, val) in enumerate(s):
    if val == 'B':
      g_indexes.append(idx) 
    
    s_graph[idx] = val
  
  result = update_position(s_graph, g_indexes, n, t)
  print(('').join(list(result.values())))

