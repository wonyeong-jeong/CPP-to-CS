import clang.cindex # type: ignore


# libclang.dll 경로 설정
clang.cindex.Config.set_library_file('C:\\Program Files\\LLVM\\bin\\libclang.dll')

# Clang 인덱스 생성
index = clang.cindex.Index.create()

# 이후 코드 작성 및 실행

# C++ 파일 파싱
translation_unit = index.parse('example.cpp')

# AST 탐색 및 출력
def traverse_ast(node, level=0):
    print('  ' * level + f'{node.kind} {node.spelling}')
    for child in node.get_children():
        traverse_ast(child, level + 1)

# 루트 노드부터 시작하여 AST 탐색
traverse_ast(translation_unit.cursor)
