# import sys; sys.stdin = open("dfs.txt")
#
# def dfs(v):
#     # 방문처리
#     visited[v] = 1
#     print(v, end=' ')
#     # v의 인접한 모든 정점(w)에 대해서
#     for w in adj_list[v]:
#         # 방문 안한 정점이 있으면
#         if visited[w] == 0:
#             dfs(w)
#     return
#
# V, E = map(int, input().split())  # 정점, 간선
# adj_list = [[] for _ in range(V)]
# visited = [0] * (V)
# # temp  = list(map(int, input().split()))
# # print(temp)
# #인접리스트로 저장하기
# for i in range(E):
#     s, e = map(int, input().split())
#     adj_list[s].append(e)
#     # adj_list[e].append(s)
#
# print(adj_list)
# dfs(0)
stack = []
print(not stack)