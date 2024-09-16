import enum


# @enum.unique これをつけると同じステータス名をゆるさない
class Status(enum.Enum):
    ACTIVE = 1
    RENAME_ACTIVE = 1  # 別名として定義する（valからは呼び出せない）
    INACTIVE = 2
    RUNNING = 3


print(Status.ACTIVE)
print(Status.ACTIVE == 1)  # enum.Intnumを継承すればTrue
print(Status.ACTIVE == Status(1))
print(repr(Status.ACTIVE))
print(Status.ACTIVE.name)
print(Status.ACTIVE.value)

for s in Status:
    print(s)
    print(type(s))

print(Status(1))

# 値を整数で管理するためDB容量を節約できる


# 実行、書き込み、読み込みの権限を管理
class Perm(enum.IntFlag):
    R = 4
    W = 2
    X = 1


print(Perm.R | Perm.W)
print(repr(Perm.R | Perm.W))
