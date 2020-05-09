# 알파벳 순서대로 갔다가
# 만약 길이 없다면(티켓을 이미 다 소진했거나 처음부터 없었다면) 다시 돌아와야 한다 -> 스택에 쌓는다
# 어차피 한붓그리기가 실패하는 경우는 없다고 문제에서 명시했다
# 다시 돌아와서 스택에 계속 쌓아올리고
# 모든 도시를 방문했으면 스택에서 꺼낸 뒤
# 그걸 다시 거꾸로 출력하면 된다(스택은 last in first out이므로)


def solution(tickets):
    d = {}
    for t in tickets:
        d[t[0]] = d.get(t[0], []) + [t[1]]
    for x in d:
        d[x].sort(reverse=True)  # 끝에서부터 자르는게 리스트에서 효율적이므로 정렬을 reverse로 한다

    stack = ["ICN"]
    path = []

    while len(stack) > 0:
        top = stack[-1]
        if top not in d or len(d[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(d[top][-1])
            d[top] = d[top][:-1]
    return path[::-1]
