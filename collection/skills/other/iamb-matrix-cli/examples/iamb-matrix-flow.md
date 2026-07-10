# iamb Matrix Flow Example

## 场景
目标：完成 Matrix 用户注册、token 获取、Space ID 查询，并在 iamb 中维护空间子房间。

## 1) 注册用户
```bash
python collection/skills/iamb-matrix-cli/scripts/matrix_iamb_helper.py register \
  --homeserver https://matrix.example.com \
  --username demo_user
```

## 2) 登录并获取 token
```bash
python collection/skills/iamb-matrix-cli/scripts/matrix_iamb_helper.py login \
  --homeserver https://matrix.example.com \
  --user @demo_user:matrix.example.com
```

## 3) 查询 Space IDs
```bash
python collection/skills/iamb-matrix-cli/scripts/matrix_iamb_helper.py space-ids \
  --homeserver https://matrix.example.com \
  --access-token '<TOKEN>'
```

## 4) iamb 内部操作
```text
:spaces
:room id show
:space child set !child_room:matrix.example.com ++suggested
:space child remove
```
