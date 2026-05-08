# ConsoleMVC

Python으로 구현하는 MVC 패턴 실습 프로젝트입니다.
콘솔 기반의 사용자 관리 CRUD 애플리케이션을 통해 Model-View-Controller 구조를 학습합니다.

## 브랜치 안내

| 브랜치 | 설명 |
|--------|------|
| `main` | 스켈레톤 코드 — 클래스·메서드 선언만 작성, 구현부는 비어 있음 |
| `sample` | 완성된 구현 코드 + 테스트 — 참고용 |

> 막히는 부분이 있다면 `sample` 브랜치의 코드를 참고하세요.

## 프로젝트 구조

```
MVC_poc/
├── main.py                      # 진입점: 세 레이어 생성 후 controller.run() 호출
├── models/
│   └── user.py                  # User dataclass, UserRepository (인메모리 저장소)
├── views/
│   └── user_view.py             # 출력·입력 담당 (print / input 래핑)
├── controllers/
│   └── user_controller.py       # CRUD 흐름 조율, 메뉴 루프
└── tests/
    ├── test_model.py
    ├── test_view.py
    └── test_controller.py
```

## MVC 의존성 방향

```
main.py → Controller → Model
                    → View
```

- **Model** (`models/user.py`): 데이터와 비즈니스 로직 담당
- **View** (`views/user_view.py`): 화면 출력·사용자 입력만 담당
- **Controller** (`controllers/user_controller.py`): Model과 View를 연결하고 흐름을 제어

## 구현 목표

각 파일의 `pass`로 비어 있는 메서드를 직접 구현하세요.

### UserRepository (`models/user.py`)

| 메서드 | 설명 |
|--------|------|
| `add(user)` | id 부여 후 저장, 저장된 user 반환 |
| `get(user_id)` | id로 단건 조회, 없으면 `None` |
| `get_all()` | 전체 목록 반환 |
| `update(user_id, **kwargs)` | 필드 수정 (id 필드는 변경 불가) |
| `delete(user_id)` | 삭제 성공 시 `True`, 없으면 `False` |

### UserView (`views/user_view.py`)

| 메서드 | 설명 |
|--------|------|
| `show_user(user)` | 유저 단건 출력 |
| `show_user_list(users)` | 유저 목록 출력 (빈 경우 안내 메시지) |
| `show_message(message)` | 일반 메시지 출력 |
| `get_input(prompt)` | `input()` 래핑, `strip()` 적용 |

### UserController (`controllers/user_controller.py`)

| 메서드 | 설명 |
|--------|------|
| `create_user()` | 이름·이메일 입력받아 저장 |
| `list_users()` | 전체 유저 목록 출력 |
| `update_user()` | id 입력받아 이름 수정 |
| `delete_user()` | id 입력받아 삭제 |
| `run()` | 메뉴 루프 실행 (0 입력 시 종료) |

## 실행 방법

```bash
# 앱 실행
python main.py

# 테스트 실행
python -m pytest tests/ -v
```

## 요구 환경

- Python 3.10 이상
- pytest (`pip install pytest`)
